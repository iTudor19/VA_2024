import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def skin_detection_binary(image):
    r, g, b = image[:, :, 2], image[:, :, 1], image[:, :, 0]

    skin_mask = (r > 95) & (g > 40) & (b > 20) & \
                ((np.maximum(r, np.maximum(g, b)) - np.minimum(r, np.minimum(g, b))) > 15) & \
                (np.abs(r - g) > 15) & (r > g) & (r > b)

    binary_skin_image = np.zeros_like(r, dtype=np.uint8)
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

    binary_skin_image = skin_detection_binary(image)

    plt.imshow(binary_skin_image, cmap='gray')
    plt.title(f"Masca binara a pielii pentru {image_file}")
    plt.show()
