import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./image/car.jpg')
img = cv2.resize(img,(600,400))
img1 = cv2.GaussianBlur(img,(5,5),0)
gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

cv2.namedWindow('image')
cv2.imshow('image',img)
edges = cv2.Canny(gray, 159, 255)
c, h = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(len(c))
print(c[8].shape)
print(h)
draw = cv2.drawContours(img,c,8,(0,255,0),1)
# dst = cv2.bitwise_and(img,img,mask=edges)
plt.subplot(121), plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB)), plt.title('Canny')
plt.subplot(122), plt.imshow(cv2.cvtColor(draw, cv2.COLOR_BGR2RGB)), plt.title('contours')
plt.show()

    
