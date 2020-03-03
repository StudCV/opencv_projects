import cv2
import numpy as np
img = cv2.imread('lab3.png', cv2.IMREAD_COLOR)
imggrey = cv2.imread('lab3.png', cv2.IMREAD_GRAYSCALE)

#1
cv2.imshow('BGR' ,img)
cv2.imshow('GRAYSCALE' , imggrey)
cv2.imwrite('testg.jpg',imggrey)

#Для каждого пикселя инвертируйте его значение 
height,width = imggrey.shape
for y in range(height):
    for x in range(width):
        imggrey[y][x] =  255 - imggrey[y][x]
cv2.imwrite('testinv.jpg',imggrey)

#Поменяйте местами значения красного и зеленого каналов.
for y in range(height):
    for x in range(width):
        img[y][x][1],img[y][x][2] =  img[y][x][2],img[y][x][1]
cv2.imwrite('test3.jpg',img)
        
cv2.waitKey(0)
