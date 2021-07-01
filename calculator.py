import cv2 

class draw:
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
		x,y = 20,30
		for row in self.signs:
			for sign in row:
				cv2.rectangle(frame,(x,y),(x+40,y+40),colors[1],7)
				cv2.putText(frame,sign,(x+17,y+22),cv2.FONT_HERSHEY_TRIPLEX,0.7,colors[0],2)
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
				x += 40 
			y += 40
			x = 20
			cv2.circle(frame,(X,Y),4,(0,0,240),-1)
		return frame,phrase

	def getColor(self):
		return self.num_color,self.box_color

class calculate:
	"""
	calculate phrase
	"""
	def __init__(self):
		self.boxes = {'0':(20,30),'1':(60,30),'2':(100,30),'+':(140,30),
				'3':(20,80),'4':(60,80),'5':(100,80),'-':(140,80),
				'6':(20,110),'7':(60,110),'8':(100,110),'x':(140,110),'D':(180,110),
				'9':(20,150),'.':(60,150),'/':(100,150),'=':(140,150),'C':(180,150)}

	def Calc(self,phrase=""):
		try:
			phrase = phrase.replace('x','*')
			return str(round(eval(phrase),2))
		except:
			return '[ERROR]'

	def operate(self,phrase,dot):
		x,y = dot 
		for k,v in self.boxes.items():
			if (x >= v[0] and x <= v[0]+39) and (y >= v[1] and y <= v[1]+39):
				return k
		return ''

	def click(self,dist):
		if dist >= 15:
			return True
		return False