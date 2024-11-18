import cv2
import numpy as np
import os
from sklearn.metrics import confusion_matrix, accuracy_score
import matplotlib.pyplot as plt


def detect_skin(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    
    return mask

folder_path = os.path.dirname(__file__)
image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]

for image_file in image_files:
    image = cv2.imread(os.path.join(folder_path, image_file))
    
    ground_truth_file = os.path.join(folder_path, image_file)
    ground_truth = cv2.imread(ground_truth_file, cv2.IMREAD_GRAYSCALE)
    
    if image is None:
        print(f"Nu am putut incarca imaginea {image_file}. Verifica calea fisierului.")
        continue
    if ground_truth is None:
        print(f"Nu am putut incarca imaginea de ground truth {image_file}. Verifica calea fisierului.")
        continue
    
    skin_detection = detect_skin(image)
    
    ground_truth_bin = (ground_truth > 128).astype(np.uint8)
    
    tp = np.sum((ground_truth_bin == 1) & (skin_detection == 255))
    tn = np.sum((ground_truth_bin == 0) & (skin_detection == 0))
    fp = np.sum((ground_truth_bin == 0) & (skin_detection == 255))
    fn = np.sum((ground_truth_bin == 1) & (skin_detection == 0))
    
    cm = np.array([[tp, fn], [fp, tn]])
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    
    print(f"Confusion Matrix for {image_file}:")
    print(cm)
    print(f"Accuracy: {accuracy:.4f}")
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(skin_detection, cmap='gray')
    plt.title('Skin Detection')
    plt.subplot(1, 2, 2)
    plt.imshow(ground_truth_bin, cmap='gray')
    plt.title('Ground Truth')
    plt.show()
