import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('C:/Users/Tudor/Documents/GitHub/VA_2024/lab1/lena.tif')

kernel_blur_5x5 = np.ones((5, 5), np.float32) / 25
kernel_blur_11x11 = np.ones((11, 11), np.float32) / 121

blur1 = cv2.filter2D(image, -1, kernel_blur_5x5)
blur2 = cv2.filter2D(image, -1, kernel_blur_11x11)

sharpen_kernel = np.array([[0, -1, 0],
                           [-1, 5,-1],
                           [0, -1, 0]])
sharpen1 = cv2.filter2D(image, -1, sharpen_kernel)

strong_sharpen_kernel = np.array([[1, -2, 1],
                                  [-2, 9,-2],
                                  [1, -2, 1]])
sharpen2 = cv2.filter2D(image, -1, strong_sharpen_kernel)

images = [image, blur1, blur2, sharpen1, sharpen2]
titles = ['Original', 'Kernel Blur (5x5)', 'Kernel Blur (11x11)', 'Sharpen 1', 'Strong Sharpen']

plt.figure(figsize=(10, 7))
for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis('off')
plt.show()

cv2.imwrite('kernel_blur_5x5.tif', blur1)
cv2.imwrite('kernel_blur_11x11.tif', blur2)
cv2.imwrite('sharpen1.tif', sharpen1)
cv2.imwrite('strong_sharpen.tif', sharpen2)
