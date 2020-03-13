import numpy as np
import cv2

dop = cv2.imread('Documents/91-Gog/lab4/LR_4_1.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('LR_4_1', dop)

dop1 = cv2.imread('Documents/91-Gog/lab4/LR_4_2.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('LR_4_2', dop1)

dop2 = cv2.imread('Documents/91-Gog/lab4/LR_4_3.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('LR_4_3', dop2)

cat = cv2.imread('Documents/91-Gog/lab4/cat.jpeg', cv2.IMREAD_GRAYSCALE)

a = dop[1][1]
b = dop[1][1]
(c, d) = np.shape(dop)
for i in range(0,c):
    if a < max(dop[i][:]):
        a = max(dop[i][:])
    if b > min(dop[i][:]):
        b = min(dop[i][:])

dop_new = (1 / 255) * (dop - b) * (255 / (a - b))

a1 = dop1[1][1]
b1 = dop1[1][1]
(c1, d1) = np.shape(dop1)
for i in range(0,c1):
    if a1 < max(dop1[i][:]):
        a1 = max(dop1[i][:])
    if b1 > min(dop1[i][:]):
        b1 = min(dop1[i][:])

dop1_new = (1 / 255) * (dop1 - b1) * (255 / (a1 - b1))

a2 = dop2[1][1]
b2 = dop2[1][1]
(c2, d2) = np.shape(dop2)
for i in range(0,c2):
    if a2 < max(dop2[i][:]):
        a2 = max(dop2[i][:])
    if b2 > min(dop2[i][:]):
        b2 = min(dop2[i][:])

dop2_new = (1 / 255) * (dop2 - b2) * (255 / (a2 - b2))

cv2.imshow('Dop_new', dop_new)
cv2.imshow('Dop1_new', dop1_new)
cv2.imshow('Dop2_new', dop2_new)

cv2.waitKey(-1)