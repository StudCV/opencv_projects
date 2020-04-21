import cv2
import numpy as np

gray = cv2.imread(r"C:\Users\happi\pics\6_2.png", cv2.IMREAD_REDUCED_GRAYSCALE_2)
img = cv2.imread(r"C:\Users\happi\pics\6_2.png", cv2.IMREAD_REDUCED_COLOR_2)
gray = 255 - gray
#lines = cv2.HoughLinesP(gray,1,np.pi/180,211,minLineLength=500,maxLineGap=2)
lines = cv2.HoughLines(gray, 0.5, np.pi/180, 400)
for i in range (np.size(lines, 0)):
    rho, theta = lines[i, 0]
    x0 = np.cos(theta) * rho
    y0 = np.sin(theta) * rho
    pt1 = int(x0 - 1000 * np.sin(theta)), int(y0 + 1000 * np.cos(theta))
    pt2 = int(x0 + 1000 * np.sin(theta)), int(y0 - 1000 * np.cos(theta))
    cv2.line(img, pt1, pt2, (255, 255, 255), 2)

cv2.imshow('houghlines3.jpg',img)
cv2.waitKey(0)