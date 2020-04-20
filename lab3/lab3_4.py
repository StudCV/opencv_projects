import cv2
import numpy as np

img = np.zeros((240,400,3), np.uint8)
for y in range(400):
    for x in range(0,80):
        img[x,y] = [255, 255, 255]
    for x in range(81,160):
        img[x,y] = [255, 0 ,0]
    for x in range(161,240):
        img[x,y] = [0, 0 ,255]
cv2.imshow('RUSSIA', img)
cv2.waitKey(0)