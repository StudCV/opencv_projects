import cv2
import numpy as np

gray = cv2.imread(r"C:\Users\happi\pics\6_1.png", cv2.IMREAD_REDUCED_GRAYSCALE_2)
img = cv2.imread(r"C:\Users\happi\pics\6_1.png", cv2.IMREAD_REDUCED_COLOR_2)
gray = 255 - gray
minLineLength = 100
maxLineGap = 20
lines = cv2.HoughLinesP(gray, 1, np.pi/180, 10, minLineLength, maxLineGap)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2, 10)

max = 0
for i in range (np.size(lines, 0)):
    x1, y1, x2, y2 = lines[i, 0]
    dist = (x2 - x1)**2 + (y1 - y2)**2
    if(dist > max):
        max = dist
        x1m, y1m, x2m, y2m = x1, y1, x2, y2

maxr = 0
for i in range (np.size(circles, 0)):
    x0, y0, r = circles[i, 0]
    if(r > max):
        max = r
        x0m,y0m,r =  x0,y0,r
cv2.line(img, (x1m, y1m), (x2m, y2m), (0, 255, 0), 2)
cv2.circle(img, (x0, y0) ,r,(0, 0, 255), 2)
cv2.imshow('houghlines3.jpg', img)
cv2.waitKey(0)