import cv2
import numpy as np
i = 0
def getP(event,x,y,flags,param):
    global i
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),5,(0,255,0),5)
        pts1[i]= [x,y]
        print(pts1[i])
        i += 1

cv2.namedWindow('img')
cv2.setMouseCallback('img',getP)
img = cv2.imread('./image/car.jpg')
pts1 = np.float32([[59,166],[514,59],[537,177],[103,325]])
pts2 = np.float32([[0,0],[400,0],[400,200],[0,200]])
cv2.imshow('img',img)
cv2.waitKey(0)
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(400,200))
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()