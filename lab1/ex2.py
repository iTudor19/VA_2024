import cv2
from matplotlib import pyplot as plt

image = cv2.imread('C:/Users/Tudor/Documents/GitHub/VA_2024/lab1/lena.tif')

print(f"Dimensiunile imaginii: {image.shape}")

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Imaginea Lena')
plt.show()

cv2.imwrite('lena_output.tif', image)
