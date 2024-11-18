import cv2
import numpy as np

image = cv2.imread('C:/Users/Tudor/Documents/GitHub/VA_2024/lab2/lena.tif')

gray_image = (0.3 * image[:, :, 2] + 0.59 * image[:, :, 1] + 0.11 * image[:, :, 0]).astype(np.uint8)

cv2.imwrite('lena_grayscale_weighted_average.png', gray_image)
