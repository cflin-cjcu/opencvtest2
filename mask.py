import cv2

img = cv2.imread('./image/test.jpg',cv2.IMREAD_COLOR)
img2 = cv2.imread('./image/test2.png',cv2.IMREAD_COLOR)
print(img.shape, img.size)

roi1 = img[160:500, 100:330]

roi2 = img2[150:490,570:800]
roi2gray = cv2.cvtColor(roi2,cv2.COLOR_RGB2GRAY)
ret, mask = cv2.threshold(roi2gray,250,255,cv2.THRESH_BINARY_INV)
maskinv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi1,roi1,mask = maskinv)
img2_fg = cv2.bitwise_and(roi2,roi2,mask = mask)
roi = cv2.add(img1_bg,img2_fg)
img[160:500, 100:330] = roi
cv2.imshow('roi2gray',roi2gray)
cv2.imshow('mask',mask)
cv2.imshow('maskinv',maskinv)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img2_fg',img2_fg)
cv2.imshow('final',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
