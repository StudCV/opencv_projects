import cv2
import numpy as np

img = cv2.imread('/home/user/Documents/92-2/lab3/text_2.jpg', cv2.IMREAD_GRAYSCALE)

bin_threshold, bin_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
otsu_threshold, otsu_img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
tri_threshold, tri_img = cv2.threshold(img, 0, 255, cv2.THRESH_TRIANGLE)
mean_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 15)
gauss_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 15)
cv2.imshow('BINARY', bin_img)
cv2.imshow('OTSU', otsu_img)
cv2.imshow('TRIANGLE', tri_img)
cv2.imshow('MEAN', mean_img)
cv2.imshow('GAUSS', gauss_img)
cv2.waitKey(0)