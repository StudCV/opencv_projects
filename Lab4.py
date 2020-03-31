import cv2
import numpy as np
import math
a = input ("Ввведите порог:")
thresh = int(a)
bsize = input ("Ввведите blocksize:")
b = int(bsize)
const = input ("Ввведите константу С:")
c = int(const)

img1 = cv2.imread ('D:\doroga.jpg',0)
cv2.imshow('pic1',img1)
ret ,new_img1 = cv2.threshold( img1, thresh, 255, cv2.THRESH_BINARY)
cv2.imshow ('pic1_2',new_img1)
cv2.imwrite ('binary1.jpg',new_img1)

img2 = cv2.imread ('D:\doc.jpg',0)
cv2.imshow ('pic2',img2)
ret ,new_img2 = cv2.threshold (img2, thresh, 255, cv2.THRESH_BINARY)
cv2.imshow ('pic2_1',new_img2)
cv2.imwrite ('binary2.jpg',new_img2)

img3 = cv2.imread ('D:\pop.jpg',0)
cv2.imshow ('pic3',img3)
ret ,new_img3 = cv2.threshold(img3, thresh, 255, cv2.THRESH_BINARY)
cv2.imshow ('pic3_1',new_img3)
cv2.imwrite ('binary3.jpg',new_img3)

ret ,new_img4 = cv2.threshold( img1, thresh, 255, cv2.THRESH_OTSU)
cv2.imshow ('pic4',new_img4)
cv2.imwrite ('binary4.jpg',new_img4)

ret ,new_img5 = cv2.threshold (img2, thresh, 255, cv2.THRESH_OTSU)
cv2.imshow ('pic5',new_img5)
cv2.imwrite ('binary5.jpg',new_img5)

ret ,new_img6 = cv2.threshold(img3, thresh, 255, cv2.THRESH_OTSU)
cv2.imshow ('pic6',new_img6)
cv2.imwrite ('binary6.jpg',new_img6)

new_img7 = cv2.adaptiveThreshold(
img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
cv2.THRESH_BINARY, b, c)
cv2.imshow ('pic7',new_img7)
cv2.imwrite ('binary7.jpg',new_img7)

new_img8 = cv2.adaptiveThreshold(
img2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
cv2.THRESH_BINARY, b, c)
cv2.imshow ('pic8',new_img8)
cv2.imwrite ('binary8.jpg',new_img8)

new_img9 = cv2.adaptiveThreshold(
img3, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
cv2.THRESH_BINARY, b, c)
cv2.imshow ('pic9',new_img9)
cv2.imwrite ('binary9.jpg',new_img9)

cv2.waitKey(0)
