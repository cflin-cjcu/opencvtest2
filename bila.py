import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./image//test15.jpg')
img = cv2.resize(img,(800,600))

bila1 = cv2.bilateralFilter(img, 30, 200, 10)
bila2 = cv2.bilateralFilter(img, 30, 400, 10)

plt.subplot(131), plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)), plt.title('Original')
plt.subplot(132), plt.imshow(cv2.cvtColor(bila1,cv2.COLOR_BGR2RGB)), plt.title('bila1')
plt.subplot(133), plt.imshow(cv2.cvtColor(bila2,cv2.COLOR_BGR2RGB)), plt.title('bila2')
plt.show()