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

class Xpatt(Square):
	def __init__(self,width,nails,thick,Nshift=0,trimStart=0,trimEnd=0,parts=[1,1]):
		super().__init__(width,nails,thick)
		self.StringLengthThis=0
		self.parts = parts
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
			if(self.parts[0]):
				for i in range(1,len(self.Xpatt1X)+1):
					plt.plot(self.Xpatt1X[0:i],self.Xpatt1Y[0:i],color,linewidth=1)
					fig.savefig(tutName+"A"+str(i)+".png")
			if(self.parts[1]):
				for i in range(1,len(self.Xpatt1X)+1):
					plt.plot(self.Xpatt2X[0:i],self.Xpatt2Y[0:i],color,linewidth=1)
					fig.savefig(tutName+"B"+str(i)+".png")		
		else:
			if(self.parts[0]):
				plt.plot(self.Xpatt1X,self.Xpatt1Y,color,linewidth=1)
			if(self.parts[1]):
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
		if(parts[1]):
			for i in range(Nstart+trimStart,self.nails-Nend-trimEnd):
				self.zigzag2X.append(self.x4[i+Nshift])
				self.zigzag2Y.append(self.y4[i+Nshift])
				self.zigzag2X.append(self.x3[nails-1-i-Nshift])
				self.zigzag2Y.append(self.y3[nails-1-i-Nshift])

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
			self.Curve1X.append(self.x1[i+Nshift])
			self.Curve1Y.append(self.y1[i+Nshift])
			self.Curve1X.append(self.x2[i+Nshift])
			self.Curve1Y.append(self.y2[i+Nshift])

			self.Curve2X.append(self.x2[i+Nshift])
			self.Curve2Y.append(self.y2[i+Nshift])
			self.Curve2X.append(self.x3[i+Nshift])
			self.Curve2Y.append(self.y3[i+Nshift])

			self.Curve3X.append(self.x3[i+Nshift])
			self.Curve3Y.append(self.y3[i+Nshift])
			self.Curve3X.append(self.x4[i+Nshift])
			self.Curve3Y.append(self.y4[i+Nshift])

			self.Curve4X.append(self.x4[i+Nshift])
			self.Curve4Y.append(self.y4[i+Nshift])
			self.Curve4X.append(self.x1[i+Nshift])
			self.Curve4Y.append(self.y1[i+Nshift])

	def plot(self,color='b',makePic=0,tutName="Square",makeGif=0):
		if(makeGif):
			if(self.parts[0]):
				for i in range(1,len(self.Curve1X)+1):
					plt.plot(self.Curve1X[0:i],self.Curve1Y[0:i],color,linewidth=1)
					fig.savefig(tutName+"A"+str(i)+".png")
			if(self.parts[1]):
				for i in range(1,len(self.Curve2X)+1):
					plt.plot(self.Curve2X[0:i],self.Curve2Y[0:i],color,linewidth=1)
					fig.savefig(tutName+"B"+str(i)+".png")
			if(self.parts[2]):
				for i in range(1,len(self.Curve3X)+1):
					plt.plot(self.Curve3X[0:i],self.Curve3Y[0:i],color,linewidth=1)
					fig.savefig(tutName+"C"+str(i)+".png")
			if(self.parts[3]):
				for i in range(1,len(self.Curve4X)+1):
					plt.plot(self.Curve4X[0:i],self.Curve4Y[0:i],color,linewidth=1)
					fig.savefig(tutName+"D"+str(i)+".png")
		else:
			if(self.parts[0]):
				plt.plot(self.Curve1X,self.Curve1Y,color,linewidth=1)
			if(self.parts[1]):
				plt.plot(self.Curve2X,self.Curve2Y,color,linewidth=1)
			if(self.parts[2]):
				plt.plot(self.Curve3X,self.Curve3Y,color,linewidth=1)
			if(self.parts[3]):
				plt.plot(self.Curve4X,self.Curve4Y,color,linewidth=1)
			if(makePic):
				fig.savefig(tutName+".png")




# Xp1 = Xpatt(500,22,30,13,0,0,[1,0])
# Xp2 = Xpatt(500,22,30,-13,0,0,[0,1])
# Xp3 = Xpatt(500,22,30,0,0,13,[1,0])
# Xp4 = Xpatt(500,22,30,0,13,0,[0,1])

z1 = Zigzag(500,22,30,0,0,0)

c1 = Curve(500,22,30,17,0,0)
c2 = Curve(500,22,30,12,0,5)
c3 = Curve(500,22,30,7,0,10)
c4 = Curve(500,22,30,0,0,15)


fig = plt.figure()

z1.plotSquare()
# c1.plot('m',0,"A",1)
# c2.plot('r',0,"B",1)
# c3.plot('b',0,"C",1)
# c4.plot('y',0,"D",1)
# Xp1.plot('b',0,"A",1)
# Xp2.plot('b',0,"B",1)
# Xp4.plot('r',0,"C",1)
# Xp3.plot('r',0,"D",1)

z1.plot()


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