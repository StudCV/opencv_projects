import cv2
import numpy as np
import math

gray=cv2.imread(r"C:\Users\happi\pics\LR_4_3.png",cv2.IMREAD_GRAYSCALE)
gray2=np.ndarray(shape=[np.size(gray,0), np.size(gray,1)], dtype=np.uint8)
max=np.max(gray)
min=np.min(gray)
gray2=np.uint8(((gray-min) / (max - min) * 255))
cv2.imshow('Gray', gray)
cv2.imshow('Gray2', gray2)
cv2.waitKey(0)