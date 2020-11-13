class ColorManager:
	def getcolor(self,key):
		color=[0,0,0]

		color[0]=((int)(key[0:4])+(int)(key[12:]))%256
		color[1]=((int)(key[4:8])+(int)(key[12:]))%256
		color[2]=((int)(key[8:12])+(int)(key[12:]))%256
		return color
		