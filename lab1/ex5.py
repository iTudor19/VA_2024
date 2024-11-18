import cv2
from matplotlib import pyplot as plt

def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    
    center = (w // 2, h // 2)
    
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    
    rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))
    
    return rotated_image

image = cv2.imread('C:/Users/Tudor/Documents/GitHub/VA_2024/lab1/lena.tif')

rotated_clockwise_45 = rotate_image(image, -45)
rotated_counterclockwise_45 = rotate_image(image, 45)

rotated_clockwise_90 = rotate_image(image, -90)
rotated_counterclockwise_90 = rotate_image(image, 90)

titles = ['Original', 'Clockwise 45°', 'Counterclockwise 45°', 'Clockwise 90°', 'Counterclockwise 90°']
images = [image, rotated_clockwise_45, rotated_counterclockwise_45, rotated_clockwise_90, rotated_counterclockwise_90]

plt.figure(figsize=(12, 8))
for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis('off')

plt.show()

cv2.imwrite('lena_clockwise_45.tif', rotated_clockwise_45)
cv2.imwrite('lena_counterclockwise_45.tif', rotated_counterclockwise_45)
cv2.imwrite('lena_clockwise_90.tif', rotated_clockwise_90)
cv2.imwrite('lena_counterclockwise_90.tif', rotated_counterclockwise_90)
