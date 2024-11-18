import cv2
import numpy as np

width, height = 400, 400

zombie_face = np.ones((height, width, 3), dtype=np.uint8) * 255  #Fundal

cv2.rectangle(zombie_face, (100, 50), (300, 350), (60, 120, 30), -1)  #Cap

cv2.rectangle(zombie_face, (150, 100), (200, 150), (0, 0, 0), -1)  #Ochi stang
cv2.rectangle(zombie_face, (250, 100), (300, 150), (0, 0, 0), -1)  #Ochi drept

cv2.rectangle(zombie_face, (190, 180), (210, 220), (90, 140, 40), -1)  #Nas

cv2.rectangle(zombie_face, (150, 250), (250, 280), (100, 80, 40), -1)  #Gura

cv2.imshow("Zombie Emoji", zombie_face)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('zombie_emoji.png', zombie_face)
