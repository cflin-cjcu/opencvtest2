import cv2 as cv
import numpy as np

def abc(x):
    pass

cv.namedWindow('res')
cv.createTrackbar('hmin','res',0,180,abc)
cv.createTrackbar('hmax','res',0,180,abc)
cv.createTrackbar('smin','res',0,255,abc)
cv.createTrackbar('smax','res',0,255,abc)
cv.createTrackbar('vmin','res',0,255,abc)
cv.createTrackbar('vmax','res',0,255,abc)
img = cv.imread('./image/test.jpg')
img = cv.resize(img,(300,200))
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    # _, frame = cap.read()
    frame = img
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    hmin = cv.getTrackbarPos('hmin','res')
    hmax = cv.getTrackbarPos('hmax','res')
    smin = cv.getTrackbarPos('smin','res')
    smax = cv.getTrackbarPos('smax','res')
    vmin = cv.getTrackbarPos('vmin','res')
    vmax = cv.getTrackbarPos('vmax','res')    
    # define range of blue color in HSV
    lower_blue = np.array([hmin,smin,vmin])
    upper_blue = np.array([hmax,smax,vmax])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
