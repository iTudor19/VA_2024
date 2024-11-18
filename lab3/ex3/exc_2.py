import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def skin_detection_hsv(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_image)

    s = s / 255.0
    v = v / 255.0

    skin_mask = (h >= 0) & (h <= 50) & (s >= 0.23) & (s <= 0.68) & (v >= 0.35) & (v <= 1.0)

    binary_skin_image = np.zeros_like(h, dtype=np.uint8)
    binary_skin_image[skin_mask] = 255

    return binary_skin_image

folder_path = os.path.dirname(__file__)
image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]

for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    image = cv2.imread(image_path)

    if image is None:
        print(f"Nu s-a putut încarca imaginea {image_file}. Verifica calea fisierului.")
        continue

    binary_skin_image = skin_detection_hsv(image)

    plt.imshow(binary_skin_image, cmap='gray')
    plt.title(f"Masca binara a pielii (HSV) pentru {image_file}")
    plt.show()
