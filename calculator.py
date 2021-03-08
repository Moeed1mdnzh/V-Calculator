import cv2 

class draw(object):
	"""
	draw the calculator
	"""
	def __init__(self,num_color,box_color):
		self.num_color = num_color 
		self.box_color = box_color 
		self.machine = calculate()
		self.signs = [['0','1','2','+'],
				['3','4','5','-'],
				['6','7','8','x','D'],
				['9','.','/','=','C']]

	def Draw(self,frame,colors,phrase,pressed=False,X=0,Y=0):
		x,y = 100,100
		for row in self.signs:
			for sign in row:
				cv2.rectangle(frame,(x,y),(x+80,y+80),colors[1],10)
				cv2.putText(frame,sign,(x+35,y+45),cv2.FONT_HERSHEY_TRIPLEX,0.9,colors[0],3)
				if pressed:
					SIGN = self.machine.operate(phrase,(X,Y))
					if SIGN == 'C': 
						phrase = ''
					elif SIGN == 'D': 
						phrase = phrase[:len(phrase)-1]
					elif SIGN == '=': 
						phrase = self.machine.Calc(phrase)
					else: phrase += SIGN
					pressed = False
				x += 80 
			y += 80
			x = 100
		return frame,phrase

	def getColor(self):
		return self.num_color,self.box_color

class calculate:
	"""
	calculate phrase
	"""
	def __init__(self):
		self.boxes = {'0':(100,100),'1':(180,100),'2':(260,100),'+':(340,100),
				'3':(100,180),'4':(180,180),'5':(260,180),'-':(340,180),
				'6':(100,260),'7':(180,260),'8':(260,260),'x':(340,260),'D':(420,260),
				'9':(100,340),'.':(180,340),'/':(260,340),'=':(340,340),'C':(420,340)}

	def Calc(self,phrase=""):
		try:
			phrase = phrase.replace('x','*')
			return str(round(eval(phrase),2))
		except:
			return '[ERROR]'

	def operate(self,phrase,dot):
		x,y = dot 
		for k,v in self.boxes.items():
			if (x >= v[0] and x <= v[0]+79) and (y >= v[1] and y <= v[1]+79):
				return k
		return ''

	def click(self,area):
		if area >= 1800:
			return True
		return False