import cv2
import numpy as np

img = cv2.imread('/home/user/Documents/92-2/lab3/img.jpg', cv2.IMREAD_GRAYSCALE)
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        img[x,y] = 255-img[x,y]
cv2.imshow('NEGATIVE', img)
cv2.waitKey(0)