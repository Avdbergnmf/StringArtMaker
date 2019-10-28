# Test prog stringart square

import matplotlib.pyplot as plt
import numpy as np
import math

blat = 30

breedte = 450-blat #mm
Nspijkers = 42

afstand = breedte/Nspijkers

x1 = np.linspace(0,breedte,Nspijkers) #onder
y1 = np.linspace(0,breedte,Nspijkers) #rechts
x2 = np.linspace(breedte,0,Nspijkers) #boven
y2 = np.linspace(breedte,0,Nspijkers) #links

cross1X = []
cross1Y = []
cross2X = []
cross2Y = []
for i in range(len(x1)):
	cross1X.append(x1[i])
	cross1X.append(x2[i])
	cross1Y.append(0)
	cross1Y.append(breedte)

	cross2Y.append(y1[i])
	cross2Y.append(y2[i])
	cross2X.append(0)
	cross2X.append(breedte)

hoek1X = []
hoek1Y = []
hoek2X = []
hoek2Y = []
hoek3X = []
hoek3Y = []
hoek4X = []
hoek4Y = []
for i in range(len(x1)):
	hoek1X.append(x1[i])
 	hoek1X.append(breedte)
	hoek1Y.append(0)
	hoek1Y.append(y1[i])

	hoek2X.append(breedte)
	hoek2X.append(x2[i])
	hoek2Y.append(y1[i])
	hoek2Y.append(breedte)

	hoek3X.append(x2[i])
 	hoek3X.append(0)
	hoek3Y.append(breedte)
	hoek3Y.append(y2[i])

	hoek4X.append(0)
	hoek4X.append(x1[i])
	hoek4Y.append(y2[i])
	hoek4Y.append(0)

recht1X = []
recht1Y = []
recht2X = []
recht2Y = []
recht3X = []
recht3Y = []
recht4X = []
recht4Y = []
for i in range(len(x1)):
	recht1X.append(x1[i])
 	recht1X.append(breedte)
	recht1Y.append(0)
	recht1Y.append(y2[i])

	recht2X.append(breedte)
	recht2X.append(x2[i])
	recht2Y.append(y2[i])
	recht2Y.append(breedte)

	recht3X.append(x2[i])
 	recht3X.append(0)
	recht3Y.append(breedte)
	recht3Y.append(y1[i])

	recht4X.append(0)
	recht4X.append(x2[i])
	recht4Y.append(y2[i])
	recht4Y.append(0)
	

fig = plt.figure()
#contour
plt.plot(x1,np.zeros(len(x1)),'ko')
plt.plot(x2,np.ones(len(x1))*breedte,'ko')
plt.plot(np.zeros(len(y1)),y1,'ko')
plt.plot(np.ones(len(y1))*breedte,y2,'ko')


# outer contour
plt.plot([-blat/2,breedte+blat/2,breedte+blat/2,-blat/2,-blat/2],[-blat/2,-blat/2,breedte+blat/2,breedte+blat/2,-blat/2],'k',linewidth=2.0,)
plt.plot([blat/2,breedte-blat/2,breedte-blat/2,blat/2,blat/2],[blat/2,blat/2,breedte-blat/2,breedte-blat/2,blat/2],'k',linewidth=2.0,)

plt.axis([-blat,breedte+blat,-blat,breedte+blat])
plt.gca().set_aspect('equal', adjustable='box') # make axes equal

#plot patterns
plt.plot(hoek1X,hoek1Y,'r-')
plt.plot(hoek2X,hoek2Y,'b-')
plt.plot(hoek3X,hoek3Y,'r-')
plt.plot(hoek4X,hoek4Y,'b-')

# plt.plot(recht1X,recht1Y,'c-')
# plt.plot(recht2X,recht2Y,'b-')
# plt.plot(recht3X,recht3Y,'c-')
# plt.plot(recht4X,recht4Y,'b-')

plt.plot(cross1X,cross1Y,'m-')
# plt.plot(cross2X,cross2Y,'b-')

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
distanceKruis = 0
distanceHoek = 0
distanceRecht = 0

for count in range(1,len(hoek1X)):
	distanceHoek += math.sqrt(math.pow(hoek1X[count]-hoek1X[count-1],2) + math.pow(hoek1Y[count]-hoek1Y[count-1],2))
	
for count in range(1,len(cross1X)):
	distanceKruis += math.sqrt(math.pow(cross1X[count]-cross1X[count-1],2) + math.pow(cross1Y[count]-cross1Y[count-1],2))

for count in range(1,len(recht1X)):
	distanceRecht += math.sqrt(math.pow(recht1X[count]-recht1X[count-1],2) + math.pow(recht1Y[count]-recht1Y[count-1],2))

print distanceKruis
print distanceHoek
print distanceRecht

print (distanceHoek*4+distanceKruis*2)