import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./image/test.jpg')
#Import only if not previously imported

img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img1)
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([]) # 隐藏 X 和 Y 轴的刻度值
plt.show()
