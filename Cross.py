#!/usr/bin/env python
# Test prog stringart triangle

import matplotlib.pyplot as plt
import numpy as np
import math

# Global Vars
StringLength = 0
NailCount = 0

class Cross:
	def __init__(self,width,nails,thick):
		self.width=width
		self.nails=nails
		self.thick=thick

		NailCount = nails*4

		self.nailwidth = width-thick

		half = self.nailwidth/2

		self.x1 = np.linspace(0,half,nails) # rechts
		self.y1 = np.zeros(nails)
		self.x2 = np.zeros(nails) # boven
		self.y2 = np.linspace(0,half,nails)
		self.x3 = np.linspace(0,-half,nails) # links
		self.y3 = np.zeros(nails)
		self.x4 = np.zeros(nails) # onder
		self.y4 = np.linspace(0,-half,nails)

		self.xcontourplot = [thick/2,width/2,width/2,thick/2,thick/2,-thick/2,-thick/2,-width/2,-width/2,-thick/2,-thick/2,thick/2,thick/2]
		self.ycontourplot = [thick/2,thick/2,-thick/2,-thick/2,-width/2,-width/2,-thick/2,-thick/2,thick/2,thick/2,width/2,width/2,thick/2]

	def plotCross(self):
		plt.plot(self.x1,self.y1,'ko',linewidth=1)
		plt.plot(self.x2,self.y2,'ko',linewidth=1)
		plt.plot(self.x3,self.y3,'ko',linewidth=1)
		plt.plot(self.x4,self.y4,'ko',linewidth=1)
		plt.plot(self.xcontourplot,self.ycontourplot,'k-',linewidth=1)
		plt.axis([-self.width/2-self.thick,self.width/2+self.thick,-self.width/2-self.thick,self.width/2+self.thick])
		plt.gca().set_aspect('equal', adjustable='box') # make axes equal

class Curve(Cross):
	def __init__(self,width,nails,thick,Nshift=0,trimStart=0,trimEnd=0,color='b'):
		super().__init__(width,nails,thick)
		self.Nshift = Nshift
		self.trimStart = trimStart
		self.trimEnd = trimEnd
		self.color = color

		self.curve1X = []
		self.curve1Y = []
		if(self.Nshift<0):
			Nstart = -self.Nshift
			Nend = 0
		else:
			Nstart = 0
			Nend = self.Nshift
			
		for i in range(Nstart+self.trimStart,self.nails-Nend-self.trimEnd):
			self.curve1X.append(self.x1[i])
			self.curve1Y.append(0)

			self.curve1X.append(0)
			self.curve1Y.append(self.y2[self.nails-1-i-self.Nshift])

			self.curve1X.append(self.x3[i])
			self.curve1Y.append(0)

			self.curve1X.append(0)
			self.curve1Y.append(self.y4[self.nails-1-i-self.Nshift])

			self.curve1X.append(self.x1[i])
			self.curve1Y.append(0)

			self.StringLengthThis = 0
			for count in range(1,len(self.curve1X)):
				self.StringLengthThis += math.sqrt(math.pow(self.curve1X[count]-self.curve1X[count-1],2) + math.pow(self.curve1X[count]-self.curve1X[count-1],2)) # *4 cause 4 quadrants
			# StringLength += self.StringLengthThis


	def plotCurve(self,makeTut=0,tutName="cross"):

		for i in range(1,len(self.curve1X)):
			plt.plot(self.curve1X[0:i],self.curve1Y[0:i],self.color,linewidth=1)
			if(makeTut):
				fig.savefig(tutName+str(i)+".png")
		# plt.plot(self.curve1X,self.curve1Y,self.color,linewidth=1)
		# if(makeTut):
		# 	fig.savefig(tutName+".png")



c1 = Curve(500,13,38,-4,0,0,'r')
# c2 = Curve(500,13,38,-4,0,5,'b')
# c3 = Curve(500,13,38,5,0,0,'y')


fig = plt.figure()
c1.plotCross()
c1.plotCurve(1,"1CrossA")
# c2.plotCurve(1,"2CrossA")
# c3.plotCurve(1,"3CrossA")
plt.show()



# blat = 38

# breedte = 500-blat #mm
# Nspijkers = 20 #mm

# afstand = breedte/Nspijkers

# helft = breedte/2

# x1 = np.linspace(0,helft,Nspijkers) # rechts
# y1 = np.zeros(Nspijkers)
# x2 = np.zeros(Nspijkers) # boven
# y2 = np.linspace(0,helft,Nspijkers)
# x3 = np.linspace(0,-helft,Nspijkers) # links
# y3 = np.zeros(Nspijkers)
# x4 = np.zeros(Nspijkers) # onder
# y4 = np.linspace(0,-helft,Nspijkers)

# Nshift = 5
# Nshift2 = 5

# layer2_Nshift = 0
# layer2_Nshift2 = 15

# layer3_Nshift = 10
# layer3_Nshift2 = 0

# straight_Nshift = 0
# straight_Nshift2 = 10

# hoek1X = []
# hoek1Y = []
# hoek2X = []
# hoek2Y = []
# hoek3X = []
# hoek3Y = []
# hoek4X = []
# hoek4Y = []
# for i in range(0,Nspijkers-Nshift2-Nshift):
# 	hoek1X.append(x1[i+Nshift2])
# 	hoek1X.append(0)
# 	hoek1Y.append(0)
# 	hoek1Y.append(y2[Nspijkers-1-i-Nshift])

# 	hoek2X.append(0)
# 	hoek2X.append(x3[Nspijkers-1-i-Nshift])
# 	hoek2Y.append(y2[i+Nshift2])
# 	hoek2Y.append(0)

# 	hoek3X.append(x3[i+Nshift2])
# 	hoek3X.append(0)
# 	hoek3Y.append(0)
# 	hoek3Y.append(y4[Nspijkers-1-i-Nshift])

# 	hoek4X.append(0)
# 	hoek4X.append(x1[Nspijkers-1-i-Nshift])
# 	hoek4Y.append(y4[i+Nshift2])
# 	hoek4Y.append(0)

# layer2_hoek1X = []
# layer2_hoek1Y = []
# layer2_hoek2X = []
# layer2_hoek2Y = []
# layer2_hoek3X = []
# layer2_hoek3Y = []
# layer2_hoek4X = []
# layer2_hoek4Y = []
# for i in range(0,Nspijkers-layer2_Nshift2-layer2_Nshift):
# 	layer2_hoek1X.append(x1[i+layer2_Nshift2])
# 	layer2_hoek1X.append(0)
# 	layer2_hoek1Y.append(0)
# 	layer2_hoek1Y.append(y2[Nspijkers-1-i-layer2_Nshift])

# 	layer2_hoek2X.append(0)
# 	layer2_hoek2X.append(x3[Nspijkers-1-i-layer2_Nshift])
# 	layer2_hoek2Y.append(y2[i+layer2_Nshift2])
# 	layer2_hoek2Y.append(0)

# 	layer2_hoek3X.append(x3[i+layer2_Nshift2])
# 	layer2_hoek3X.append(0)
# 	layer2_hoek3Y.append(0)
# 	layer2_hoek3Y.append(y4[Nspijkers-1-i-layer2_Nshift])

# 	layer2_hoek4X.append(0)
# 	layer2_hoek4X.append(x1[Nspijkers-1-i-layer2_Nshift])
# 	layer2_hoek4Y.append(y4[i+layer2_Nshift2])
# 	layer2_hoek4Y.append(0)

# layer3_hoek1X = []
# layer3_hoek1Y = []
# layer3_hoek2X = []
# layer3_hoek2Y = []
# layer3_hoek3X = []
# layer3_hoek3Y = []
# layer3_hoek4X = []
# layer3_hoek4Y = []
# for i in range(0,Nspijkers-layer3_Nshift2-layer3_Nshift):
# 	layer3_hoek1X.append(x1[i+layer3_Nshift2])
# 	layer3_hoek1X.append(0)
# 	layer3_hoek1Y.append(0)
# 	layer3_hoek1Y.append(y2[Nspijkers-1-i-layer3_Nshift])

# 	layer3_hoek2X.append(0)
# 	layer3_hoek2X.append(x3[Nspijkers-1-i-layer3_Nshift])
# 	layer3_hoek2Y.append(y2[i+layer3_Nshift2])
# 	layer3_hoek2Y.append(0)

# 	layer3_hoek3X.append(x3[i+layer3_Nshift2])
# 	layer3_hoek3X.append(0)
# 	layer3_hoek3Y.append(0)
# 	layer3_hoek3Y.append(y4[Nspijkers-1-i-layer3_Nshift])

# 	layer3_hoek4X.append(0)
# 	layer3_hoek4X.append(x1[Nspijkers-1-i-layer3_Nshift])
# 	layer3_hoek4Y.append(y4[i+layer3_Nshift2])
# 	layer3_hoek4Y.append(0)


# straight_hoek1X = []
# straight_hoek1Y = []
# straight_hoek2X = []
# straight_hoek2Y = []
# straight_hoek3X = []
# straight_hoek3Y = []
# straight_hoek4X = []
# straight_hoek4Y = []
# for i in range(straight_Nshift,Nspijkers-straight_Nshift2):
# 	straight_hoek1X.append(x1[i])
# 	straight_hoek1X.append(0)
# 	straight_hoek1Y.append(0)
# 	straight_hoek1Y.append(y2[i])

# 	straight_hoek2X.append(0)
# 	straight_hoek2X.append(x3[i])
# 	straight_hoek2Y.append(y2[i])
# 	straight_hoek2Y.append(0)

# 	straight_hoek3X.append(x3[i])
# 	straight_hoek3X.append(0)
# 	straight_hoek3Y.append(0)
# 	straight_hoek3Y.append(y4[i])

# 	straight_hoek4X.append(0)
# 	straight_hoek4X.append(x1[i])
# 	straight_hoek4Y.append(y4[i])
# 	straight_hoek4Y.append(0)

# fig = plt.figure()




# #plot patterns
# plt.plot(hoek1X,hoek1Y,'r-',linewidth=1.0)
# plt.plot(hoek2X,hoek2Y,'r-',linewidth=1.0)
# plt.plot(hoek3X,hoek3Y,'r-',linewidth=1.0)
# plt.plot(hoek4X,hoek4Y,'r-',linewidth=1.0)

# plt.plot(layer2_hoek1X,layer2_hoek1Y,'b-',linewidth=1.0)
# plt.plot(layer2_hoek2X,layer2_hoek2Y,'b-',linewidth=1.0)
# plt.plot(layer2_hoek3X,layer2_hoek3Y,'b-',linewidth=1.0)
# plt.plot(layer2_hoek4X,layer2_hoek4Y,'b-',linewidth=1.0)

# plt.plot(layer3_hoek1X,layer3_hoek1Y,'y-',linewidth=1.0)
# plt.plot(layer3_hoek2X,layer3_hoek2Y,'y-',linewidth=1.0)
# plt.plot(layer3_hoek3X,layer3_hoek3Y,'y-',linewidth=1.0)
# plt.plot(layer3_hoek4X,layer3_hoek4Y,'y-',linewidth=1.0)

# # plt.plot(straight_hoek1X,straight_hoek1Y,'y-')
# # plt.plot(straight_hoek2X,straight_hoek2Y,'y-')
# # plt.plot(straight_hoek3X,straight_hoek3Y,'y-')
# # plt.plot(straight_hoek4X,straight_hoek4Y,'y-')

# plt.show()
# fig.savefig("cross1.png")

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
# distanceHoek = 0
# distanceHoek_layer2 = 0
# distanceHoek_layer3 = 0
# distanceHoek_straight = 0

# for count in range(1,len(hoek1X)):
# 	distanceHoek += math.sqrt(math.pow(hoek1X[count]-hoek1X[count-1],2) + math.pow(hoek1Y[count]-hoek1Y[count-1],2))
	
# for count in range(1,len(layer2_hoek1X)):
# 	distanceHoek_layer2 += math.sqrt(math.pow(layer2_hoek1X[count]-layer2_hoek1X[count-1],2) + math.pow(layer2_hoek1Y[count]-layer2_hoek1Y[count-1],2))

# for count in range(1,len(layer3_hoek1X)):
# 	distanceHoek_layer3 += math.sqrt(math.pow(layer3_hoek1X[count]-layer3_hoek1X[count-1],2) + math.pow(layer3_hoek1Y[count]-layer3_hoek1Y[count-1],2))

# # for count in range(1,len(straight_hoek1X)):
# # 	distanceHoek_straight += math.sqrt(math.pow(straight_hoek1X[count]-straight_hoek1X[count-1],2) + math.pow(straight_hoek1Y[count]-straight_hoek1Y[count-1],2))

# print ((distanceHoek+distanceHoek_layer2+distanceHoek_layer3)*4)


# print("Lengte String: " + str(round((distanceHoek+distanceHoek_layer2+distanceHoek_layer3)*4/1000,2)) + "m")
# print("Aantal Spijkers: " + str(Nspijkers*4-4))