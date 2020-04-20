import cv2

img = cv2.imread('C:/Users/po/Desktop/img_2.jpg', cv2.IMREAD_REDUCED_COLOR_2)

sobel = cv2.Sobel(img, cv2.CV_8U, 1, 1, ksize = 3)
sobel_x = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize = 3)
sobel_y = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize = 3)
laplacian = cv2.Laplacian(img, cv2.CV_8U, ksize = 3)
blur = cv2.GaussianBlur(img, (5, 5), 0)
canny = cv2.Canny(blur, 0, 150, apertureSize = 3)

cv2.imshow('BLUR', blur)
cv2.imshow('SOBEL', sobel)
cv2.imshow('SOBEL X', sobel_x)
cv2.imshow('SOBEL Y', sobel_y)
cv2.imshow('LAPLACIAN', laplacian)
cv2.imshow('CANNY', canny)

cv2.waitKey(0)