import cv2

image = cv2.imread('C:/Users/Tudor/Documents/GitHub/VA_2024/lab2/lena.tif')

gray_r = image[:, :, 2]#R
gray_g = image[:, :, 1]#G
gray_b = image[:, :, 0]#B

cv2.imwrite('lena_grayscale_red_channel.png', gray_r)
cv2.imwrite('lena_grayscale_green_channel.png', gray_g)
cv2.imwrite('lena_grayscale_blue_channel.png', gray_b)
