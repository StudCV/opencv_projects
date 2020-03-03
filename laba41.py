import cv2
import numpy 
img = cv2.imread('/home/user/Documents/TSUKVA6491/text2.jpg', cv2.IMREAD_GRAYSCALE)
new_threshold, new_img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
new_threshold, new_img1 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)
new_threshold, new_img2 = cv2.threshold(img, 230, 255, cv2.THRESH_TRUNC)
new_threshold, new_img3 = cv2.threshold(img, 170, 255, cv2.THRESH_TOZERO)
new_img5 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,101 ,50)
'''cv2.imwrite('/home/user/Documents/TSUKVA6491/cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,101 ,50).jpg',new_img5)'''
cv2.imshow('GRAYSCALE' , new_img)
cv2.imshow('GRAYSCALE1' , new_img1)
cv2.imshow('GRAYSCALE2' , new_img2)
cv2.imshow('GRAYSCALE3' , new_img3)
cv2.imshow('GRAYSCALE5' , new_img5)
cv2.waitKey(-1)