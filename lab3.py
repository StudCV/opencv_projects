import numpy as np
import cv2
img = cv2.imread('Documents/91-Gog/lab3/cat.jpeg', cv2.IMREAD_COLOR)
cv2.imshow('RGB', img)
img_gray = cv2.imread('Documents/91-Gog/lab3/cat.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('GRAYSCALE', img_gray)
cv2.imwrite('Documents/91-Gog/lab3/cat_gray.jpeg', img_gray)
img_gray_inv = np.copy(img_gray)
(a, b) = np.shape(img_gray_inv)
for i in range(0,a):
    for j in range(0,b):
        img_gray_inv[i][j] = 255 - img_gray_inv[i][j]
cv2.imshow('GRAYSCALE_INV', img_gray_inv)
cv2.imwrite('Documents/91-Gog/lab3/cat_gray_inv.jpeg', img_gray_inv)
img_red_to_green = np.copy(img)
(c, d, e) = np.shape(img_red_to_green)
for i in range(0,c):
    for j in range(0,d):
        g = img_red_to_green[i][j][1]
        r = img_red_to_green[i][j][2]
        img_red_to_green[i][j][1] = r
        img_red_to_green[i][j][2] = g
cv2.imshow('RED_TO_GREEN', img_red_to_green)
cv2.imwrite('Documents/91-Gog/lab3/cat_red_to_green.jpeg', img_red_to_green)

img1 = cv2.imread('Documents/91-Gog/lab3/cat1.jpeg', cv2.IMREAD_COLOR)
img_red_to_green_2 = np.copy(img1)
(c1, d1, e1) = np.shape(img1)
for i in range(0,c1):
    for j in range(0,d1):
        g = img_red_to_green_2[i][j][1]
        r = img_red_to_green_2[i][j][2]
        img_red_to_green_2[i][j][1] = r
        img_red_to_green_2[i][j][2] = g

cv2.imshow('RGB_2', img1)
cv2.imshow('RED_TO_GREEN_2', img_red_to_green_2)
cv2.imwrite('Documents/91-Gog/lab3/cat1_red_to_green_2.jpeg', img_red_to_green_2)

cv2.waitKey(-1)