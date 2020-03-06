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

#np.arange(48).reshape(4, 3, 4)
rus_flag = np.zeros((600, 1200,3))
for i in range(0,200):
    for j in range(0,1200):
        rus_flag[i][j][0] = 255
        rus_flag[i][j][1] = 255
        rus_flag[i][j][2] = 255
for i in range(200,400):
    for j in range(0,1200):
        rus_flag[i][j][0] = 255
        rus_flag[i][j][1] = 0
        rus_flag[i][j][2] = 0

for i in range(400,600):
    for j in range(0,1200):
        rus_flag[i][j][0] = 0
        rus_flag[i][j][1] = 0
        rus_flag[i][j][2] = 255        
cv2.imshow('RUS_FLAG', rus_flag)
cv2.imwrite('Documents/91-Gog/lab3/rus_flag.jpeg', rus_flag)

experiment = np.zeros((600, 1200,3))
for i in range(0,200):
    for j in range(0,400):
        experiment[i][j][0] = 150/255
        experiment[i][j][1] = 62/255
        experiment[i][j][2] = 1
    for j in range(400,800):
        experiment[i][j][0] = 86/255
        experiment[i][j][1] = 114/255
        experiment[i][j][2] = 1
    for j in range(800,1200):
        experiment[i][j][0] = 144/255
        experiment[i][j][1] = 238/255
        experiment[i][j][2] = 144/255
for i in range(200,400):
    for j in range(0,400):
        experiment[i][j][0] = 205/255
        experiment[i][j][1] = 92/255
        experiment[i][j][2] = 92/255
    for j in range(400,800):
        experiment[i][j][0] = 127/255
        experiment[i][j][1] = 1
        experiment[i][j][2] = 212/255
    for j in range(800,1200):
        experiment[i][j][0] = 29/255
        experiment[i][j][1] = 102/255
        experiment[i][j][2] = 205/255
for i in range(400,600):
    for j in range(0,400):
        experiment[i][j][0] = 0
        experiment[i][j][1] = 139/255
        experiment[i][j][2] = 139/255

cv2.imshow('Experiment', experiment)
experiment[:][:] = experiment[:][:]*255
cv2.imwrite('Documents/91-Gog/lab3/experiment.jpeg', experiment)
cv2.waitKey(-1)