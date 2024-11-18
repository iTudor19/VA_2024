import cv2
import numpy as np

image = cv2.imread('C:/Users/Tudor/Documents/GitHub/VA_2024/lab2/lena.tif')

gray_image = (image[:, :, 0] / 3 + image[:, :, 1] / 3 + image[:, :, 2] / 3).astype(np.uint8)

cv2.imwrite('lena_grayscale_average.png', gray_image)
