import cv2
from matplotlib import pyplot as plt

def crop_image(image, start_x, start_y, width, height):
    cropped_image = image[start_y:start_y + height, start_x:start_x + width]
    return cropped_image

image = cv2.imread('C:/Users/Tudor/Documents/GitHub/VA_2024/lab1/lena.tif')

start_x, start_y = 100, 100
width, height = 200, 150

cropped_image = crop_image(image, start_x, start_y, width, height)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Imagine Originala')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
plt.title(f'Decupata ({width}x{height}) de la ({start_x}, {start_y})')
plt.axis('off')

plt.show()

cv2.imwrite('lena_cropped.tif', cropped_image)
