""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('C:\Users\dabrahams\AppData\Local\Continuum\Anaconda\pkgs\opencv-2.4.9.1-np19py27_0\Library\include\opencv\data\haarcascades')
print face_cascade


while(True):
	ret, frame = cap.read()
	faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
	for (x,y,w,h) in faces:
		print 'face'
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()