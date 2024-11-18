import cv2
import numpy as np

image = cv2.imread('C:/Users/Tudor/Documents/GitHub/VA_2024/lab2/lena.tif')

max_gray_image = np.max(image, axis=2).astype(np.uint8)
min_gray_image = np.min(image, axis=2).astype(np.uint8)

cv2.imwrite('lena_grayscale_max_decomposition.png', max_gray_image)
cv2.imwrite('lena_grayscale_min_decomposition.png', min_gray_image)
