# Test prog stringart square

import matplotlib.pyplot as plt
import numpy as np
import math

class Square:
	def __init__(self,width,nails,thick):
		self.width=width
		self.nails=nails
		self.thick=thick
		
		nailwidth = width-thick
		half = nailwidth/2
		
		self.x1 = np.linspace(-half,half,nails) # onder
		self.y1 = np.ones(nails)*-half
		self.x2 = np.ones(nails)*half# rechts
		self.y2 = np.linspace(-half,half,nails)
		self.x3 = np.linspace(half,-half,nails) # boven
		self.y3 = np.ones(nails)*half
		self.x4 = np.ones(nails)*-half # links
		self.y4 = np.linspace(half,-half,nails)
		
		self.xcontour1 = [-half-thick/2,half+thick/2,half+thick/2,-half-thick/2,-half-thick/2]
		self.ycontour1 = [-half-thick/2,-half-thick/2,half+thick/2,half+thick/2,-half-thick/2]
		self.xcontour2 = [-half+thick/2,half-thick/2,half-thick/2,-half+thick/2,-half+thick/2]
		self.ycontour2 = [-half+thick/2,-half+thick/2,half-thick/2,half-thick/2,-half+thick/2]

	def plotSquare(self):
		plt.plot(self.x1,self.y1,'ko',linewidth=1)
		plt.plot(self.x2,self.y2,'ko',linewidth=1)
		plt.plot(self.x3,self.y3,'ko',linewidth=1)
		plt.plot(self.x4,self.y4,'ko',linewidth=1)
		
		# outer contour
		plt.plot(self.xcontour1,self.ycontour1,'k')
		plt.plot(self.xcontour2,self.ycontour2,'k')

		plt.axis([-self.width/2-self.thick,self.width/2+self.thick,-self.width/2-self.thick,self.width/2+self.thick])
		plt.gca().set_aspect('equal', adjustable='box') # make axes equal

class Xpatt(Square):
	def __init__(self,width,nails,thick,Nshift=0,trimStart=0,trimEnd=0):
		super().__init__(width,nails,thick)
		self.Xpatt1X = []
		self.Xpatt1Y = []
		self.Xpatt2X = []
		self.Xpatt2Y = []

		if(Nshift<0):
			Nstart = -Nshift
			Nend = 0
		else:
			Nstart = 0
			Nend = +Nshift

		for i in range(Nstart+trimStart,self.nails-Nend-trimEnd):
			self.Xpatt1X.append(self.x1[i+Nshift])
			self.Xpatt1Y.append(self.y1[i+Nshift])
			self.Xpatt1X.append(self.x3[i+Nshift])
			self.Xpatt1Y.append(self.y3[i+Nshift])

		for i in range(Nstart+trimStart,self.nails-Nend-trimEnd):
			self.Xpatt2X.append(self.x2[i+Nshift])
			self.Xpatt2Y.append(self.y2[i+Nshift])
			self.Xpatt2X.append(self.x4[i+Nshift])
			self.Xpatt2Y.append(self.y4[i+Nshift])

	def plot(self,color='b',makePic=0,tutName="Square",makeGif=0):
		if(makeGif):
			for i in range(1,len(self.Xpatt1X)+1):
				plt.plot(self.Xpatt1X[0:i],self.Xpatt1Y[0:i],color,linewidth=1)
				plt.plot(self.Xpatt2X[0:i],self.Xpatt2Y[0:i],color,linewidth=1)
				fig.savefig(tutName+str(i)+".png")
		else:
			plt.plot(self.Xpatt1X,self.Xpatt1Y,color,linewidth=1)
			plt.plot(self.Xpatt2X,self.Xpatt2Y,color,linewidth=1)
			if(makePic):
				fig.savefig(tutName+".png")
				
def Curve(Square):
	def __init__(self,width,nails,thick,Nshift=0,trimStart=0,trimEnd=0):
		super().__init__(self,width,nails,thick)
		


Xp1 = Xpatt(500,22,30,17,0,0)
Xp2 = Xpatt(500,22,30,-17,0,0)

fig = plt.figure()

Xp1.plotSquare()
Xp1.plot('b',0,"cross",0)
Xp2.plot('b',1,"cross",0)

plt.show()







# hoek1X = []
# hoek1Y = []
# hoek2X = []
# hoek2Y = []
# hoek3X = []
# hoek3Y = []
# hoek4X = []
# hoek4Y = []
# for i in range(Nshift,len(x1)-Nshift2):
# 	hoek1X.append(x1[i])
#  	hoek1X.append(breedte)
# 	hoek1Y.append(0)
# 	hoek1Y.append(y1[i+Nshift2])

# 	hoek2X.append(breedte)
# 	hoek2X.append(x2[i])
# 	hoek2Y.append(y1[i+Nshift2])
# 	hoek2Y.append(breedte)

# 	hoek3X.append(x2[i])
#  	hoek3X.append(0)
# 	hoek3Y.append(breedte)
# 	hoek3Y.append(y2[i+Nshift2])

# 	hoek4X.append(0)
# 	hoek4X.append(x1[i])
# 	hoek4Y.append(y2[i+Nshift2])
# 	hoek4Y.append(0)

# layer2_hoek1X = []
# layer2_hoek1Y = []
# layer2_hoek2X = []
# layer2_hoek2Y = []
# layer2_hoek3X = []
# layer2_hoek3Y = []
# layer2_hoek4X = []
# layer2_hoek4Y = []
# for i in range(layer2_Nshift+1,len(x1)-layer2_Nshift2):
# 	layer2_hoek1X.append(x1[i])
#  	layer2_hoek1X.append(breedte)
# 	layer2_hoek1Y.append(0)
# 	layer2_hoek1Y.append(y1[i+layer2_Nshift2])

# 	layer2_hoek2X.append(breedte)
# 	layer2_hoek2X.append(x2[i])
# 	layer2_hoek2Y.append(y1[i+layer2_Nshift2])
# 	layer2_hoek2Y.append(breedte)

# 	layer2_hoek3X.append(x2[i])
#  	layer2_hoek3X.append(0)
# 	layer2_hoek3Y.append(breedte)
# 	layer2_hoek3Y.append(y2[i+layer2_Nshift2])

# 	layer2_hoek4X.append(0)
# 	layer2_hoek4X.append(x1[i])
# 	layer2_hoek4Y.append(y2[i+layer2_Nshift2])
# 	layer2_hoek4Y.append(0)

# layer3_hoek1X = []
# layer3_hoek1Y = []
# layer3_hoek2X = []
# layer3_hoek2Y = []
# layer3_hoek3X = []
# layer3_hoek3Y = []
# layer3_hoek4X = []
# layer3_hoek4Y = []
# for i in range(layer3_Nshift,len(x1)-layer3_Nshift2):
# 	layer3_hoek1X.append(x1[Nspijkers-1-i])
#  	layer3_hoek1X.append(breedte)
# 	layer3_hoek1Y.append(0)
# 	layer3_hoek1Y.append(y1[Nspijkers-i-layer3_Nshift2])

# 	layer3_hoek2X.append(breedte)
# 	layer3_hoek2X.append(x2[Nspijkers-1-i])
# 	layer3_hoek2Y.append(y1[Nspijkers-i-layer3_Nshift2])
# 	layer3_hoek2Y.append(breedte)

# 	layer3_hoek3X.append(x2[Nspijkers-1-i])
#  	layer3_hoek3X.append(0)
# 	layer3_hoek3Y.append(breedte)
# 	layer3_hoek3Y.append(y2[Nspijkers-i-layer3_Nshift2])

# 	layer3_hoek4X.append(0)
# 	layer3_hoek4X.append(x1[Nspijkers-1-i])
# 	layer3_hoek4Y.append(y2[Nspijkers-i-layer3_Nshift2])
# 	layer3_hoek4Y.append(0)


# recht1X = []
# recht1Y = []
# recht2X = []
# recht2Y = []
# recht3X = []
# recht3Y = []
# recht4X = []
# recht4Y = []
# for i in range(Nshift_recht, len(x1)):
# 	recht1X.append(x1[i])
#  	recht1X.append(breedte)
# 	recht1Y.append(0)
# 	recht1Y.append(y1[Nspijkers-1-i+Nshift_recht])

# 	recht2X.append(breedte)
# 	recht2X.append(x2[i])
# 	recht2Y.append(y1[Nspijkers-1-i+Nshift_recht])
# 	recht2Y.append(breedte)

# 	recht3X.append(x2[i])
#  	recht3X.append(0)
# 	recht3Y.append(breedte)
# 	recht3Y.append(y2[Nspijkers-1-i+Nshift_recht])

# 	recht4X.append(0)
# 	recht4X.append(x1[i])
# 	recht4Y.append(y2[Nspijkers-1-i+Nshift_recht])
# 	recht4Y.append(0)

# fig = plt.figure()
# #contour
# plt.plot(x1,np.zeros(len(x1)),'ko')
# plt.plot(x2,np.ones(len(x1))*breedte,'ko')
# plt.plot(np.zeros(len(y1)),y1,'ko')
# plt.plot(np.ones(len(y1))*breedte,y2,'ko')




# plt.axis([-blat,breedte+blat,-blat,breedte+blat])
# plt.gca().set_aspect('equal', adjustable='box') # make axes equal

# #plot patterns


# # plt.plot(cross1X,cross1Y,'b-')
# # plt.plot(cross2X,cross2Y,'b-')

# plt.plot(layer2_hoek1X,layer2_hoek1Y,'m-')
# plt.plot(layer2_hoek3X,layer2_hoek3Y,'m-')
# plt.plot(layer3_hoek2X,layer3_hoek2Y,'m-')
# plt.plot(layer3_hoek4X,layer3_hoek4Y,'m-')

# plt.plot(hoek1X,hoek1Y,'r-')
# plt.plot(hoek2X,hoek2Y,'r-')
# plt.plot(hoek3X,hoek3Y,'r-')
# plt.plot(hoek4X,hoek4Y,'r-')

# plt.plot(layer2_hoek2X,layer2_hoek2Y,'b-')
# plt.plot(layer2_hoek4X,layer2_hoek4Y,'b-')
# plt.plot(layer3_hoek1X,layer3_hoek1Y,'b-')
# plt.plot(layer3_hoek3X,layer3_hoek3Y,'b-')





# # plt.plot(recht1X,recht1Y,'b-')
# # plt.plot(recht2X,recht2Y,'b-')
# # plt.plot(recht3X,recht3Y,'b-')
# # plt.plot(recht4X,recht4Y,'b-')



# plt.show()
# fig.savefig("squareC_9.png")


# # COLORS
# # blue		b	[0,0,1]
# # black		k	[0,0,0]
# # red		r	[1,0,0]
# # green		g	[0,1,0]
# # yellow	y	[1,1,0]
# # cyan		c	[0,1,1]
# # magenta	m	[1,0,1]
# # white		w	[1,1,1]

# # Calculate distances
# distanceKruis = 0
# distanceHoek = 0
# distanceRecht = 0

# for count in range(1,len(hoek1X)):
# 	distanceHoek += math.sqrt(math.pow(hoek1X[count]-hoek1X[count-1],2) + math.pow(hoek1Y[count]-hoek1Y[count-1],2))
	
# for count in range(1,len(cross1X)):
# 	distanceKruis += math.sqrt(math.pow(cross1X[count]-cross1X[count-1],2) + math.pow(cross1Y[count]-cross1Y[count-1],2))

# for count in range(1,len(recht1X)):
# 	distanceRecht += math.sqrt(math.pow(recht1X[count]-recht1X[count-1],2) + math.pow(recht1Y[count]-recht1Y[count-1],2))

# print("Lengte String: " + str(round((distanceHoek*4)/1000,2)) + "m")
# print("Aantal Spijkers: " + str(Nspijkers*4-4))