import cv2 
import numpy as np

road1 = cv2.imread('lab4_1.jpg', cv2.IMREAD_GRAYSCALE)
        
new_threshold, new_img = cv2.threshold(img, threshold,maxVal, thresholdType)

cv2.imwrite('after_my_tresh_bin.jpg',THRESH_BINARY_MY(imggrey,127))