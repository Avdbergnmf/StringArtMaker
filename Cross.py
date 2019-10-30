#!/usr/bin/env python3
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

		NailCount = nails*4-3

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
	def __init__(self,width,nails,thick,Nshift=0,trimStart=0,trimEnd=0):
		super().__init__(width,nails,thick)
		self.Nshift = Nshift
		self.trimStart = trimStart
		self.trimEnd = trimEnd

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
				self.StringLengthThis += math.sqrt(math.pow(self.curve1X[count]-self.curve1X[count-1],2) + math.pow(self.curve1X[count]-self.curve1X[count-1],2)) 
			# StringLength += self.StringLengthThis


	def plot(self,color='b',makeTut=0,tutName="cross"):

		for i in range(1,len(self.curve1X)):
			plt.plot(self.curve1X[0:i],self.curve1Y[0:i],color,linewidth=1)
			if(makeTut):
				fig.savefig(tutName+str(i)+".png")
		# plt.plot(self.curve1X,self.curve1Y,self.color,linewidth=1)
		# if(makeTut):
		# 	fig.savefig(tutName+".png")

class Straight(Cross):
	def __init__(self,width,nails,thick,Nshift=0,trimStart=0,trimEnd=0):
		super().__init__(width,nails,thick)
		self.Nshift = Nshift
		self.trimStart = trimStart
		self.trimEnd = trimEnd

		self.curve1X = []
		self.curve1Y = []
		if(self.Nshift>0):
			Nstart = self.Nshift
			Nend = 0
		else:
			Nstart = 0
			Nend = -self.Nshift
			
		for i in range(Nstart+self.trimStart,self.nails-Nend-self.trimEnd):
			print(i)
			print(Nend)
			self.curve1X.append(self.x1[i])
			self.curve1Y.append(0)

			self.curve1X.append(0)
			self.curve1Y.append(self.y2[i-self.Nshift])

			self.curve1X.append(self.x3[i])
			self.curve1Y.append(0)

			self.curve1X.append(0)
			self.curve1Y.append(self.y4[i-self.Nshift])

			self.curve1X.append(self.x1[i])
			self.curve1Y.append(0)

			self.StringLengthThis = 0
			for count in range(1,len(self.curve1X)):
				self.StringLengthThis += math.sqrt(math.pow(self.curve1X[count]-self.curve1X[count-1],2) + math.pow(self.curve1X[count]-self.curve1X[count-1],2))
			# StringLength += self.StringLengthThis


	def plot(self,color='b',makeTut=0,tutName="cross"):

		for i in range(1,len(self.curve1X)):
			plt.plot(self.curve1X[0:i],self.curve1Y[0:i],color,linewidth=1)
			if(makeTut):
				fig.savefig(tutName+str(i)+".png")
		# plt.plot(self.curve1X,self.curve1Y,self.color,linewidth=1)
		# if(makeTut):
		# 	fig.savefig(tutName+".png")






c1 = Curve(500,16,38,-4,0,0)
# c2 = Curve(500,13,38,-4,0,5)
# c3 = Curve(500,13,38,5,0,0)
s1 = Straight(500,16,38,5,0,0)


fig = plt.figure()
c1.plotCross()
# c1.plot('r',0,"1CrossA")
s1.plot('b',0,"1CrossA")

# plt.clf() # To clear figure (but leaves axes) -> need to replot cross though!

# c2.plot('b',1,"2CrossA")
# c3.plot('y',1,"3CrossA")
plt.show()


# # COLORS
# # blue		b	[0,0,1]
# # black		k	[0,0,0]
# # red		r	[1,0,0]
# # green		g	[0,1,0]
# # yellow	y	[1,1,0]
# # cyan		c	[0,1,1]
# # magenta	m	[1,0,1]
# # white		w	[1,1,1]

# print("Lengte String: " + str(round((distanceHoek+distanceHoek_layer2+distanceHoek_layer3)*4/1000,2)) + "m")
# print("Aantal Spijkers: " + str(Nspijkers*4-4))