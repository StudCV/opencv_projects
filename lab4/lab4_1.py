import cv2
import numpy as np

def threshold_bin(threshold):
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if img[x,y] > threshold:
                img[x,y] = 255
            else:
                img[x,y] = 0

img = cv2.imread('/home/user/Documents/92-2/lab3/img.jpg', cv2.IMREAD_GRAYSCALE)
threshold_bin(150)
cv2.imshow('BINARY', img)
cv2.waitKey(0)