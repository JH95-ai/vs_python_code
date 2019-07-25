import numpy as np
import pandas as pd
import cv2
from scipy import ndimage

#滤波器矩阵
kernel_3x3 = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])

kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
                       [-1,  1,  2,  1, -1],
                       [-1,  2,  4,  2, -1],
                       [-1,  1,  2,  1, -1],
                       [-1, -1, -1, -1, -1]])

img = cv2.imread("E:/Download/VOC2012/VOC2012/JPEGImages/2007_000027.jpg", 0)

k3 = ndimage.convolve(img, kernel_3x3)
k5 = ndimage.convolve(img, kernel_5x5)

#高斯模糊滤波
blurred = cv2.GaussianBlur(img, (17,17), 0)
g_hpf = img - blurred

# cv2.imshow('blurred', blurred)
# cv2.imshow("g_hpf", g_hpf)

cv2.imshow("img", img)
cv2.imshow("3x3", k3)
cv2.imshow("5x5", k5)
cv2.imshow("g_hpf", g_hpf)
cv2.waitKey()
cv2.destroyAllWindows()