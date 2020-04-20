import cv2
from math import pi

img = cv2.imread('C:/Users/po/Desktop/circle.jpg', cv2.IMREAD_REDUCED_COLOR_2)

blur = cv2.GaussianBlur(img, (5, 5), 0)
canny = cv2.Canny(blur, 0, 150, apertureSize = 3)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print('Number of contours: ' + str(len(contours)))
cv2.drawContours(img, contours, 0, (0, 0, 255), 2)
cv2.drawContours(img, contours, 3, (0, 255, 0), 2)
outside = contours[0]
inside = contours[3]
print('Outside circle length: ' + str(cv2.arcLength(outside, True)))
print('Inside circle length: ' + str(cv2.arcLength(inside, True)))
print('Outside circle area: ' + str(cv2.contourArea(outside)))
print('Inside circle area: ' + str(cv2.contourArea(inside)))
x, y, w, h = cv2.boundingRect(outside)
cv2.rectangle(img, (x,y), (x + w, y + h), (255, 0, 0), 2)
print('Outside rectangle area: ' + str(w * h))
(x,y), radius = cv2.minEnclosingCircle(outside)
center = (int(x), int(y))
radius = int(radius)
cv2.circle(img, center, radius, (128, 128, 0), 2)
print('Outside enclosing circle area: ' + str(pi * (radius ** 2)))
x, y, w, h = cv2.boundingRect(inside)
cv2.rectangle(img, (x,y), (x + w, y + h), (0, 128, 128), 2)
print('Inside rectangle area: ' + str(w * h))
(x,y), radius = cv2.minEnclosingCircle(inside)
center = (int(x), int(y))
radius = int(radius)
cv2.circle(img, center, radius, (128, 128, 128), 2)
print('Inside enclosing circle area: ' + str(pi * (radius ** 2)))

cv2.imshow('CIRCLE', img)

cv2.waitKey(0)