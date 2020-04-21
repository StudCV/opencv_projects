import cv2
import numpy as np

gray = cv2.imread(r"C:\Users\happi\pics\photo.jpg", cv2.IMREAD_REDUCED_GRAYSCALE_4)

#imgScale = 1
#newX,newY = gray.shape[1]*imgScale, gray.shape[0]*imgScale
#gray = cv2.resize(gray,(int(newX),int(newY))) 

binary_thresh, binary=cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY)
Otsu_thresh, Otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
triangle_thresh, triangle = cv2.threshold(gray, 0, 255, cv2.THRESH_TRIANGLE)
adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)
gauss = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 10)


cv2.imshow('Binary', binary)
cv2.imshow('Otsu', Otsu)
cv2.imshow('Triangle', triangle)
cv2.imshow('Adaptive', adaptive)
cv2.imshow('Gauss', gauss)
cv2.waitKey(0)