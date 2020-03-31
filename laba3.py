import cv2
import numpy as np
img = cv2.imread('/home/artem/Документы/laba3/RGB.jpeg', cv2.IMREAD_COLOR)
img_gr = cv2.imread('/home/artem/Документы/laba3/RGB.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('/home/artem/Документы/laba3/gray.jpeg', img_gr)
cv2.imshow('GRAYSCALE.jpeg', img_gr)
cv2.imshow('Color.jpeg', img)
img_gr2 = np.copy(img_gr)
img_gr2 = 255 - img_gr2
cv2.imshow('GRAYSCALE2.jpeg', img_gr2)
cv2.imwrite('/home/artem/Документы/laba3/gray_inv.jpeg', img_gr2)
img2 = np.copy(img)
#img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
#cv2.imshow('Color2.jpeg',img2)
#cv2.imwrite('/home/user/Documents/91-2/laba3/Color2.jpeg', img2)
red_to_gr = np.copy(img)
(c, d, e) = np.shape(red_to_gr)
for i in range(c):
    for j in range(d):
        g = red_to_gr[i][j][1]
        r = red_to_gr[i][j][2]
        red_to_gr[i][j][1] = r
        red_to_gr[i][j][2] = g
cv2.imshow('red_to_gr.jpeg', red_to_gr)
cv2.imwrite('/home/artem/Документы/laba3/red_to_gr.jpeg', red_to_gr)
cv2.waitKey(0)