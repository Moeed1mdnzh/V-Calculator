import cv2 

class draw(object):
	"""
	draw the calculator
	"""
	def __init__(self,num_color,box_color):
		self.num_color = num_color 
		self.box_color = box_color 
		self.signs = [['0','1','2','+'],
				['3','4','5','-'],
				['6','7','8','x'],
				['9','.','/','=']]

	def Draw(self,frame,colors,pressed=False,x=0,y=0):
		x,y = 100,100
		for row in self.signs:
			for sign in row:
				cv2.rectangle(frame,(x,y),(x+80,y+80),colors[1],2)
				cv2.putText(frame,sign,(x+40,y+40),cv2.FONT_HERSHEY_TRIPLEX,0.7,colors[0],2)
				if pressed:
					pass
				x += 80 
			y += 80
			x = 100
		return frame

	def getColor(self):
		return self.num_color,self.box_color

class calculate:
	"""
	calculate phrase
	"""
	def __init__(self):
		pass 

	def Calc(self,phrase=""):
		pass 

	def click(self,area):
		if area >= 3000:
			print(area)
		return False