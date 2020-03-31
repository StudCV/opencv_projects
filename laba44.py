import cv2
import numpy
img = cv2.imread('/home/artem/Документы/laba4/doc.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('before', img)
new_threshold, new_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('binary', new_img)


img = cv2.imread('/home/artem/Документы/laba4/doc.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('before', img)
new_threshold, new_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('binaryinv', new_img)


img = cv2.imread('/home/artem/Документы/laba4/doc.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('before', img)
new_threshold, new_img = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow('trunc', new_img)


img = cv2.imread('/home/artem/Документы/laba4/doc.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('before', img)
new_threshold, new_img = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow('tozero', new_img)

img = cv2.imread('/home/artem/Документы/laba4/doc.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('before', img)
new_threshold, new_img = cv2.threshold(img, 127, 255, cv2.THRESH_OTSU)
cv2.imshow('otsu', new_img)

img = cv2.imread('/home/artem/Документы/laba4/doc.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('before', img)
new_threshold, new_img = cv2.threshold(img, 127, 255, cv2.THRESH_TRIANGLE)
cv2.imshow('Triangle', new_img)

new_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11,9)
cv2.imshow('adaptb',new_img2)

new_img3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 9)
cv2.imshow('adptg',new_img3)

cv2.waitKey(0)