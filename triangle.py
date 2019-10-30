# Test prog stringart triangle

import matplotlib.pyplot as plt
import numpy as np
import math

class Triangle:
	def __init__(self,width,nails,thick):
		self.width=width
		self.nails=nails
		self.thick=thick

		helft = width/2
		self.height = math.sqrt(3)*helft

		self.x1 = np.linspace(0,width,nails)
		self.y1 = np.zeros(nails)
		self.x2 = np.linspace(width,helft,nails)
		self.y2 = np.linspace(0,self.height,nails)
		self.x3 = np.linspace(helft,0,nails)
		self.y3 = np.linspace(self.height,0,nails)

		thickTop = np.sqrt(3)*thick/2
		thickDiag = (thick/2)/np.tan(np.pi/6)

		self.xcontour1 = [-thickDiag,width+thick,helft,-thickDiag]
		self.ycontour1 = [-thickDiag/2,-thickDiag/2,self.height+thickTop,-thickDiag/2]

		self.xcontour2 = [thickDiag,width-thickDiag,helft,thickDiag]
		self.ycontour2 = [thickDiag/2,thickDiag/2,self.height-thickTop,thickDiag/2]
		
	def plotTriangle(self):
		plt.plot(self.x1,self.y1,'ko',linewidth=1)
		plt.plot(self.x2,self.y2,'ko',linewidth=1)
		plt.plot(self.x3,self.y3,'ko',linewidth=1)
		
		# outer contour
		plt.plot(self.xcontour1,self.ycontour1,'k')
		plt.plot(self.xcontour2,self.ycontour2,'k')

		plt.axis([-self.thick*1.5,self.width+self.thick*1.5,-self.thick*1.5,self.height+self.thick*1.5])
		plt.ylabel("height [mm]")
		plt.xlabel("width [mm]")
		plt.gca().set_aspect('equal', adjustable='box') # make axes equal

class Curve(Triangle):
	def __init__(self,width,nails,thick,Nshift=0,trimStart=0,trimEnd=0,parts=[1,1,1]):
		super().__init__(width,nails,thick)
		self.Nshift = Nshift
		self.trimStart = trimStart
		self.trimEnd = trimEnd

		self.curve1X = []
		self.curve1Y = []
		self.curve2X = []
		self.curve2Y = []
		self.curve3X = []
		self.curve3Y = []

		if(self.Nshift<0):
			Nstart = -self.Nshift
			Nend = 0
		else:
			Nstart = 0
			Nend = self.Nshift
			
		if(parts[0]):
			for i in range(Nstart+self.trimStart,self.nails-Nend-self.trimEnd):
					self.curve1X.append(self.x1[i])
					self.curve1X.append(self.x2[i+Nshift])
					self.curve1Y.append(self.y1[i])
					self.curve1Y.append(self.y2[i+Nshift])
		if(parts[1]):
			for i in range(Nstart+self.trimStart,self.nails-Nend-self.trimEnd):
					self.curve2X.append(self.x2[i])
					self.curve2X.append(self.x3[i+Nshift])
					self.curve2Y.append(self.y2[i])
					self.curve2Y.append(self.y3[i+Nshift])
		if(parts[2]):
			for i in range(Nstart+self.trimStart,self.nails-Nend-self.trimEnd):
					self.curve3X.append(self.x3[i])
					self.curve3X.append(self.x1[i+Nshift])
					self.curve3Y.append(self.y3[i])
					self.curve3Y.append(self.y1[i+Nshift])

	def plot(self,color='b',makePic=0,tutName="Square",makeGif=0):
		if(makeGif):
			for i in range(1,len(self.curve1X)+1):
				plt.plot(self.curve1X[0:i],self.curve1Y[0:i],color,linewidth=1)
				fig.savefig(tutName+"A"+str(i)+".png")
			for i in range(1,len(self.curve2X)+1):
				plt.plot(self.curve2X[0:i],self.curve2Y[0:i],color,linewidth=1)
				fig.savefig(tutName+"B"+str(i)+".png")
			for i in range(1,len(self.curve3X)+1):
				plt.plot(self.curve3X[0:i],self.curve3Y[0:i],color,linewidth=1)
				fig.savefig(tutName+"C"+str(i)+".png")

		else:
			plt.plot(self.curve1X,self.curve1Y,color,linewidth=1)
			plt.plot(self.curve2X,self.curve2Y,color,linewidth=1)
			plt.plot(self.curve3X,self.curve3Y,color,linewidth=1)
			if(makePic):
				fig.savefig(tutName+".png")

class Straight(Triangle):
	def __init__(self,width,nails,thick,Nshift=0,trimStart=0,trimEnd=0,parts=[1,1,1]):
		super().__init__(width,nails,thick)
		self.Nshift = Nshift
		self.trimStart = trimStart
		self.trimEnd = trimEnd

		self.straight1X = []
		self.straight1Y = []
		self.straight2X = []
		self.straight2Y = []
		self.straight3X = []
		self.straight3Y = []

		if(self.Nshift<0):
			Nstart = -self.Nshift
			Nend = 0
		else:
			Nstart = 0
			Nend = self.Nshift
			
		if(parts[0]):
			for i in range(Nstart+self.trimStart,self.nails-Nend-self.trimEnd):
					self.straight1X.append(self.x1[i])
					self.straight1Y.append(self.y1[i])
					self.straight1X.append(self.x2[nails-1-i-Nshift])
					self.straight1Y.append(self.y2[nails-1-i-Nshift])
					if(nails-2-i-Nshift>=0):
						self.straight1X.append(self.x2[nails-2-i-Nshift])
						self.straight1Y.append(self.y2[nails-2-i-Nshift])
		if(parts[1]):
			for i in range(Nstart+self.trimStart,self.nails-Nend-self.trimEnd):
					self.straight2X.append(self.x2[i])
					self.straight2Y.append(self.y2[i])
					self.straight2X.append(self.x3[nails-1-i-Nshift])
					self.straight2Y.append(self.y3[nails-1-i-Nshift])
					if(nails-2-i-Nshift>=0):
						self.straight2X.append(self.x3[nails-2-i-Nshift])
						self.straight2Y.append(self.y3[nails-2-i-Nshift])

		if(parts[2]):
			for i in range(Nstart+self.trimStart,self.nails-Nend-self.trimEnd):
					self.straight3X.append(self.x3[i])
					self.straight3Y.append(self.y3[i])
					self.straight3X.append(self.x1[nails-1-i-Nshift])
					self.straight3Y.append(self.y1[nails-1-i-Nshift])
					if(nails-2-i-Nshift>=0):
						self.straight3X.append(self.x1[nails-2-i-Nshift])
						self.straight3Y.append(self.y1[nails-2-i-Nshift])

	def plot(self,color='b',makePic=0,tutName="Square",makeGif=0):
		if(makeGif):
			for i in range(1,len(self.straight1X)+1):
				plt.plot(self.straight1X[0:i],self.straight1Y[0:i],color,linewidth=1)
				fig.savefig(tutName+"A"+str(i)+".png")
			for i in range(1,len(self.straight2X)+1):
				plt.plot(self.straight2X[0:i],self.straight2Y[0:i],color,linewidth=1)
				fig.savefig(tutName+"B"+str(i)+".png")
			for i in range(1,len(self.straight3X)+1):
				plt.plot(self.straight3X[0:i],self.straight3Y[0:i],color,linewidth=1)
				fig.savefig(tutName+"C"+str(i)+".png")

		else:
			plt.plot(self.straight1X,self.straight1Y,color,linewidth=1)
			plt.plot(self.straight2X,self.straight2Y,color,linewidth=1)
			plt.plot(self.straight3X,self.straight3Y,color,linewidth=1)
			if(makePic):
				fig.savefig(tutName+".png")

s1 = Straight(445,22,30,0,0,18)
c1 = Curve(445,22,30,11,0,0)

# c2 = Curve(445,22,30,0,0,0,[0,1,0])
# c3 = Curve(445,22,30,0,0,0,[0,0,1])

fig = plt.figure()
c1.plotTriangle()
s1.plot('r')
c1.plot('b',1,"A",0)
# c2.plot('b',1,"A",0)

plt.show()


# COLORS
# blue		b	[0,0,1]
# black		k	[0,0,0]
# red		r	[1,0,0]
# green		g	[0,1,0]
# yellow	y	[1,1,0]
# cyan		c	[0,1,1]
# magenta	m	[1,0,1]
# white		w	[1,1,1]