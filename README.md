
# StringArtMaker
Make Stringart designs by modifying this code

not exactly user-friendly but gives nice basis of ideas to start with

Just mess around with what to plot, along with the sizes, nailcount, colors and the Nshift values to get differ different shapes.

### Make GIFs
Turn string of pictures into gif from command line:

```convert -delay 20 -loop 0 `ls -v|grep png` CrossA.gif```

Remove pngs afterwards:

```rm `ls -v|grep png```

## Some examples
### Crosses

```python
# CrossA
c1 = Curve(500,13,38,-4,4,0,'r')
c2 = Curve(500,13,38,-4,0,5,'b')
c3 = Curve(500,13,38,5,0,0,'y')```

