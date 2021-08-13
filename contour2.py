import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('./image/car.jpg')
img = cv2.resize(img,(600,400))
img1 = cv2.GaussianBlur(img,(5,5),0)
gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 159, 255)
c, h = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for cnt in c:
    if cv2.contourArea(cnt) > 1000:
        # draw = cv2.drawContours(img,cnt,-1,(0,255,0),2)
        length = cv2.arcLength(cnt, True)
        epsilon = 0.01*length
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        draw = cv2.drawContours(img,approx,-1,(0,255,0),2)
        cv2.polylines(img, [approx], True, (0, 255, 0), 2)
# print(len(c))
# print(c[8].shape)
# print(h)
print(cv2.moments(c[8]))
# draw = cv2.drawContours(img,approx,-1,(0,255,0),2)
# cv2.polylines(img, [approx], True, (0, 255, 0), 3)

# dst = cv2.bitwise_and(img,img,mask=edges)
cv2.imshow('canny',edges)
cv2.imshow('contour',draw)
cv2.waitKey(0)
cv2.destroyAllWindows()

    
