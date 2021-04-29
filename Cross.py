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


class Curve(Cross):
	def __init__(self,width,nails,thick,Nshift=0,trimStart=0,trimEnd=0):
		super().__init__(width,nails,thick)
		self.Nshift = Nshift
		self.trimStart = trimStart
		self.trimEnd = trimEnd

		self.StringLength = 0

		self.curveX = []
		self.curveY = []
		if(self.Nshift<0):
			Nstart = -self.Nshift
			Nend = 0
		else:
			Nstart = 0
			Nend = self.Nshift
			
		for i in range(Nstart+self.trimStart,self.nails-Nend-self.trimEnd):
			self.curveX.append(self.x1[i])
			self.curveY.append(0)

			self.curveX.append(0)
			self.curveY.append(self.y2[self.nails-1-i-self.Nshift])

			self.curveX.append(self.x3[i])
			self.curveY.append(0)

			self.curveX.append(0)
			self.curveY.append(self.y4[self.nails-1-i-self.Nshift])

			self.curveX.append(self.x1[i])
			self.curveY.append(0)

			
		for count in range(1,len(self.curveX)):
			self.StringLength += math.sqrt(math.pow(self.curveX[count]-self.curveX[count-1],2) + math.pow(self.curveY[count]-self.curveY[count-1],2)) 


	def plot(self,color='b',makePic=0,tutName="Cross",makeGif=0):
		if(makeGif):
			for i in range(1,len(self.curveX)+1):
				plt.plot(self.curveX[0:i],self.curveY[0:i],color,linewidth=1)
				fig.savefig(tutName+str(i)+".png")
		else:
			plt.plot(self.curveX,self.curveY,color,linewidth=1)
			if(makePic):
				fig.savefig(tutName+".png")

class Straight(Cross):
	def __init__(self,width,nails,thick,Nshift=0,trimStart=0,trimEnd=0):
		super().__init__(width,nails,thick)
		self.Nshift = Nshift
		self.trimStart = trimStart
		self.trimEnd = trimEnd

		self.StringLength = 0

		self.straightX = []
		self.straightY = []
		if(self.Nshift>0):
			Nstart = self.Nshift
			Nend = 0
		else:
			Nstart = 0
			Nend = -self.Nshift
			
		for i in range(Nstart+self.trimStart,self.nails-Nend-self.trimEnd):
			self.straightX.append(self.x1[i])
			self.straightY.append(0)

			self.straightX.append(0)
			self.straightY.append(self.y2[i-self.Nshift])

			self.straightX.append(self.x3[i])
			self.straightY.append(0)

			self.straightX.append(0)
			self.straightY.append(self.y4[i-self.Nshift])

			self.straightX.append(self.x1[i])
			self.straightY.append(0)

		for count in range(1,len(self.straightX)):
			self.StringLength += math.sqrt(math.pow(self.straightX[count]-self.straightX[count-1],2) + math.pow(self.straightY[count]-self.straightY[count-1],2))


	def plot(self,color='b',makePic=0,tutName="Cross",makeGif=0):
		if(makeGif):
			for i in range(1,len(self.straightX)+1):
				plt.plot(self.straightX[0:i],self.straightY[0:i],color,linewidth=1)
				fig.savefig(tutName+str(i)+".png")
		else:
			plt.plot(self.straightX,self.straightY,color,linewidth=1)
			if(makePic):
				fig.savefig(tutName+".png")
