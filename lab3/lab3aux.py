import cv2
import numpy as np

#дополнительные
#флаг РФ
RFflag = np.empty((300, 200, 3))
for y in range(300):
    for x in range(200):
            if y<100:
                RFflag[y][x] = (255,255,255)
            elif y<200:
                RFflag[y][x] = (255,0,0) 
            else:
                RFflag[y][x] = (0,0,255) 
cv2.imshow('Rf flag' ,RFflag)


'''
#палитра
alpha_slider_max = 255
title_window = 'Linear Blend'

img = np.empty((200, 200, 3))

blue = 0

def on_trackbar(blue):
    print(blue)
    for y in range(200):
        for x in range(200):
            img[x][y][0] = blue
            img[x][y][1] = blue
            img[x][y][2] = blue
    cv2.imshow(title_window, img)

cv2.namedWindow(title_window)
trackbar_name = 'Blue'
cv2.createTrackbar(trackbar_name, title_window, 0,alpha_slider_max, on_trackbar )

# Show some stuff
#on_trackbar(0)

#cv2.imwrite('test.jpg',img )
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#cv2.imshow('inv',img[:,:,1])
#invert= np.copy(imggrey)
cv2.waitKey(0)

'''