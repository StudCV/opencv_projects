import cv2
import numpy as np

gray = cv2.imread(r"C:\Users\happi\pics\circle.png", cv2.IMREAD_GRAYSCALE)
color = cv2.imread(r"C:\Users\happi\pics\circle.png", cv2.IMREAD_COLOR)

sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 1, ksize = 3)
lapl = cv2.Laplacian(gray, cv2.CV_8U, ksize = 3)
gray = cv2.blur(gray, (3, 3))
Canny1 = cv2.Canny(gray, 0, 100, apertureSize = 3)
Canny2 = cv2.Canny(gray, 0, 150, apertureSize = 3)
Canny3 = cv2.Canny(gray, 0, 200, apertureSize = 3)

binary_thresh, binary=cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
custom = np.ndarray(shape=[np.size(gray, 0), np.size(gray,1), 3], dtype=np.uint8)
custom2 = np.ndarray(shape=[np.size(gray, 0), np.size(gray,1), 3], dtype=np.uint8)
custom = color;
contours, hierarchi = cv2.findContours(Canny1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours2, hierarchi2 = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

length = cv2.arcLength(contours[0], 1)
area = cv2.contourArea(contours[0])
rect = cv2.boundingRect(contours[0])
rectarea = rect[2] * rect[3]
circle = cv2.minEnclosingCircle(contours[0])
circlearea = np.pi * circle[1]**2
print('length0 =', length)
print('area0 =', area)
print('rectarea0 =', rectarea)
print('circlearea0 =', circlearea)
length = cv2.arcLength(contours[2], 1)
area = cv2.contourArea(contours[2])
rect = cv2.boundingRect(contours[2])
rectarea = rect[2] * rect[3]
circle = cv2.minEnclosingCircle(contours[2])
circlearea = np.pi * circle[1]**2
print('length2 =', length)
print('area2 =', area)
print('rectarea2 =', rectarea)
print('circlearea2 =', circlearea)

cv2.drawContours(custom, contours, 2, color = (0, 228, 0), thickness = 2, lineType = cv2.LINE_4)
cv2.drawContours(custom, contours, 0, color = (0, 87, 205), thickness = 2, lineType = cv2.LINE_4)


cv2.imshow('Gray', gray)
cv2.imshow('Sobel', sobel)
cv2.imshow('Laplace', lapl)
cv2.imshow('Canny1', Canny1)
cv2.imshow('Canny2', Canny2)
cv2.imshow('Canny3', Canny3)
cv2.imshow('Contours Canny', custom)
cv2.imshow('Contours Binary', custom2)
cv2.waitKey(0)