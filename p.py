import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(1):
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #设定红色
    lower_red=np.array([156,43,46])
    upper_red=np.array([180,255,255])
    
    mask=cv2.inRange(hsv,lower_red,upper_red)
    res=cv2.bitwise_and(frame,frame,mask=mask1)
    cv2.imshow("mask", mask1)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    cv2.imshow("frame", frame)
    k=cv2.waitKey(5)&0xff
    if k==27:
        break;
cap.release()
cv2.destroyWindow()
