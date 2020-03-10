import cv2
import numpy as np

img_color = cv2.imread("/home/user/Documents/92-2/lab3/mazda626.jpg", cv2.IMREAD_COLOR)
img_black = cv2.imread("/home/user/Documents/92-2/lab3/mazda626.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("RGB", img_color)
cv2.imshow("GRAYSCALE", img_black)

cv2.imwrite("/home/user/Documents/92-2/lab3/mazda626_grayscale.jpg", img_black)

# revertion of image
img_reverted = np.copy(img_black)
print(img_reverted[0][0])
for i in range(len(img_reverted)):
    #print(i)
    for j in range(len(img_reverted[i])):
        #print(j)
        img_reverted[i][j] = 255 - img_reverted[i][j]
        #print(img_reverted[i][j])

cv2.imwrite("/home/user/Documents/92-2/lab3/mazda626_reverted.jpg", img_reverted)

# changing of red and green channels
img_change_channels = np.copy(img_color)
for i in range(len(img_change_channels)):
    for j in range(len(img_change_channels[i])):

        val = img_change_channels[i, j, 2]
        img_change_channels[i, j, 2] = img_change_channels[i, j, 1]
        img_change_channels[i, j, 1] = val

cv2.imwrite("/home/user/Documents/92-2/lab3/mazda626_change_channels.jpg", img_change_channels)

# 

img_flag = np.zeros((300, 600, 3))


for i in range(len(img_flag)):
    if i <= 99:
        for j in range(len(img_flag[i])):
            img_flag[i,j,0] = 255
            img_flag[i,j,1] = 255
            img_flag[i,j,2] = 255
    elif 100 <= i <= 199:
        for j in range(len(img_flag[i])):
            img_flag[i,j,0] = 255
            img_flag[i,j,1] = 0
            img_flag[i,j,2] = 0
    elif i >= 200:
        for j in range(len(img_flag[i])):
            img_flag[i,j,0] = 0
            img_flag[i,j,1] = 0
            img_flag[i,j,2] = 255           

cv2.imwrite("/home/user/Documents/92-2/lab3/Motherland.jpg", img_flag)

img_rainbow = np.zeros((700, 1400, 3))

for i in range(len(img_rainbow)):
    if i <= 99:
        for j in range(len(img_rainbow[i])):
            img_rainbow[i,j,0] = 0
            img_rainbow[i,j,1] = 0
            img_rainbow[i,j,2] = 255
    elif 100 <= i <= 199:
        for j in range(len(img_rainbow[i])):
            img_rainbow[i,j,0] = 0
            img_rainbow[i,j,1] = 83
            img_rainbow[i,j,2] = 255
    elif 200 <= i <= 299:
        for j in range(len(img_rainbow[i])):
            img_rainbow[i,j,0] = 0
            img_rainbow[i,j,1] = 255
            img_rainbow[i,j,2] = 255 
    elif 300 <= i <= 399:
        for j in range(len(img_rainbow[i])):
            img_rainbow[i,j,0] = 0
            img_rainbow[i,j,1] = 255
            img_rainbow[i,j,2] = 0 
    elif 400 <= i <= 499:
        for j in range(len(img_rainbow[i])):
            img_rainbow[i,j,0] = 255
            img_rainbow[i,j,1] = 255
            img_rainbow[i,j,2] = 0        
    elif 500 <= i <= 599:
        for j in range(len(img_rainbow[i])):
            img_rainbow[i,j,0] = 255
            img_rainbow[i,j,1] = 0
            img_rainbow[i,j,2] = 0
    elif 600 <= i <= 699:
        for j in range(len(img_rainbow[i])):
            img_rainbow[i,j,0] = 64
            img_rainbow[i,j,1] = 0
            img_rainbow[i,j,2] = 64  
cv2.imwrite("/home/user/Documents/92-2/lab3/Artem'sflag.jpg", img_rainbow)

img_rainbownew = np.copy(img_rainbow)
for i in range(len(img_rainbownew)):
    for j in range(len(img_rainbownew[i])):

        val = img_rainbownew[i, j, 2]
        img_rainbownew[i, j, 2] = img_rainbownew[i, j, 1]
        img_rainbownew[i, j, 1] = val

cv2.imwrite("/home/user/Documents/92-2/lab3/Misha'sflag.jpg", img_rainbownew)

img_rainbownew2 = np.copy(img_rainbownew)
for i in range(len(img_rainbownew2)):
    for j in range(len(img_rainbownew2[i])):

        val = img_rainbownew2[i, j, 1]
        img_rainbownew2[i, j, 1] = img_rainbownew2[i, j, 2]
        img_rainbownew2[i, j, 2] = 0

cv2.imwrite("/home/user/Documents/92-2/lab3/Ruslans'sflag.jpg", img_rainbownew2)