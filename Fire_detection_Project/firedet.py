import cv2
import numpy as np
from playsound import playsound

fire_rep = 0
alarm = False
  
video = cv2.VideoCapture("/Users/sandeepreddy/Documents/fire project/firebg.mov")

while(1):
    ret, frame = video.read()
    blur = cv2.GaussianBlur(frame,(31,31),cv2.BORDER_TRANSPARENT)
    hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    
    low = np.array([10,15,15],dtype='uint8')
    high = np.array([25,255,255],dtype='uint8')
    
    mask = cv2.inRange(hsv,low,high)
    op = cv2.bitwise_and(frame,hsv,mask=mask)
    
    range_of_fire = cv2.countNonZero(mask)
    
    if int(range_of_fire)>15000:
        fire_rep+=1
        
        if fire_rep>0:
            if alarm == False:
                playsound("alarm.mp3",True)
                alarm = True
    
    cv2.imshow('video',op)
    k = cv2.waitKey(1)
    if k==27:
        break
    
video.release()
cv2.destroyAllWindows()