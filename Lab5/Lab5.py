import cv2
import numpy as np

gray = cv2.imread(r"C:\Users\happi\pics\konosuba.png", cv2.IMREAD_REDUCED_GRAYSCALE_2)
color = cv2.imread(r"C:\Users\happi\pics\konosuba.png", cv2.IMREAD_REDUCED_COLOR_2)

sobel = cv2.Sobel(gray, cv2.CV_8U, 2, 2, ksize = 3)
lapl = cv2.Laplacian(gray, cv2.CV_8U, ksize = 3)
gray = cv2.blur(gray, (5, 5))
Canny1 = cv2.Canny(gray, 0, 100, apertureSize = 3)
Canny2 = cv2.Canny(gray, 0, 150, apertureSize = 3)
Canny3 = cv2.Canny(gray, 0, 200, apertureSize = 3)

binary_thresh, binary=cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
custom = np.ndarray(shape=[np.size(gray, 0), np.size(gray,1), 3], dtype=np.uint8)
custom2 = np.ndarray(shape=[np.size(gray, 0), np.size(gray,1), 3], dtype=np.uint8)
#custom = color;
custom2 = color;
contours, hierarchi = cv2.findContours(Canny1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours2, hierarchi2 = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(custom, contours, -1, color = (0, 0, 255), thickness = 1, lineType = cv2.LINE_4)
cv2.drawContours(custom2, contours2, -1, color = (0, 0, 255), thickness = 1, lineType = cv2.LINE_4)


cv2.imshow('Gray', gray)
cv2.imshow('Sobel', sobel)
cv2.imshow('Laplace', lapl)
cv2.imshow('Canny1', Canny1)
cv2.imshow('Canny2', Canny2)
cv2.imshow('Canny3', Canny3)
cv2.imshow('Contours', custom)
cv2.imshow('Contours2', custom2)
cv2.waitKey(0)