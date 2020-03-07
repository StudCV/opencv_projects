import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('D:\doroga.jpg',0)
new_threshold, new_img = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
cv2.imshow('doroga', img)
img2= cv2.imread('D:\doc.jpg',0)
new_threshold, new_img = cv2.threshold(img,111,255,cv2.THRESH_BINARY)
cv2.imshow('doc', img2)
img3 = cv2.imread('D:\pop.jpg',0)
new_threshold, new_img = cv2.threshold(img,10,255,cv2.THRESH_BINARY)
cv2.imshow('text', img3)
cv2.waitKey(-1)
cv2.destroyAllWindows()