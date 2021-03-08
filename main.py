import cv2 
import numpy as np 
from calculator import draw,calculate

cam = cv2.VideoCapture(1,cv2.CAP_DSHOW)  
l_green = (36,80,0) 
h_green = (86,255,255)
pre_area = 0 
area = 0
machine = calculate()
pen = draw((130,130,255),(255,180,180))
phrase = ''
def findObject(org,image):
	global frame,l_green,h_green,pre_area,area,phrase
	hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv,l_green,h_green)
	cnts,_ = cv2.findContours(mask,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
	if len(cnts) > 0:
		cnt = max(cnts,key=cv2.contourArea) 
		area = cv2.contourArea(cnt)
		if area >= 1200:
			M = cv2.moments(cnt)
			X = int(M['m10'] / M['m00'])
			Y = int(M['m01'] / M['m00'])
			if pre_area != 0:
				pressed = area-pre_area 
				org,phrase = pen.Draw(org,pen.getColor(),phrase,pressed=machine.click(pressed),X=X,Y=Y)
				cv2.putText(org,phrase,(100,70),cv2.FONT_HERSHEY_TRIPLEX,1,(130,255,130),2)
				pre_area = area
				return org
			pre_area = area
	return []

def main():
	while True:
		frame = cam.read()[1]
		frame = cv2.flip(frame,1)
		blurred = cv2.GaussianBlur(frame,(9,9),0)
		obj = findObject(frame,blurred)
		if len(obj) > 0:
			frame = obj
		cv2.imshow('UNNAMED',frame)
		if cv2.waitKey(1) == ord("q"):
			quit()

if __name__ == '__main__':
	main()