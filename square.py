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
		plt.ylabel("height [mm]")
		plt.xlabel("width [mm]")
		plt.axis([-self.width/2-self.thick,self.width/2+self.thick,-self.width/2-self.thick,self.width/2+self.thick])
		plt.gca().set_aspect('equal', adjustable='box') # make axes equal

class Xpattern(Square):
	def __init__(self,width,nails,thick,Nshift=0,trimStart=0,trimEnd=0,parts=[1,1]):
		super().__init__(width,nails,thick)
		self.parts = parts
		self.Xpatt1X = []
		self.Xpatt1Y = []
		self.Xpatt2X = []
		self.Xpatt2Y = []

		self.StringLength = 0

		if(Nshift<0):
			Nstart = -Nshift
			Nend = 0
		else:
			Nstart = 0
			Nend = +Nshift

		if(self.parts[0]):
			for i in range(Nstart+trimStart,self.nails-Nend-trimEnd):
				self.Xpatt1X.append(self.x1[i+Nshift])
				self.Xpatt1Y.append(self.y1[i+Nshift])
				self.Xpatt1X.append(self.x3[i+Nshift])
				self.Xpatt1Y.append(self.y3[i+Nshift])
			for count in range(1,len(self.Xpatt1X)):
				self.StringLength += math.sqrt(math.pow(self.Xpatt1X[count]-self.Xpatt1X[count-1],2) + math.pow(self.Xpatt1Y[count]-self.Xpatt1Y[count-1],2))
		if(self.parts[1]):
			for i in range(Nstart+trimStart,self.nails-Nend-trimEnd):
				self.Xpatt2X.append(self.x2[i+Nshift])
				self.Xpatt2Y.append(self.y2[i+Nshift])
				self.Xpatt2X.append(self.x4[i+Nshift])
				self.Xpatt2Y.append(self.y4[i+Nshift])
			for count in range(1,len(self.Xpatt2X)):
				self.StringLength += math.sqrt(math.pow(self.Xpatt2X[count]-self.Xpatt2X[count-1],2) + math.pow(self.Xpatt2Y[count]-self.Xpatt2Y[count-1],2))

	def plot(self,color='b',makePic=0,tutName="Square",makeGif=0):
		if(makeGif):
			for i in range(1,len(self.Xpatt1X)+1):
				plt.plot(self.Xpatt1X[0:i],self.Xpatt1Y[0:i],color,linewidth=1)
				fig.savefig(tutName+"A"+str(i)+".png")
			for i in range(1,len(self.Xpatt1X)+1):
				plt.plot(self.Xpatt2X[0:i],self.Xpatt2Y[0:i],color,linewidth=1)
				fig.savefig(tutName+"B"+str(i)+".png")		
		else:
			plt.plot(self.Xpatt1X,self.Xpatt1Y,color,linewidth=1)
			plt.plot(self.Xpatt2X,self.Xpatt2Y,color,linewidth=1)
			if(makePic):
				fig.savefig(tutName+".png")
				
class Zigzag(Square):
	def __init__(self,width,nails,thick,Nshift=0,trimStart=0,trimEnd=0,parts=[1,1]):
		super().__init__(width,nails,thick)
		self.StringLengthThis=0
		self.parts = parts
		self.zigzag1X = []
		self.zigzag1Y = []
		self.zigzag2X = []
		self.zigzag2Y = []

		self.StringLength = 0

		if(Nshift<0):
			Nstart = -Nshift
			Nend = 0
		else:
			Nstart = 0
			Nend = Nshift

		if(parts[0]):
			for i in range(Nstart+trimStart,self.nails-Nend-trimEnd):
				self.zigzag1X.append(self.x1[i+Nshift])
				self.zigzag1Y.append(self.y1[i+Nshift])
				self.zigzag1X.append(self.x2[nails-1-i-Nshift])
				self.zigzag1Y.append(self.y2[nails-1-i-Nshift])
			for count in range(1,len(self.zigzag1X)):
				self.StringLength += math.sqrt(math.pow(self.zigzag1X[count]-self.zigzag1X[count-1],2) + math.pow(self.zigzag1Y[count]-self.zigzag1Y[count-1],2))
		if(parts[1]):
			for i in range(Nstart+trimStart,self.nails-Nend-trimEnd):
				self.zigzag2X.append(self.x4[i+Nshift])
				self.zigzag2Y.append(self.y4[i+Nshift])
				self.zigzag2X.append(self.x3[nails-1-i-Nshift])
				self.zigzag2Y.append(self.y3[nails-1-i-Nshift])
			for count in range(1,len(self.zigzag2X)):
				self.StringLength += math.sqrt(math.pow(self.zigzag2X[count]-self.zigzag2X[count-1],2) + math.pow(self.zigzag2Y[count]-self.zigzag2Y[count-1],2))

	def plot(self,color='b',makePic=0,tutName="Square",makeGif=0):
		if(makeGif):
			for i in range(1,len(self.zigzag1X)+1):
				plt.plot(self.zigzag1X[0:i],self.zigzag1Y[0:i],color,linewidth=1)
				fig.savefig(tutName+"A"+str(i)+".png")
			for i in range(1,len(self.zigzag1X)+1):
				plt.plot(self.zigzag2X[0:i],self.zigzag2Y[0:i],color,linewidth=1)
				fig.savefig(tutName+"B"+str(i)+".png")		
		else:
			plt.plot(self.zigzag1X,self.zigzag1Y,color,linewidth=1)
			plt.plot(self.zigzag2X,self.zigzag2Y,color,linewidth=1)
			if(makePic):
				fig.savefig(tutName+".png")


class Curve(Square):
	def __init__(self,width,nails,thick,Nshift=0,trimStart=0,trimEnd=0,parts=[1,1,1,1]):
		super().__init__(width,nails,thick)
		self.parts = parts

		self.StringLength = 0

		self.Curve1X = []
		self.Curve1Y = []
		self.Curve2X = []
		self.Curve2Y = []
		self.Curve3X = []
		self.Curve3Y = []
		self.Curve4X = []
		self.Curve4Y = []

		if(Nshift<0):
			Nstart = -Nshift
			Nend = 0
		else:
			Nstart = 0
			Nend = Nshift

		for i in range(Nstart+trimStart,self.nails-Nend-trimEnd):

			if(self.parts[0]):
				self.Curve1X.append(self.x1[i])
				self.Curve1Y.append(self.y1[i])
				self.Curve1X.append(self.x2[i+Nshift])
				self.Curve1Y.append(self.y2[i+Nshift])
			if(self.parts[1]):
				self.Curve2X.append(self.x2[i])
				self.Curve2Y.append(self.y2[i])
				self.Curve2X.append(self.x3[i+Nshift])
				self.Curve2Y.append(self.y3[i+Nshift])
			if(self.parts[2]):
				self.Curve3X.append(self.x3[i])
				self.Curve3Y.append(self.y3[i])
				self.Curve3X.append(self.x4[i+Nshift])
				self.Curve3Y.append(self.y4[i+Nshift])
			if(self.parts[3]):
				self.Curve4X.append(self.x4[i])
				self.Curve4Y.append(self.y4[i])
				self.Curve4X.append(self.x1[i+Nshift])
				self.Curve4Y.append(self.y1[i+Nshift])

		for count in range(1,len(self.Curve1X)):
			self.StringLength += math.sqrt(math.pow(self.Curve1X[count]-self.Curve1X[count-1],2) + math.pow(self.Curve1Y[count]-self.Curve1Y[count-1],2))
		for count in range(1,len(self.Curve2X)):
			self.StringLength += math.sqrt(math.pow(self.Curve2X[count]-self.Curve2X[count-1],2) + math.pow(self.Curve2Y[count]-self.Curve2Y[count-1],2))
		for count in range(1,len(self.Curve3X)):
			self.StringLength += math.sqrt(math.pow(self.Curve3X[count]-self.Curve3X[count-1],2) + math.pow(self.Curve3Y[count]-self.Curve3Y[count-1],2))
		for count in range(1,len(self.Curve4X)):
			self.StringLength += math.sqrt(math.pow(self.Curve4X[count]-self.Curve4X[count-1],2) + math.pow(self.Curve4Y[count]-self.Curve4Y[count-1],2))

	def plot(self,color='b',makePic=0,tutName="Square",makeGif=0):
		if(makeGif):
			for i in range(1,len(self.Curve1X)+1):
				plt.plot(self.Curve1X[0:i],self.Curve1Y[0:i],color,linewidth=1)
				fig.savefig(tutName+"A"+str(i)+".png")
			for i in range(1,len(self.Curve2X)+1):
				plt.plot(self.Curve2X[0:i],self.Curve2Y[0:i],color,linewidth=1)
				fig.savefig(tutName+"B"+str(i)+".png")
			for i in range(1,len(self.Curve3X)+1):
				plt.plot(self.Curve3X[0:i],self.Curve3Y[0:i],color,linewidth=1)
				fig.savefig(tutName+"C"+str(i)+".png")
			for i in range(1,len(self.Curve4X)+1):
				plt.plot(self.Curve4X[0:i],self.Curve4Y[0:i],color,linewidth=1)
				fig.savefig(tutName+"D"+str(i)+".png")

		else:
			plt.plot(self.Curve1X,self.Curve1Y,color,linewidth=1)
			plt.plot(self.Curve2X,self.Curve2Y,color,linewidth=1)
			plt.plot(self.Curve3X,self.Curve3Y,color,linewidth=1)
			plt.plot(self.Curve4X,self.Curve4Y,color,linewidth=1)
			if(makePic):
				fig.savefig(tutName+".png")

# Make plots
c1 = Curve(500,23,30,0,0,0)
c2 = Curve(500,23,30,-5,0,0)
c3 = Curve(500,23,30,-13,0,0)
c4 = Curve(500,23,30,13,0,0)


fig = plt.figure()

c1.plotSquare()
c1.plot('r')
c4.plot('y')
c2.plot('b')
c3.plot('m',1)




# print("Total string length: " + str(round((z1.StringLength+z2.StringLength+c1.StringLength)/1000,2)) + "m") # you need to add the used patterns yourself here
plt.show()

# plt.clf() # To clear figure (but leaves axes) -> need to replot cross though!

# COLORS
# blue		b	[0,0,1]
# black		k	[0,0,0]
# red		r	[1,0,0]
# green		g	[0,1,0]
# yellow	y	[1,1,0]
# cyan		c	[0,1,1]
# magenta	m	[1,0,1]
# white		w	[1,1,1]