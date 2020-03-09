import cv2
import numpy as np

img=cv2.imread(r"C:\Users\happi\pics\pic.jpg",cv2.IMREAD_COLOR)
cv2.imshow('RGB',img)
img_gray=cv2.imread(r"C:\Users\happi\pics\pic.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imwrite(r"C:\Users\happi\pics\pic_grey.jpg", img_gray)
cv2.imshow('Grayscale',img_gray)

img1_gray=cv2.imread(r"C:\Users\happi\pics\pic1.jpg",cv2.IMREAD_GRAYSCALE)
for i in range (np.size(img1_gray, 0)):    
    for j in range (np.size(img1_gray, 1)):
        img1_gray[i][j]=255-img1_gray[i][j]
cv2.imwrite(r"C:\Users\happi\pics\pic1_grey.jpg", img1_gray)
cv2.imshow('Grayscale1',img1_gray)

img1_rev=cv2.imread(r"C:\Users\happi\pics\pic1.jpg",cv2.IMREAD_COLOR)
img1_rev[:, :, [0, 1, 2]]=img1_rev[:, :, [0, 2, 1]]
cv2.imwrite(r"C:\Users\happi\pics\pic1_rev.jpg", img1_rev)
cv2.imshow('Reverse',img1_rev)

russia=np.ndarray(shape=(333, 666, 3))
for i in range (111):
    for j in range (666):
        russia[i][j]=[255, 255, 255]
for i in range (111, 222):
    for j in range (666):
        russia[i][j]=[255, 0, 0]
for i in range (222, 333):
    for j in range (666):
        russia[i][j]=[0, 0, 255]
cv2.imshow(r"C:\Users\happi\pics\russia.jpg", russia)
cv2.waitKey(0)