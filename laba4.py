import cv2
import numpy
img = cv2.imread('/home/user/Documents/TSUKVA6491/zadanie/tree.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('gray' , img)
def fun(img,a):
    for i in range(len(img)):
        for j in range(len(img[i])):
            if img[i][j]>a:
                img[i][j]=255
            else: 
                img[i][j]=0
fun(img,50)
cv2.imshow('gray2' , img)
cv2.waitKey(-1)