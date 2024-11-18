import cv2
import numpy as np

image = cv2.imread('C:/Users/Tudor/Documents/GitHub/VA_2024/lab2/lena.tif')

gray_image = (0.3 * image[:, :, 2] + 0.59 * image[:, :, 1] + 0.11 * image[:, :, 0]).astype(np.uint8)

p = 3

equal_intervals = True
if equal_intervals:
    a_values = np.linspace(0, 255, p+1).astype(int)
else:
    a_values = np.sort(np.random.choice(range(1, 255), p - 1, replace=False))
    a_values = np.insert(a_values, 0, 0)
    a_values = np.append(a_values, 255)

quantized_image = np.zeros_like(gray_image)

for i in range(1, len(a_values)):
    interval_mask = (gray_image >= a_values[i - 1]) & (gray_image < a_values[i])
    mean_value = int((a_values[i - 1] + a_values[i]) / 2)
    quantized_image[interval_mask] = mean_value

cv2.imwrite('lena_grayscale_custom_shades_2.png', quantized_image)
