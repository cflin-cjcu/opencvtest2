import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./image/test.jpg')
G0=img
G1 = cv2.pyrDown(G0)
G2 = cv2.pyrDown(G1)
G3 = cv2.pyrDown(G2)
L0 = G0 - cv2.pyrUp(G1)
L1 = G1 - cv2.pyrUp(G2)
L2 = G2 - cv2.pyrUp(G3)

# plt.subplot(131), plt.imshow(cv2.cvtColor(L0, cv2.COLOR_BGR2RGB)), plt.title('L0')
# plt.subplot(132), plt.imshow(cv2.cvtColor(L1, cv2.COLOR_BGR2RGB)), plt.title('L1')
# plt.subplot(133), plt.imshow(cv2.cvtColor(L2, cv2.COLOR_BGR2RGB)), plt.title('L2')

cv2.imshow('L0',L0)
cv2.imshow('L1',L1)
cv2.imshow('L2',L2)
cv2.waitKey(0)
cv2.destroyAllWindows()