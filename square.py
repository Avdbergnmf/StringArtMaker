		



				



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