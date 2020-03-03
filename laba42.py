import cv2
import numpy 
img = cv2.imread('/home/user/Documents/TSUKVA6491/LR_4_3.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('gray' , img)
min1=255
max1=0
for i in range(len(img)):
    for j in range(len(img[i])):
             if min1>img[i][j]:
                 min1=img[i][j]
             if max1<img[i][j]:
                 max1=img[i][j]
for i in range(len(img)):
        for j in range(len(img[i])):
             a=(img[i][j]-min1)*255/(max1-min1)
             img[i][j]=a
cv2.imshow('gray2' , img)
cv2.waitKey(-1)