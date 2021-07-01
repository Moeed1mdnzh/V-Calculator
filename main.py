import cv2 
import numpy as np 
import mediapipe as mp
from calculator import draw,calculate

cam = cv2.VideoCapture(0)  
machine = calculate()
pen = draw((130,130,255),(255,180,180))
phrase = ''
hand_base = mp.solutions.hands
hand = hand_base.Hands()
pre_x,pre_y = None,None
def findFinger(image,H,W):
	global phrase,pre_x,pre_y
	clone = image.copy()
	rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
	res = hand.process(rgb)
	if res.multi_hand_landmarks:
		for hand_landmarks in res.multi_hand_landmarks:
			finger = hand_landmarks.landmark[hand_base.HandLandmark.INDEX_FINGER_TIP]
			X,Y = int(finger.x*W),int(finger.y*H)
			if pre_y is not None: 
				org,phrase = pen.Draw(clone,pen.getColor(),phrase,pressed=machine.click(Y-pre_y),
					X=int(np.mean(np.array([X,pre_x]))),
					Y=int(np.mean(np.array([Y,pre_y])))
					)
				cv2.putText(org,phrase,(20,15),cv2.FONT_HERSHEY_TRIPLEX,0.6,(130,255,130),2)
				pre_x,pre_y = X,Y
				return org
			pre_x,pre_y = X,Y
		return clone
	return clone



def main():
	while True:
		frame = cam.read()[1]
		frame = cv2.resize(frame,(448,336))
		frame = cv2.flip(frame,1)
		frame = findFinger(frame,336,448)
		cv2.imshow('UNNAMED',frame)
		if cv2.waitKey(30) == ord("q"):
			quit()

if __name__ == '__main__':
	main()

"""org,phrase = pen.Draw(org,pen.getColor(),phrase,pressed=machine.click(pressed),X=X,Y=Y)
cv2.putText(org,phrase,(100,70),cv2.FONT_HERSHEY_TRIPLEX,1,(130,255,130),2)"""