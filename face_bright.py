import numpy as np
import cv2
from time import sleep
import os





def face_ident(face_detect):
	count = 0
	on = 0

	#if face detected
	if isinstance(face_detect,np.ndarray):
        count = 0
        on+=1
        if on > 10:
            os.system('xrandr --output eDP-1 --brightness 1')
        for (x, y , w , h) in face_detect:
            # print('Face')
            cv2.rectangle(frame, (x,y), (x+w, y+h), (209, 255, 82),25)
            
            

    else :
        on = 0
        # print('No Face')
        count = count+1
    
    #if away from screen    
    if count > 60:
        os.system('xrandr --output eDP-1 --brightness 0.01')
        # print('Lower brightness')


cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')


while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_detect = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)

    face_ident(face_detect)
        

    cv2.imshow('frame',frame)             
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()