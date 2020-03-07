import cv2
import numpy
img = cv2.imread('D:\doby.jpg',cv2.IMREAD_COLOR)
img_gray = cv2.imread('D:\doby.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('rgb', img)
cv2.imshow('gray', img_gray)
cv2.imwrite('D:\doby_gray.jpg', img_gray)
img_gray2 = numpy.copy(img_gray)
for p in range (len(img_gray2)):
    img_gray2[p] = 255-img_gray2[p]
cv2.imshow('invert-gray', img_gray2)
cv2.imwrite('D:\doby_gray2.jpg', img_gray2)
img2 = numpy.copy(img)
for p in range (len(img2)):
    for z in range(1,3):
        img2[p][z] = img2[p][z]
cv2.imshow('invert-rgb', img2)
cv2.imwrite('D:\doby_2.jpg', img2)
cv2.waitKey(-1)
cv2.destroyAllWindows()