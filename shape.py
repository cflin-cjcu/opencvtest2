import cv2

img = cv2.imread('./image/test.jpg',cv2.IMREAD_COLOR)
img2 = cv2.imread('./image/test2.png',cv2.IMREAD_COLOR)
print(img.shape, img.size)

# img[:,:,1] = 0
# img[:,:,2] = 0

# roi = img[80:180,450:600]
roi1 = img[160:500, 100:330]
roi2 = img2[150:490,570:800]

for i in range(10):
    roi = cv2.addWeighted(roi1,0.1*i,roi2,1-0.1*i,0)
    img[160:500, 100:330] = roi
    cv2.imshow('test',img)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()