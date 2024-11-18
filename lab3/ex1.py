import cv2
import numpy as np

image_names = ["1", "2", "3", "4", "5", "group", "group2", "hands3", "t26", "t27", "t63"]

lower_skin = np.array([0, 20, 70], dtype=np.uint8)
upper_skin = np.array([20, 255, 255], dtype=np.uint8)

for name in image_names:
    image_path = f"{name}.jpg"
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Image {name}.jpg not found.")
        continue

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    skin_mask = cv2.inRange(hsv_image, lower_skin, upper_skin)

    binary_skin_image = cv2.threshold(skin_mask, 127, 255, cv2.THRESH_BINARY)[1]

    output_path = f"binary_skin_{name}.jpg"
    cv2.imwrite(output_path, binary_skin_image)
    print(f"Processed and saved: {output_path}")

print("Processing complete for all images.")
