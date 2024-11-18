import cv2
import numpy as np

image = cv2.imread('C:/Users/Tudor/Documents/GitHub/VA_2024/lab2/lena.tif')

min_channel = np.min(image, axis=2)
max_channel = np.max(image, axis=2)
gray_image = ((min_channel + max_channel) / 2).astype(np.uint8)

cv2.imwrite('lena_grayscale_desaturation.png', gray_image)
