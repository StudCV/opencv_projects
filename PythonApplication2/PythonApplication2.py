import cv2
import numpy as np

def light_binary(img, threshold=128, maxVal=255):
    img_binary=np.ndarray(shape=(np.size(img, 0), np.size(img, 1)))
    for i in range (np.size(img, 0)):
        for j in range ((np.size(img, 1))):
            if(img[i, j]>threshold):
                img_binary[i, j]=maxVal
            else: img_binary[i, j]=0
    return img_binary
img_gray=cv2.imread(r"C:\Users\happi\pics\pic.jpg",cv2.IMREAD_GRAYSCALE)
img_gray_binary=light_binary(img_gray)
cv2.imwrite(r"C:\Users\happi\pics\pic_grey_binary.jpg", img_gray_binary)
cv2.imshow('Grayscale',img_gray)
cv2.imshow('Binary',img_gray_binary)
cv2.waitKey(0)