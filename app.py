import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import math

import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, ALL

from StringArtShapes import Triangle, Square

# TODO
# Add Cross
# Upload & Deploy somewhere online
# Animation button https://plotly.com/python/animations/
# Bug: When changing the number of nails, the sliders of the layers should update...


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.renderer = 'var renderer = new DashRenderer();'

# App layout
app.layout = html.Div([
    
    html.H1("StringArt Generation App with Dash", style={'color': '#FFA200', 'text-align': 'center'}),

    html.Div([
        html.P('Select a StringArt Frame Shape',style={'text-align': 'center'}),
        html.Div(
        dcc.RadioItems(id="slct_shape",
            options=[
                {'label': 'Triangle    ', 'value': 'T'},
                {'label': 'Square    ', 'value': 'S'},
                {'label': 'Cross    ', 'value': 'C'}
            ],
            value='T',
            labelStyle={'display': 'inline-block'},
            style={}
            # value='T',style={'width':'30%', 'color': colors['text'], 'paddingLeft':'22%'}
            ),style={'display': 'flex', 'justifyContent': 'center', 'font-size': 25, "marginRight": 20}
        ),
    ]),
    html.Div([
        html.Div([
            html.P('Width (mm)',style={'text-align': 'center'}),
            dcc.Input(id="in_width",
                placeholder='Width (mm)...',
                type='number',
                value=500
            )
        ]),
        html.Div([
            html.P('Frame Thickness (mm)',style={'text-align': 'center'}),
            dcc.Input(id="in_thick",
                placeholder='Thickness of frame (mm)...',
                type='number',
                value=30
            )
        ]),
        html.Div([
            html.P('Number of Nails per Side',style={'text-align': 'center'}),
            dcc.Input(id="in_nails",
                placeholder='Number of nails per side...',
                type='number',
                value=30
            )
        ])
    ],style={'display': 'flex', 'justifyContent': 'center'}),

    html.P('Add layers and adjust them to create a piece of string art.'),
    html.Div([
        html.Button("Add Layer", id="add-layer", n_clicks=1),
        html.Button("Reset StringArt", id="reset",n_clicks=0),
    ],style = {'display': 'inline-block'}),
    

    html.Br(),
    dcc.Tabs(id='layer-tabs',children=[], value=''),

    # Slider for progression in plot
    dcc.Slider(id="sld_nails",
        min=0,
        max=10,
        step=1,
        value=0
    ),

    # Display graph / plot
    html.Div(
    dcc.Graph(id='stringart_plot', figure={},style={'display': 'inline-block'}),
    style={'justifyContent': 'center','display': 'flex'})
    ]
)

# Callback--------------------------------------------------------------------------
def reset_layers():
    children = []
    n_clicks = 1
    curr_layer = 0
    return children, n_clicks, 'tab-'+str(curr_layer)

@app.callback(
    [Output('layer-tabs', 'children'),
    Output('add-layer','n_clicks'),
    Output('layer-tabs','value')],

    [Input('add-layer', 'n_clicks'),
    Input('reset','n_clicks'),
    Input(component_id='slct_shape', component_property='value')],

    [State('layer-tabs', 'children'),
    State('layer-tabs', 'value'),
    State('in_nails', 'value')]
)
def display_layers(n_clicks,_,slct_shape, children, selected_tab, n_nails):
    print(dash.callback_context.triggered[0]['prop_id'].split('.')[0])
    if dash.callback_context.triggered[0]['prop_id'].split('.')[0] == 'slct_shape':
        children = []
        n_clicks = 1
    if dash.callback_context.triggered[0]['prop_id'].split('.')[0] == 'reset':
        children = []
        n_clicks = 1

    shape = get_shape(slct_shape,1,1,1)

    new_layer = new_layer_tab(n_nails, shape, n_clicks)

    children.append(new_layer)

    return children, n_clicks, 'tab-'+str(len(children))

def new_layer_tab(n_nails,shape,n_clicks):
    n_sides = shape.n_sides
    shape_methods = shape.shape_methods

    checklistOptions    = [{'label': str(i+1), 'value': i} for i in range(n_sides)]
    checklistValues     = [i for i in range(n_sides)]

    layerDropdownShapes = [{'label': method, 'value': method} for method in shape_methods]
    label='Layer ' + str(n_clicks)

    max_slider = n_nails

    return dcc.Tab(label=label,
        children=[
            html.Div([
                html.Div([
                        dcc.Dropdown(
                            id={
                                'type': 'layer-dropdown',
                                'index': n_clicks
                            },
                            options=layerDropdownShapes,
                            multi=False,
                            value=list(shape_methods.keys())[0]
                        ),
                        html.Br(),
                        html.P('Select / Deselect sections', style={'color' : '#111111'}),
                        dcc.Checklist(
                            id={
                                'type': 'section-selector',
                                'index': n_clicks
                            },
                            options=checklistOptions,
                            value=checklistValues,
                            style={'display': 'inline-block'}
                        )],style={'width': '20%', 'display': 'inline-block', 'color' : '#111111'}
                ),
                html.Div(
                    [daq.ColorPicker(
                        id={
                            'type': 'color-picker',
                            'index': n_clicks
                        },
                        label='Layer Color',
                        value=dict(hex='#FFA200'),
                        size=200
                    )],style={'width': '40%', 'display': 'inline-block'}
                ),
                html.Div([
                    html.P('Shift the starting nail', style={'color' : '#111111'}),
                    dcc.Slider(
                        id={
                            'type': 'nshift-slider',
                            'index': n_clicks
                        },
                        min=-max_slider,
                        max=max_slider,
                        step=1,
                        value=0,
                        marks={i: str(i) for i in range(-max_slider,max_slider+1,max([int(max_slider/10),1]))}
                    ),
                    html.P('Trim off beginning & end of string', style={'color' : '#111111'}),
                    dcc.RangeSlider(
                        id={
                            'type': 'trim-slider',
                            'index': n_clicks
                        },
                        min=0,
                        max=max_slider,
                        step=1,
                        value=[0,max_slider],
                        marks={i: str(i) for i in range(0,max_slider+1)}
                    )
                    # html.P('trim off end string', style={'color' : '#111111'}),
                    # dcc.Slider(
                    #     id={
                    #         'type': 'trim-end-slider',
                    #         'index': n_clicks
                    #     },
                    #     min=0,
                    #     max=max_slider,
                    #     step=1,
                    #     value=0,
                    #     marks={i: str(i) for i in range(max_slider+1)}
                    # )
                    ],style={'width': '40%', 'display': 'inline-block'})
                ]),
                html.Br()
        ], className="tab-content" #style={'justifyContent': 'center','display': 'flex'}
    )

# Change stringart parameters
@app.callback(
    Output(component_id='stringart_plot', component_property='figure'),

    [Input({'type': 'layer-dropdown', 'index': ALL}, 'value'),
    Input({'type': 'color-picker', 'index': ALL}, 'value'),
    Input({'type': 'nshift-slider', 'index': ALL}, 'value'),
    Input({'type': 'trim-slider', 'index': ALL}, 'value'),
    # Input({'type': 'trim-end-slider', 'index': ALL}, 'value'),
    Input({'type': 'section-selector', 'index': ALL}, 'value'),
    Input(component_id='in_width', component_property='value'),
    Input(component_id='in_nails', component_property='value'),
    Input(component_id='in_thick', component_property='value')
    ],

    State(component_id='slct_shape', component_property='value')
)

def update_plot(layer_dropdown, color_picker, nshift_slider, trim_slider, section_selector, in_width, in_nails, in_thick, slct_shape):
    shape = get_shape(slct_shape,in_width,in_nails,in_thick)
    fig = shape.plotFrame()

    for (i,value) in enumerate(layer_dropdown): 
        style_dict = {
			'color' 		: color_picker[i]["hex"],
			'Nshift' 		: nshift_slider[i],
			'trimStart' 	: trim_slider[i][0],
			'trimEnd' 		: in_nails-trim_slider[i][1],
			'parts' 		: section_selector[i]
		}
        fig = getattr(shape, layer_dropdown[i])(fig,style_dict)

    fig["layout"]= go.Layout(margin=dict(t=10,l=10,r=10,b=10), height=800, width=800, 
        paper_bgcolor='rgba(0,0,0,0)', font_color="#D5D5D5",font_size=20
    )
    fig.update_xaxes(title_text="Width (mm)")
    fig.update_yaxes(title_text="Height (mm)")

    return fig

def get_shape(slct_shape,in_width,in_nails,in_thick):
    if slct_shape == 'T':
        shape = Triangle(in_width,in_nails,in_thick)
    elif slct_shape == 'S':
        shape = Square(in_width,in_nails,in_thick)
    elif slct_shape == 'C':
        shape = Triangle(in_width,in_nails,in_thick)
    else:
        shape = None
    return shape

# --------------------------------------------------------------------------
if __name__ == "__main__":
    app.run_server(debug=True)