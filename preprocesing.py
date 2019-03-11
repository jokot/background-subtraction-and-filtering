import numpy as np
import cv2

def filter_mask(img):
    cv2.imshow('bacground',img)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('closing',closing)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
    cv2.imshow('opening',opening)
    dilation = cv2.dilate(opening, kernel, iterations=1)
    cv2.imshow('dilation',dilation)
        

##    return opening
##    return dilation

cap = cv2.VideoCapture('http://cctv-dishub.sukoharjokab.go.id/zm/cgi-bin/nph-zms?mode=jpeg&monitor=8&scale=100&maxfps=15&buffer=1000&user=user&pass=user')
##cap = cv2.VideoCapture('output3.avi')
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

while(1):
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    
    
    
    fgmask = fgbg.apply(frame)
    filter_mask(fgmask)
    
    cv2.imshow('frame',frame)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
