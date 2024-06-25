import cv2
from util import color_limit
from PIL import Image

cam = cv2.VideoCapture(0)
pink = [147,20,255]
yellow = [0,255,255]
color = yellow
while True:
   
    ret, frame = cam.read()
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit,upperLimit=color_limit(color=yellow)
    mask = cv2.inRange(hsvImage, lowerLimit,upperLimit)

    
    cv2.imshow('mask',mask)
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    if bbox!=None:
        x, y, w, h = bbox
        frame=cv2.rectangle(frame, (x, y), (w,h),(0,255,0),4)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cam.release()
#print("mask",mask)