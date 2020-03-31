import cv2
import numpy
img = cv2.imread('/home/artem/Документы/laba4/hm.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('before', img)
def fun(img,a):
    for i in range(len(img)):
        for j in range(len(img[i])):
            if img[i][j]>a:
                img[i][j]=255
            else: 
                img[i][j]=0
fun(img,200)
cv2.imshow('new' , img)
cv2.waitKey(0)