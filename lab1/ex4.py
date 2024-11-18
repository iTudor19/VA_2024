import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('C:/Users/Tudor/Documents/GitHub/VA_2024/lab1/lena.tif')

kernel_w = np.array([[0, -2, 0],
                     [-2, 8, -2],
                     [0, -2, 0]])

filtered_image = cv2.filter2D(image, -1, kernel_w)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Imagine Originală')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB))
plt.title('Imagine Filtrată (kernel w)')
plt.axis('off')

plt.show()

cv2.imwrite('lena_filtered_w.tif', filtered_image)
