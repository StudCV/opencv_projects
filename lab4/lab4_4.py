import cv2 
import numpy as np

#адаптивного вычисления порога
road1 = cv2.imread('lab4_1.jpg', cv2.IMREAD_GRAYSCALE)
maxVal1 = 255  
threshold1 = 100 #127 170 220
blocksize = 21
C = 0.2

road1_1 = cv2.adaptiveThreshold(road1, maxVal1 , cv2.ADAPTIVE_THRESH_MEAN_C ,cv2.THRESH_BINARY , blocksize , C)
cv2.imwrite(f"lab4_1_ADAPTIVE_THRESH_MEAN_C__{threshold1}_{maxVal1}_{blocksize}_{C}.jpg",road1_1)

road1_1 = cv2.adaptiveThreshold(road1, maxVal1 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C ,cv2.THRESH_BINARY , blocksize , C)
cv2.imwrite(f"lab4_1_ADAPTIVE_THRESH_GAUSSIAN_C__{threshold1}_{maxVal1}_{blocksize}_{C}.jpg",road1_1)
