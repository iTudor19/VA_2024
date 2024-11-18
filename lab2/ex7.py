import numpy as np
import cv2

def apply_threshold(value):
    return 0 if value < 128 else 255

def floyd_steinberg_dithering(image):
    image = image.astype(np.float32)
    height, width = image.shape

    fs_matrix = np.array([
        [0, 0, 7/16],
        [3/16, 5/16, 1/16]
    ])
    fs_offsets = [(0, 1), (1, -1), (1, 0), (1, 1)]

    for y in range(height - 1):
        for x in range(1, width - 1):
            old_pixel = image[y, x]
            new_pixel = apply_threshold(old_pixel)
            image[y, x] = new_pixel
            error = old_pixel - new_pixel

            for (dy, dx), weight in zip(fs_offsets, fs_matrix.flatten()):
                ny, nx = y + dy, x + dx
                if 0 <= nx < width and 0 <= ny < height:
                    image[ny, nx] += error * weight

    return np.clip(image, 0, 255).astype(np.uint8)

def stucki_dithering(image):
    image = image.astype(np.float32)
    height, width = image.shape

    stucki_matrix = np.array([
        [0, 0, 0, 8/42, 4/42],
        [2/42, 4/42, 8/42, 4/42, 2/42],
        [1/42, 2/42, 4/42, 2/42, 1/42]
    ])
    stucki_offsets = [
        (0, 3), (1, -2), (1, -1), (1, 0), (1, 1), (1, 2),
        (2, -2), (2, -1), (2, 0), (2, 1), (2, 2)
    ]

    for y in range(height - 2):
        for x in range(2, width - 2):
            old_pixel = image[y, x]
            new_pixel = apply_threshold(old_pixel)
            image[y, x] = new_pixel
            error = old_pixel - new_pixel

            for (dy, dx), weight in zip(stucki_offsets, stucki_matrix.flatten()):
                ny, nx = y + dy, x + dx
                if 0 <= nx < width and 0 <= ny < height:
                    image[ny, nx] += error * weight

    return np.clip(image, 0, 255).astype(np.uint8)

image = cv2.imread("C:/Users/Tudor/Documents/GitHub/VA_2024/lab2/lena.tif", cv2.IMREAD_GRAYSCALE)

floyd_steinberg_image = floyd_steinberg_dithering(image)
cv2.imwrite("floyd_steinberg_dithered.png", floyd_steinberg_image)

stucki_image = stucki_dithering(image)
cv2.imwrite("stucki_dithered.png", stucki_image)
