import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import math

class StringArtShape:
	def __init__(self,width,n_nails,thick):
		self.StringLength = 0 # var to hold the total length of the string

		self.width  = width
		self.height = width
		self.thick  = thick # Frame Thickness

		self.n_dim = 2
		self.n_nails = n_nails # Number of nails per side

		# Placeholder arrays
		self.n_sides = 3
		self.nails = np.zeros((self.n_dim,n_nails,self.n_sides))
		self.inner_contour = []
		self.outer_contour = []

	def plotFrame(self):
		# Styling parameters
		padding = self.thick*1.5
		nailMarkerStyle = dict(color='#ffffff', size=5, line=dict(color="#000000",width=2))
		contourLineStyle = dict(color='#000000', width=1)

		# Create Plotly Graph Object
		fig = go.Figure(
			layout_xaxis_range=[-padding,self.width+padding],
			layout_yaxis_range=[-padding,self.height+padding]
		)

		# Plot markers
		for i in range(self.n_sides):
			fig = self.add_markers(fig, self.nails[:,:,i], nailMarkerStyle)
		
		# Plot contour
		fig = self.add_lines(fig, self.inner_contour,contourLineStyle)
		fig = self.add_lines(fig, self.outer_contour,contourLineStyle)
		return fig

	def layer_shape(self,fig,style_dict,shape_dict):
		# Some fancy math to determine the stringart layer shape
		plotLineStyle = dict(color=style_dict['color'], width=1)

		plotRange = self.getPlotRange(style_dict['Nshift'],style_dict['trimStart'],style_dict['trimEnd'])

		p = shape_dict['layer_pattern']
		lines_per_step = len(p)
		n_lines = len(plotRange) * lines_per_step

		data = np.zeros((self.n_dim,n_lines,self.n_sides))

		# Some effects require a multiplier on the nail iterator 
		if 'nail_multiplier' in shape_dict:
			nail_multiplier = shape_dict['nail_multiplier']
		else:
			nail_multiplier = np.ones((lines_per_step,self.n_dim))

		# Check the side_shift array
		if len(shape_dict['side_shift'])==lines_per_step:
			side_shift = shape_dict['side_shift']
		else:
			print("ERROR: Make sure the side_shift array is has (lines_per_step) elements (usually starting with a 0).")

		for part in style_dict['parts']:
			for j in range(lines_per_step):
				side = (part+side_shift[j]) % self.n_sides # take modulus so that when we go too far, it loops back to the start
				for i in plotRange:
					x_index = int(nail_multiplier[j][0]) * i + p[j][0]
					y_index = int(nail_multiplier[j][1]) * i + p[j][1]
					
					if x_index in range(len(self.nails[0,:,side])) and y_index in range(len(self.nails[1,:,side])):
						data[:, lines_per_step*i+j,	part] = [self.nails[0, x_index, side],	self.nails[1, y_index, side]]

				#self.StringLength += self.string_length(data[:, 2*i, part], data[:, 2*i+1, part])
			fig = self.add_lines(fig,data[:, :, part],plotLineStyle)

		return fig

	def string_length(self,A,B): # return string length from point A to B
		return math.sqrt(math.pow(A[0]-B[0],2) + math.pow(A[1]-B[1],2))

	def add_markers(self,fig,data,style):
		fig.add_trace(go.Scatter(x=data[0,:], y=data[1,:], showlegend=False, mode='markers', marker=style))
		return fig

	def add_lines(self,fig,data,style):
		fig.add_trace(go.Scatter(x=data[0,:], y=data[1,:], showlegend=False, mode='lines', line=style))
		return fig

	def getPlotRange(self,Nshift,trimStart,trimEnd):
		if(Nshift<0):
			Nstart = -Nshift
			Nend = 0
		else:
			Nstart = 0
			Nend = +Nshift
		plotRange = range(Nstart+trimStart,self.n_nails-Nend-trimEnd)
		return plotRange

	def getnParts(self,n_corners): # How many distinct parts can we plot? based on the number of corners
		return math.floor(n_corners/2) + n_corners % 2

class Square(StringArtShape):
	def __init__(self,width,n_nails,thick):
		super().__init__(width,n_nails,thick)
		half = width/2

		self.shape_methods = {
			"cross": self.cross,
			"zigzag": self.zigzag,
			"curve": self.curve
		}

		# Define corners
		nail_corners = np.array([
			[-half, -half], # bottom left
			[half,  -half],  # bottom right
			[half,   half],  # top right
			[-half,  half],  # top left
			[-half, -half],  # top left
		])

		n_corners = len(nail_corners)
		self.n_sides = n_corners-1
		self.n_parts = self.getnParts(n_corners)
		self.nails = np.zeros((self.n_dim,n_nails,self.n_sides))
		
		# Create nails
		for i in range(self.n_sides):
			self.nails[:,:,i] = [np.linspace(nail_corners[i,0],nail_corners[i+1,0],n_nails), 	
								 np.linspace(nail_corners[i,1],nail_corners[i+1,1],n_nails)]

		# Create contour
		dist_pos = half+self.thick/2
		dist_neg = half-self.thick/2
		self.inner_contour = np.array([[-dist_pos,dist_pos,dist_pos,-dist_pos,-dist_pos],[-dist_pos,-dist_pos,dist_pos,dist_pos,-dist_pos]])
		self.outer_contour = np.array([[-dist_neg,dist_neg,dist_neg,-dist_neg,-dist_neg],[-dist_neg,-dist_neg,dist_neg,dist_neg,-dist_neg]])
	
	def cross(self,fig,style_dict):
		Nshift = style_dict['Nshift']
		layer_pattern = np.array([
			[Nshift,Nshift],
			[Nshift,Nshift]
		])
		shape_dict = {
			'layer_pattern' : layer_pattern,
			'side_shift' 	: [0,2]
		}

		fig = self.layer_shape(fig,style_dict,shape_dict)
		return fig

	def zigzag(self,fig,style_dict):
		Nshift = style_dict['Nshift']
		layer_pattern = np.array([
			[Nshift,Nshift],
			[Nshift,Nshift]
		])
		shape_dict = {
			'layer_pattern' : layer_pattern,
			'side_shift' 	: [0,2]
		}

		fig = self.layer_shape(fig,style_dict,shape_dict)
		return fig

	def curve(self,fig,style_dict):
		Nshift = style_dict['Nshift']
		layer_pattern = np.array([
			[0,0],
			[Nshift,Nshift]
		])
		shape_dict = {
			'layer_pattern' : layer_pattern,
			'side_shift' 	: [0,1]
		}

		fig = self.layer_shape(fig,style_dict,shape_dict)
		return fig

class Triangle(StringArtShape):
	def __init__(self,width,n_nails,thick):
		super().__init__(width,n_nails,thick)
		self.shape_methods = {
			"straight": self.straight,
			"curve": self.curve
		}

		half = width/2
		self.height = math.sqrt(3)*half

		self.n_sides = 3 	# 3 sides for a triangle
		self.nails = np.zeros((self.n_dim,n_nails,self.n_sides))

		# Create nails positions
		self.nails[:,:,0] = [np.linspace(0,width,n_nails), 		np.zeros(n_nails)]
		self.nails[:,:,1] = [np.linspace(width,half,n_nails), 	np.linspace(0,self.height,n_nails)]
		self.nails[:,:,2] = [np.linspace(half,0,n_nails), 		np.linspace(self.height,0,n_nails)]
		
		# Create contour plot
		thickTop = np.sqrt(3)*thick/2
		thickDiag = (thick/2)/np.tan(np.pi/6)
		self.inner_contour = np.array([[-thickDiag,width+thick,half,-thickDiag], [-thickDiag/2,-thickDiag/2,self.height+thickTop,-thickDiag/2]])
		self.outer_contour = np.array([[thickDiag,width-thickDiag,half,thickDiag], [thickDiag/2,thickDiag/2,self.height-thickTop,thickDiag/2]])

	def curve(self,fig,style_dict):
		Nshift = style_dict['Nshift']
		layer_pattern = np.array([
			[0,0],
			[Nshift,Nshift]
		])

		shape_dict = {
			'layer_pattern' : layer_pattern,
			'side_shift' 	: [0,1]
		}

		fig = self.layer_shape(fig,style_dict,shape_dict)
		return fig

	def straight(self,fig,style_dict):
		Nshift = style_dict['Nshift']
		
		layer_pattern = np.array([
			[0,0],
			[self.n_nails-1-Nshift,self.n_nails-1-Nshift],
			[self.n_nails-2-Nshift,self.n_nails-2-Nshift]
		])
		nail_multiplier = np.array([
			[ 1, 1],
			[-1,-1],
			[-1,-1]
		])
		shape_dict = {
			'layer_pattern'  : layer_pattern,
			'side_shift' 	 : [0,1,1],
			'nail_multiplier': nail_multiplier
		}

		fig = self.layer_shape(fig,style_dict,shape_dict)
		return fig