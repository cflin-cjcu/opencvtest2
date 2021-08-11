import cv2

img = cv2.imread('./image/test.jpg',cv2.IMREAD_COLOR)
print(img.shape, img.size)

roi = img[80:180,450:600]
img[400:500, 300:450] = roi

cv2.imshow('test',img)
cv2.waitKey(0)
cv2.destroyAllWindows()