import cv2 
import numpy as np

imggrey = cv2.imread('lab4_1.jpg', cv2.IMREAD_GRAYSCALE)

def THRESH_BINARY_MY(img,threshold):
    height,width = img.shape
    for y in range(height):
        for x in range(width):
            if img[y][x]>threshold:
                img[y][x]=255
            else:
                img[y][x]=0
    return img

cv2.imwrite("lab4_1_after_my_tresh_bin_170_255.jpg",THRESH_BINARY_MY(imggrey,170))

        
cv2.waitKey(0)