import cv2
import numpy as np

img = cv2.imread('/home/user/Documents/92-2/lab3/img.jpg', cv2.IMREAD_COLOR)
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        buf = img[x,y,1]
        img[x,y,1] = img[x,y,2]
        img[x,y,2] = buf
cv2.imshow('RED TO GREEN', img)
cv2.waitKey(0)