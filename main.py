import cv2 
import numpy as np 

cam = cv2.VideoCapture(1,cv2.CAP_DSHOW)  
l_green = (36,80,0) 
h_green = (86,255,255)
pre_area = 0 
area = 0
def findObject(image):
	global l_green,h_green,pre_area,area
	hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv,l_green,h_green)
	cnts,_ = cv2.findContours(mask,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
	if len(cnts) > 0:
		cnt = max(cnts,key=cv2.contourArea) 
		area = cv2.contourArea(cnt)
		if area >= 1000:
			M = cv2.moments(cnt)
			X = int(M['m10'] / M['m00'])
			Y = int(M['m01'] / M['m00'])
			if pre_area != 0:
				pressed = area-pre_area 
				if pressed >= 500:
					pass
			pre_area = area

while True:
	frame = cam.read()[1]
	frame = cv2.flip(frame,1)
	blurred = cv2.GaussianBlur(frame,(9,9),0)
	findObject(blurred)
	cv2.imshow('UNNAMED',frame)
	if cv2.waitKey(1) == ord("q"):
		quit()