# Test prog stringart triangle

import matplotlib.pyplot as plt
import numpy as np
import math

class Triangle:
	def __init__(self,width,nails,thick):
		self.width=width
		self.nails=nails
		self.thick=thick

		helft = breedte/2
		hoogte = math.sqrt(3)*helft

		self.x1 = np.linspace(0,breedte,nails)
		self.y1 = np.zeros(nails)
		self.x2 = np.linspace(breedte,helft,nails)
		self.y2 = np.linspace(0,hoogte,nails)
		self.x3 = np.linspace(helft,0,nails)
		self.y3 = np.linspace(hoogte,0,nails)

		thickTop = np.sqrt(3)*blat/2
		thickDiag = (blat/2)/np.tan(np.pi/6)

		self.xcontour1 = [-thickDiag,breedte+blat,helft,-thickDiag]
		self.ycontour1 = [-thickDiag/2,-thickDiag/2,hoogte+thickTop,-thickDiag/2]

		self.xcontour2 = [thickDiag,breedte-thickDiag,helft,thickDiag]
		self.ycontour2 = [thickDiag/2,thickDiag/2,hoogte-thickTop,thickDiag/2]
		
	def plotSquare(self):
		plt.plot(self.x1,self.y1,'ko',linewidth=1)
		plt.plot(self.x2,self.y2,'ko',linewidth=1)
		plt.plot(self.x3,self.y3,'ko',linewidth=1)
		
		# outer contour
		plt.plot(self.xcontour1,self.ycontour1,'k')
		plt.plot(self.xcontour2,self.ycontour2,'k')

		plt.axis([-self.thick/2,width+self.thick/2,-self.thick/2,self.width+self.thick/2])
		plt.gca().set_aspect('equal', adjustable='box') # make axes equal


hoek1X = []
hoek1Y = []
hoek2X = []
hoek2Y = []
hoek3X = []
hoek3Y = []
for i in range(0,Nspijkers-Nshift):
	hoek1X.append(x1[i])
 	hoek1X.append(x2[i+Nshift])
	hoek1Y.append(y1[i])
	hoek1Y.append(y2[i+Nshift])

	hoek2X.append(x2[i])
 	hoek2X.append(x3[i+Nshift])
	hoek2Y.append(y2[i])
	hoek2Y.append(y3[i+Nshift])

	hoek3X.append(x3[i])
 	hoek3X.append(x1[i+Nshift])
	hoek3Y.append(y3[i])
	hoek3Y.append(y1[i+Nshift])

extra_hoek1X = []
extra_hoek1Y = []
extra_hoek2X = []
extra_hoek2Y = []
extra_hoek3X = []
extra_hoek3Y = []
for i in range(0,Nspijkers-extra_Nshift):
	extra_hoek1X.append(x1[i])
 	extra_hoek1X.append(x2[i+extra_Nshift])
	extra_hoek1Y.append(y1[i])
	extra_hoek1Y.append(y2[i+extra_Nshift])

	extra_hoek2X.append(x2[i])
 	extra_hoek2X.append(x3[i+extra_Nshift])
	extra_hoek2Y.append(y2[i])
	extra_hoek2Y.append(y3[i+extra_Nshift])

	extra_hoek3X.append(x3[i])
 	extra_hoek3X.append(x1[i+extra_Nshift])
	extra_hoek3Y.append(y3[i])
	extra_hoek3Y.append(y1[i+extra_Nshift])

fig = plt.figure()
#contour
plt.plot(x1,y1,'ko')
plt.plot(x2,y2,'ko')
plt.plot(x3,y3,'ko')

# outer contour



plt.axis([-blat,breedte+blat,-blat,hoogte+blat])
plt.ylabel("hoogte [mm]")
plt.xlabel("breedte [mm]")
plt.gca().set_aspect('equal', adjustable='box') # make axes equal

#plot patterns
plt.plot(extra_hoek1X,extra_hoek1Y,'y-')
plt.plot(extra_hoek2X,extra_hoek2Y,'y-')
plt.plot(extra_hoek3X,extra_hoek3Y,'y-')

plt.plot(hoek1X,hoek1Y,'r-')
plt.plot(hoek2X,hoek2Y,'r-')
plt.plot(hoek3X,hoek3Y,'r-')



plt.show()
fig.savefig("triangleC_6.png")


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
distanceExtra_Hoek = 0

for count in range(1,len(hoek1X)):
	distanceHoek += math.sqrt(math.pow(hoek1X[count]-hoek1X[count-1],2) + math.pow(hoek1Y[count]-hoek1Y[count-1],2))
	
for count in range(1,len(extra_hoek1Y)):
	distanceExtra_Hoek += math.sqrt(math.pow(extra_hoek1X[count]-extra_hoek1X[count-1],2) + math.pow(extra_hoek1Y[count]-extra_hoek1Y[count-1],2))

print("Lengte String: " + str(round((distanceHoek*3+distanceExtra_Hoek*3)/1000,2)) + "m")
print("Aantal Spijkers: " + str(Nspijkers*3-3))