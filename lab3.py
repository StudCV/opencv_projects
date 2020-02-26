import cv2
import numpy as np
img = cv2.imread('lab3.png', cv2.IMREAD_COLOR)
imggrey = cv2.imread('lab3.png', cv2.IMREAD_GRAYSCALE)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imwrite('testg.jpg',imggrey)
cv2.imwrite('test.jpg',img )
cv2.imshow('inv',img[:,:,1])

invert= np.copy(imggrey)
for i in range(len(imggrey)):
    imggrey[i] = abs(imggrey[i] - 255)
cv2.imwrite('testinv.jpg',imggrey)

cv2.imshow('GRAYSCALE' , imggrey)
cv2.imshow('NORM' ,img)

cv2.waitKey(20000)