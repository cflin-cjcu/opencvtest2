import cv2

img = cv2.imread('./image/test2.png',0)
roi = img[144:500,560:800]

# sobelx = cv2.Sobel(roi,cv2.CV_8U,1,0,ksize=3)
sobelx = cv2.Sobel(roi, cv2.CV_64F,1,0,ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)
# sobely = cv2.Sobel(roi,cv2.CV_8U,0,1,ksize=3)
sobely = cv2.Sobel(roi, cv2.CV_64F, 0,1, ksize=3)
sobely = cv2.convertScaleAbs(sobely)

sobel = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
sobel1 = cv2.add(sobelx,sobely)
cv2.imshow('roi',roi)
cv2.imshow('sobelx',sobelx)
cv2.imshow('sobely',sobely)
cv2.imshow('sobel',sobel)
cv2.imshow('sobel_Add',sobel1)
cv2.waitKey(0)
cv2.destroyAllWindows()