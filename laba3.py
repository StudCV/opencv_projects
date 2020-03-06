import cv2
import numpy
import random

#первое задание
#foto = cv2.imread('/home/user/Documents/91-2/laba3/picture.jpg',cv2.IMREAD_COLOR)
#cv2.imshow('RGB', foto)
#cv2.waitKey(0)
#foto1 = cv2.imread('/home/user/Documents/91-2/laba3/picture.jpg',cv2.IMREAD_GRAYSCALE)
#cv2.imshow('GRAYSCALE', foto1)
#cv2.waitKey(0)
#cv2.imwrite('/home/user/Documents/91-2/laba3/picture1.jpg', foto1)

#второе задание
#foto2 = cv2.imread('/home/user/Documents/91-2/laba3/picture1.jpg')
#for i in range(0,1000):
#    for ii in range(0,1600):
#        foto2[i][ii]=255-foto2[i][ii]    
#cv2.imshow('ky',foto2)
#cv2.waitKey(0)
#cv2.imwrite('/home/user/Documents/91-2/laba3/picture2.jpg', foto2)

#третье задание
#foto3 = cv2.imread('/home/user/Documents/91-2/laba3/picture.jpg',cv2.IMREAD_COLOR)
#for i in range(0,1000):
#    for ii in range(0,1600):
#        foto3[i][ii][1] , foto3[i][ii][2] = foto3[i][ii][2] , foto3[i][ii][1]
#cv2.imshow('ky1',foto3)
#cv2.waitKey(0)
#cv2.imwrite('/home/user/Documents/91-2/laba3/picture3.jpg', foto3)

#первое дополнительное задание 
#max = numpy.zeros((900, 1600, 3))
#for i in range(0,1200):
#    for ii in range(0,1600):
#        if i<300:
#            max[i][ii][0] = 255
#            max[i][ii][1] = 255
#            max[i][ii][2] = 255
#        elif i>=300 and i<600:
#            max[i][ii][0] = 255
#            max[i][ii][1] = 0
#            max[i][ii][2] = 0
#        elif i>=600 and i<900:
#            max[i][ii][0] = 0
#            max[i][ii][1] = 0
#            max[i][ii][2] = 255
#cv2.imshow('ky2',max)
#cv2.waitKey(0) 
#cv2.imwrite('/home/user/Documents/91-2/laba3/picture4.jpg', max)           

#второе дополнительное задание  первый подпункт
#max_max = numpy.zeros((900, 1600, 3))
#for i in range(0,1200):
#    for ii in range(0,1600):
#        if i<300:
#            max_max[i][ii][0] = 0
#            max_max[i][ii][1] = 255
#            max_max[i][ii][2] = 0
#        elif i>=300 and i<600:
#            max_max[i][ii][0] = 255
#            max_max[i][ii][1] = 0
#            max_max[i][ii][2] = 0
#        elif i>=600 and i<900:
#            max_max[i][ii][0] = 0
#            max_max[i][ii][1] = 0
#            max_max[i][ii][2] = 255
#cv2.imshow('ky3',max_max)
#cv2.waitKey(0) 

#второе дополнительное задание  второй подпункт 
max_max_max = numpy.zeros((600, 600, 3))
while(True):
    R=random.random()
    B=random.random()
    G=random.random()
    for i in range(0,600):
        for ii in range(0,600):
                max_max_max[i][ii][0] = B
                max_max_max[i][ii][1] = G
                max_max_max[i][ii][2] = R
    print('R=', int(255*max_max_max[i][ii][2]),' ','G=', int(255*max_max_max[i][ii][1]),' ','B=', int(255*max_max_max[i][ii][0]) ) 
    cv2.imshow('ky4',max_max_max)
    cv2.waitKey(1000)    
