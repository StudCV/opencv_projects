import cv2

color = cv2.imread('C:/Users/po/Desktop/img_2.jpg', cv2.IMREAD_REDUCED_COLOR_2)
gs = cv2.imread('C:/Users/po/Desktop/img_2.jpg', cv2.IMREAD_REDUCED_GRAYSCALE_2)

bin_thresh, thresh = cv2.threshold(gs, 50, 150, cv2.THRESH_BINARY)
contours1, hierarchy1 = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print('Number of contours (threshold): ' + str(len(contours1)))
blur = cv2.GaussianBlur(color, (5, 5), 0)
canny = cv2.Canny(blur, 50, 150, apertureSize = 3)
contours2, hierarchy2 = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print('Number of contours (canny): ' + str(len(contours2)))
cv2.drawContours(color, contours2, -1, (0, 0, 255), 1)

cv2.imshow('THRESHOLD', thresh)
cv2.imshow('CANNY', color)

cv2.waitKey(0)