import cv2
import numpy as np

img_color = cv2.imread("/home/artemon12/Documents/92-2/mazda626.jpg", IMREAD_COLOR)
img_black = cv2.imread("/home/artemon12/Documents/92-2/mazda626.jpg", IMREAD_COLOR)

cv2.imgshow("RGB", img_color)
cv2.imgshow("GRAYSCALE", img_black)

cv2.imwrite("/home/artemon12/Documents/92-2/mazda626_grayscale.jpg", img_black)

# revertion of image
img_reverted = np.copy(img_black)

for i in len(img_reverted):
    for j in len(i):
        img_reverted[i][j] = 255 - img_reverted[i][j]

cv2.imwrite("/home/artemon12/Documents/92-2/mazda626_reverted.jpg", img_reverted)

# changing of red and green channels
img_change_channels = np.copy(img_color)

for i in len(img_color):
    for j in len(i):
        val = img_color[i][j][0]
        img_color[i][j][0] = img_color[i][j][1]
        img_color[i][j][0] = val

cv2.imwrite("/home/artemon12/Documents/92-2/mazda626_change_channels.jpg", img_reverted)

# 

img_flag = np.zeros(300, 600, 3)

for i in img_flag:
    for j in i:
        j[0] = 255
        j[1] = 0
        j[2] = 0
