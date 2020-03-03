import cv2 
import numpy as np

#Применение порогового фильтра к изображению (порог одинаковый
#для всех пикселей изображения, но вычисляется автоматически)
road1 = cv2.imread('lab4_1.jpg', cv2.IMREAD_GRAYSCALE)
maxVal1 = 255  
threshold1 = 100 #127 170 220
threshold1, road1_1 = cv2.threshold(road1, threshold1 ,maxVal1 , cv2.THRESH_OTSU)
cv2.imwrite(f"lab4_1_THRESH_OTSU_{threshold1}_{maxVal1}.jpg",road1_1)
threshold1, road1_1 = cv2.threshold(road1, threshold1 ,maxVal1 , cv2.THRESH_TRIANGLE)
cv2.imwrite(f"lab4_1_THRESH_TRIANGLE_{threshold1}_{maxVal1}.jpg",road1_1)