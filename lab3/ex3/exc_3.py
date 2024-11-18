import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def skin_detection_ycbcr_custom(image):
    r, g, b = image[:, :, 2], image[:, :, 1], image[:, :, 0]

    y = 0.299 * r + 0.587 * g + 0.114 * b
    cb = -0.1687 * r - 0.3313 * g + 0.5 * b + 128
    cr = 0.5 * r - 0.4187 * g - 0.0813 * b + 128

    skin_mask = (y > 80) & (cb > 85) & (cb < 135) & (cr > 135) & (cr < 180)

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

    binary_skin_image = skin_detection_ycbcr_custom(image)

    plt.imshow(binary_skin_image, cmap='gray')
    plt.title(f"Masca binara a pielii (YCbCr personalizat) pentru {image_file}")
    plt.show()
