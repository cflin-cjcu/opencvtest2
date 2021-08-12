import cv2
# import numpy 

img = cv2.imread('./image/test.jpg')

cv2.line(img,(100,100),(300,300),(0,0,255),5)
cv2.rectangle(img,(200,100),(400,500),(0,255,0),3)
cv2.circle(img,(300,300),100,(255,0,0),6)
cv2.ellipse(img,(150,150),(100,50),45,0,180,(0,255,255),-1)
# pts = numpy.array([[10,5],[20,30],[70,20],[50,10]], numpy.int32)
# pts = pts.reshape((-1,1,2))
# cv2.polylines(img,[pts],True,(0,255,255))

cv2.putText(img,'OpenCV',(100,100),cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,255),3)

cv2.imshow('test',img)
cv2.waitKey(0)
cv2.destroyAllWindows()