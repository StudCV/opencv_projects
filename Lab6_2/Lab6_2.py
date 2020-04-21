import cv2
import numpy as np

gray = cv2.imread(r"C:\Users\happi\pics\6_2.png", cv2.IMREAD_REDUCED_GRAYSCALE_2)
img = cv2.imread(r"C:\Users\happi\pics\6_2.png", cv2.IMREAD_REDUCED_COLOR_2)
gray = 255 - gray
lines = cv2.HoughLinesP(gray,1,np.pi/180,212,minLineLength=500,maxLineGap=2)
for i in range (np.size(lines, 0)):
    x1,y1,x2,y2 = lines[i, 0]
    cv2.line(img,(x1,y1),(x2,y2),(255,255,255))

cv2.imshow('houghlines3.jpg',img)
cv2.waitKey(0)
