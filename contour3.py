import cv2
import numpy as np
from matplotlib import pyplot as plt
font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.imread('./image/car.jpg')
img = cv2.resize(img,(600,400))
img1 = cv2.GaussianBlur(img,(5,5),0)
gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 159, 255)
c, h = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# for cnt in c:
#       print(cv2.contourArea(cnt))  
#     if cv2.contourArea(cnt) > 1000:
#         # draw = cv2.drawContours(img,cnt,-1,(0,255,0),2)
#         length = cv2.arcLength(cnt, True)
#         epsilon = 0.01*length
#         approx = cv2.approxPolyDP(cnt, epsilon, True)
#         draw = cv2.drawContours(img,approx,-1,(0,255,0),2)
#         cv2.polylines(img, [approx], True, (0, 255, 0), 2)
# # print(len(c))
# # print(c[8].shape)
# # print(h)
cnt1=c[8]
cnt2=c[14]
cnt= c[26]
# draw = cv2.drawContours(img,approx,-1,(0,255,0),2)
# cv2.polylines(img, [approx], True, (0, 255, 0), 3)
ellipse = cv2.fitEllipse(cnt)
(x, y), (a, b), angle = cv2.fitEllipse(cnt)
cv2.ellipse(img, ellipse, (0, 255, 0), 2)
text1 = 'x: ' + str(int(x)) + ' y: ' + str(int(y))
text2 = 'a:  ' + str(int(a)) + ' b:  ' + str(int(b))
text3 = 'angle: ' + str(round(angle, 2))
cv2.putText(img, text1, (10, 30), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)
cv2.putText(img, text2, (10, 60), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)
cv2.putText(img, text3, (10, 90), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)

# dst = cv2.bitwise_and(img,img,mask=edges)
cv2.imshow('canny',edges)
cv2.imshow('contour',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

    
