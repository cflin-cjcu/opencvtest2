import cv2

img = cv2.imread('./image/test.jpg',cv2.IMREAD_COLOR)
img2 = cv2.imread('./image/test2.png',cv2.IMREAD_COLOR)
print(img.shape, img.size)

# roi = img[80:180,450:600]
roi = img2[150:490,570:800]
img[160:500, 100:330] = roi

cv2.imshow('test',img)
cv2.waitKey(0)
cv2.destroyAllWindows()