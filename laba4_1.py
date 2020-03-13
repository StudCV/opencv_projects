import cv2
import numpy
import random


def obrabotka(foto):
    cv2.imshow('icxodnik', foto)

    (temp_x , temp_y) = numpy.shape(foto)
    min = foto[1][1]
    max = foto[1][1]
    for i in range(0,temp_x):
        for ii in range(0,temp_y):
            if foto[i][ii] > max: 
                max = foto[i][ii] 
            elif foto[i][ii] < min:
                min = foto[i][ii]
    foto = (1 / 255) * (foto - min) * (255 / (max - min))
    cv2.imshow('pererabotannoe', foto)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


foto = cv2.imread('/home/user/Documents/91-2/laba4/LR_4_1.png',cv2.IMREAD_GRAYSCALE)
obrabotka(foto)
foto = cv2.imread('/home/user/Documents/91-2/laba4/LR_4_2.png',cv2.IMREAD_GRAYSCALE)
obrabotka(foto)
foto = cv2.imread('/home/user/Documents/91-2/laba4/LR_4_3.png',cv2.IMREAD_GRAYSCALE)
obrabotka(foto)


