import cv2
import numpy as np

img1=cv2.imread(r"C:\Users\happi\pics\pic1.jpg",cv2.IMREAD_COLOR)
cv2.imshow('RGB',img1)
img1_gray=cv2.imread(r"C:\Users\happi\pics\pic1.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imwrite(r"C:\Users\happi\pics\pic_grey.jpg", img1_gray)
cv2.imshow('Grayscale',img1_gray)

time1 = cv2.getTickCount()
#img1_gray = 255 - img1_gray
for i in range(563):
    for j in range(1024):
        img1_gray[i, j] = 255 - img1_gray[i, j]
time2 = cv2.getTickCount()
print(time2 - time1)

cv2.imwrite(r"C:\Users\happi\pics\pic1_grey.jpg", img1_gray)
cv2.imshow('Grayscale1',img1_gray)

img1_rev=cv2.imread(r"C:\Users\happi\pics\pic1.jpg",cv2.IMREAD_COLOR)
img1_rev[:, :, [0, 1, 2]]=img1_rev[:, :, [0, 2, 1]]
cv2.imwrite(r"C:\Users\happi\pics\pic1_rev.jpg", img1_rev)
cv2.imshow('Reverse',img1_rev)

russia=np.ndarray(shape=(333, 666, 3))
russia[0:111, :] = [255, 255, 255]
russia[111:222, :] = [255, 0, 0]
russia[222:333, :] = [0, 0, 255]

cv2.imshow('RUSSIA', russia)
cv2.waitKey(0)