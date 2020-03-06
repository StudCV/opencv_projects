import numpy as np
import cv2

rus_flag = np.zeros((600, 1200,3))
for i in range(0,200):
    for j in range(0,1200):
        rus_flag[i][j][0] = 255
        rus_flag[i][j][1] = 255
        rus_flag[i][j][2] = 255
for i in range(200,400):
    for j in range(0,1200):
        rus_flag[i][j][0] = 255
        rus_flag[i][j][1] = 0
        rus_flag[i][j][2] = 0

for i in range(400,600):
    for j in range(0,1200):
        rus_flag[i][j][0] = 0
        rus_flag[i][j][1] = 0
        rus_flag[i][j][2] = 255        
cv2.imshow('RUS_FLAG', rus_flag)
cv2.waitKey(-1)
cv2.imwrite('Documents/91-Gog/lab3/rus_flag.jpeg', rus_flag)