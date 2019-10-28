# Test prog stringart triangle

import matplotlib.pyplot as plt
import numpy as np
import math

blat = 38

breedte = 500-blat #mm
Nspijkers = 20 #mm

afstand = breedte/Nspijkers

helft = breedte/2

x1 = np.linspace(0,helft,Nspijkers) # rechts
y1 = np.zeros(Nspijkers)
x2 = np.zeros(Nspijkers) # boven
y2 = np.linspace(0,helft,Nspijkers)
x3 = np.linspace(0,-helft,Nspijkers) # links
y3 = np.zeros(Nspijkers)
x4 = np.zeros(Nspijkers) # onder
y4 = np.linspace(0,-helft,Nspijkers)

Nshift = 0
Nshift2 = 0

layer2_Nshift = 5
layer2_Nshift2 = 10

layer3_Nshift = 10
layer3_Nshift2 = 0

straight_Nshift = 0
straight_Nshift2 = 10

hoek1X = []
hoek1Y = []
hoek2X = []
hoek2Y = []
hoek3X = []
hoek3Y = []
hoek4X = []
hoek4Y = []
for i in range(0,Nspijkers-Nshift2-Nshift):
	hoek1X.append(x1[i+Nshift2])
 	hoek1X.append(x2[Nspijkers-1-i-Nshift])
	hoek1Y.append(y1[i+Nshift2])
	hoek1Y.append(y2[Nspijkers-1-i-Nshift])

	hoek2X.append(x2[i+Nshift2])
 	hoek2X.append(x3[Nspijkers-1-i-Nshift])
	hoek2Y.append(y2[i+Nshift2])
	hoek2Y.append(y3[Nspijkers-1-i-Nshift])

	hoek3X.append(x3[i+Nshift2])
 	hoek3X.append(x4[Nspijkers-1-i-Nshift])
	hoek3Y.append(y3[i+Nshift2])
	hoek3Y.append(y4[Nspijkers-1-i-Nshift])

	hoek4X.append(x4[i+Nshift2])
 	hoek4X.append(x1[Nspijkers-1-i-Nshift])
	hoek4Y.append(y4[i+Nshift2])
	hoek4Y.append(y1[Nspijkers-1-i-Nshift])

layer2_hoek1X = []
layer2_hoek1Y = []
layer2_hoek2X = []
layer2_hoek2Y = []
layer2_hoek3X = []
layer2_hoek3Y = []
layer2_hoek4X = []
layer2_hoek4Y = []
for i in range(0,Nspijkers-layer2_Nshift2-layer2_Nshift):
	layer2_hoek1X.append(x1[i+layer2_Nshift2])
 	layer2_hoek1X.append(x2[Nspijkers-1-i-layer2_Nshift])
	layer2_hoek1Y.append(y1[i+layer2_Nshift2])
	layer2_hoek1Y.append(y2[Nspijkers-1-i-layer2_Nshift])

	layer2_hoek2X.append(x2[i+layer2_Nshift2])
 	layer2_hoek2X.append(x3[Nspijkers-1-i-layer2_Nshift])
	layer2_hoek2Y.append(y2[i+layer2_Nshift2])
	layer2_hoek2Y.append(y3[Nspijkers-1-i-layer2_Nshift])

	layer2_hoek3X.append(x3[i+layer2_Nshift2])
 	layer2_hoek3X.append(x4[Nspijkers-1-i-layer2_Nshift])
	layer2_hoek3Y.append(y3[i+layer2_Nshift2])
	layer2_hoek3Y.append(y4[Nspijkers-1-i-layer2_Nshift])

	layer2_hoek4X.append(x4[i+layer2_Nshift2])
 	layer2_hoek4X.append(x1[Nspijkers-1-i-layer2_Nshift])
	layer2_hoek4Y.append(y4[i+layer2_Nshift2])
	layer2_hoek4Y.append(y1[Nspijkers-1-i-layer2_Nshift])

layer3_hoek1X = []
layer3_hoek1Y = []
layer3_hoek2X = []
layer3_hoek2Y = []
layer3_hoek3X = []
layer3_hoek3Y = []
layer3_hoek4X = []
layer3_hoek4Y = []
for i in range(0,Nspijkers-layer3_Nshift2-layer3_Nshift):
	layer3_hoek1X.append(x1[i+layer3_Nshift2])
 	layer3_hoek1X.append(x2[Nspijkers-1-i-layer3_Nshift])
	layer3_hoek1Y.append(y1[i+layer3_Nshift2])
	layer3_hoek1Y.append(y2[Nspijkers-1-i-layer3_Nshift])

	layer3_hoek2X.append(x2[i+layer3_Nshift2])
 	layer3_hoek2X.append(x3[Nspijkers-1-i-layer3_Nshift])
	layer3_hoek2Y.append(y2[i+layer3_Nshift2])
	layer3_hoek2Y.append(y3[Nspijkers-1-i-layer3_Nshift])

	layer3_hoek3X.append(x3[i+layer3_Nshift2])
 	layer3_hoek3X.append(x4[Nspijkers-1-i-layer3_Nshift])
	layer3_hoek3Y.append(y3[i+layer3_Nshift2])
	layer3_hoek3Y.append(y4[Nspijkers-1-i-layer3_Nshift])

	layer3_hoek4X.append(x4[i+layer3_Nshift2])
 	layer3_hoek4X.append(x1[Nspijkers-1-i-layer3_Nshift])
	layer3_hoek4Y.append(y4[i+layer3_Nshift2])
	layer3_hoek4Y.append(y1[Nspijkers-1-i-layer3_Nshift])


straight_hoek1X = []
straight_hoek1Y = []
straight_hoek2X = []
straight_hoek2Y = []
straight_hoek3X = []
straight_hoek3Y = []
straight_hoek4X = []
straight_hoek4Y = []
for i in range(straight_Nshift,Nspijkers-straight_Nshift2):
	straight_hoek1X.append(x1[i])
 	straight_hoek1X.append(x2[i])
	straight_hoek1Y.append(y1[i])
	straight_hoek1Y.append(y2[i])

	straight_hoek2X.append(x2[i])
 	straight_hoek2X.append(x3[i])
	straight_hoek2Y.append(y2[i])
	straight_hoek2Y.append(y3[i])

	straight_hoek3X.append(x3[i])
 	straight_hoek3X.append(x4[i])
	straight_hoek3Y.append(y3[i])
	straight_hoek3Y.append(y4[i])

	straight_hoek4X.append(x4[i])
 	straight_hoek4X.append(x1[i])
	straight_hoek4Y.append(y4[i])
	straight_hoek4Y.append(y1[i])

fig = plt.figure()
#contour
plt.plot(x1,y1,'ko-',linewidth=1.0)
plt.plot(x2,y2,'ko-',linewidth=1.0)
plt.plot(x3,y3,'ko-',linewidth=1.0)
plt.plot(x4,y4,'ko-',linewidth=1.0)

# outer contour
plt.plot(x1+blat/2,y1+blat/2,'k-',linewidth=1.0)
plt.plot(x1+blat/2,y1-blat/2,'k-',linewidth=1.0)
plt.plot([x1[-1]+blat/2,x1[-1]+blat/2],[y1[-1]+blat/2,y1[-1]-blat/2],'k-')
plt.plot(x2+blat/2,y2+blat/2,'k-',linewidth=1.0)
plt.plot(x2-blat/2,y2+blat/2,'k-',linewidth=1.0)
plt.plot([x2[-1]-blat/2,x2[-1]+blat/2],[y2[-1]+blat/2,y2[-1]+blat/2],'k-')
plt.plot(x3-blat/2,y3+blat/2,'k-',linewidth=1.0)
plt.plot(x3-blat/2,y3-blat/2,'k-',linewidth=1.0)
plt.plot([x3[-1]-blat/2,x3[-1]-blat/2],[y3[-1]+blat/2,y3[-1]-blat/2],'k-')
plt.plot(x4-blat/2,y4-blat/2,'k-',linewidth=1.0)
plt.plot(x4+blat/2,y4-blat/2,'k-',linewidth=1.0)
plt.plot([x4[-1]+blat/2,x4[-1]-blat/2],[y4[-1]-blat/2,y4[-1]-blat/2],'k-')


plt.axis([-helft-afstand,helft+afstand,-helft-afstand,helft+afstand])
plt.gca().set_aspect('equal', adjustable='box') # make axes equal

#plot patterns
plt.plot(hoek1X,hoek1Y,'r-',linewidth=1.0)
plt.plot(hoek2X,hoek2Y,'r-',linewidth=1.0)
plt.plot(hoek3X,hoek3Y,'r-',linewidth=1.0)
plt.plot(hoek4X,hoek4Y,'r-',linewidth=1.0)

plt.plot(layer2_hoek1X,layer2_hoek1Y,'b-',linewidth=1.0)
plt.plot(layer2_hoek2X,layer2_hoek2Y,'b-',linewidth=1.0)
plt.plot(layer2_hoek3X,layer2_hoek3Y,'b-',linewidth=1.0)
plt.plot(layer2_hoek4X,layer2_hoek4Y,'b-',linewidth=1.0)

plt.plot(layer3_hoek1X,layer3_hoek1Y,'y-',linewidth=1.0)
plt.plot(layer3_hoek2X,layer3_hoek2Y,'y-',linewidth=1.0)
plt.plot(layer3_hoek3X,layer3_hoek3Y,'y-',linewidth=1.0)
plt.plot(layer3_hoek4X,layer3_hoek4Y,'y-',linewidth=1.0)

# plt.plot(straight_hoek1X,straight_hoek1Y,'y-')
# plt.plot(straight_hoek2X,straight_hoek2Y,'y-')
# plt.plot(straight_hoek3X,straight_hoek3Y,'y-')
# plt.plot(straight_hoek4X,straight_hoek4Y,'y-')

plt.show()
# fig.savefig("plot.png")

# COLORS
# blue		b	[0,0,1]
# black		k	[0,0,0]
# red		r	[1,0,0]
# green		g	[0,1,0]
# yellow	y	[1,1,0]
# cyan		c	[0,1,1]
# magenta	m	[1,0,1]
# white		w	[1,1,1]

# Calculate distances
distanceHoek = 0
distanceHoek_layer2 = 0
distanceHoek_layer3 = 0
distanceHoek_straight = 0

for count in range(1,len(hoek1X)):
	distanceHoek += math.sqrt(math.pow(hoek1X[count]-hoek1X[count-1],2) + math.pow(hoek1Y[count]-hoek1Y[count-1],2))
	
for count in range(1,len(layer2_hoek1X)):
	distanceHoek_layer2 += math.sqrt(math.pow(layer2_hoek1X[count]-layer2_hoek1X[count-1],2) + math.pow(layer2_hoek1Y[count]-layer2_hoek1Y[count-1],2))

for count in range(1,len(layer3_hoek1X)):
	distanceHoek_layer3 += math.sqrt(math.pow(layer3_hoek1X[count]-layer3_hoek1X[count-1],2) + math.pow(layer3_hoek1Y[count]-layer3_hoek1Y[count-1],2))

# for count in range(1,len(straight_hoek1X)):
# 	distanceHoek_straight += math.sqrt(math.pow(straight_hoek1X[count]-straight_hoek1X[count-1],2) + math.pow(straight_hoek1Y[count]-straight_hoek1Y[count-1],2))

print ((distanceHoek+distanceHoek_layer2+distanceHoek_layer3)*4)