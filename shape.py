import cv2

def abc(x):
    pass

img = cv2.imread('./image/test.jpg',cv2.IMREAD_COLOR)
temp = img
img2 = cv2.imread('./image/test2.png',cv2.IMREAD_COLOR)
print(img.shape, img.size)
cv2.namedWindow('image')
cv2.createTrackbar('a','image',0,10,abc)
# img[:,:,1] = 0
# img[:,:,2] = 0

# roi = img[80:180,450:600]
roi1 = img[160:500, 100:330]
roi2 = img2[150:490,570:800]

while(True):
    img = temp 
    time1 = cv2.getTickCount()
    a = cv2.getTrackbarPos('a','image')
    roi = cv2.addWeighted(roi1,0.7,roi2,0.3,0)
    img[160:500, 100:330] = roi
    cv2.imshow('image',img)
    time2 = cv2.getTickCount()
    tt = (time2-time1) / cv2.getTickFrequency()
    cv2.putText(img,str(tt),(100,100),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),3)
    if cv2.waitKey(20) == 27:
        break 
cv2.destroyAllWindows()