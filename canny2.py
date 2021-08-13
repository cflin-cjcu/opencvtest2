import cv2
import numpy as np
from matplotlib import pyplot as plt
def nothing(x):
    pass

img = cv2.imread('./image/test.jpg', 0)
img = cv2.resize(img,(800,600))
img = cv2.GaussianBlur(img,(5,5),0)
# sobelx = cv2.Sobel(img, cv2.CV_64F,1,0,ksize=3)
# sobelx = cv2.convertScaleAbs(sobelx)
# sobely = cv2.Sobel(img, cv2.CV_64F,0,1,ksize=3)
# sobely = cv2.convertScaleAbs(sobely)
# img = cv2.add(sobelx,sobely)
cv2.namedWindow('image')
cv2.createTrackbar('min','image',0,255,nothing)
cv2.createTrackbar('max','image',0,255,nothing)
cv2.imshow('image',img)
while(True):
    min = cv2.getTrackbarPos('min','image')
    max = cv2.getTrackbarPos('max','image')
    edges = cv2.Canny(img, min, max)
    cv2.imshow('canny',edges)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()    
