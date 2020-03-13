import cv2.cv2 as cv2
import numpy
#Чтение изображения в BGR
img = cv2.imread('D:/LAB_PYTHON/LAB_3/test.jpeg', cv2.IMREAD_COLOR)
#Чтение изображения в оттенках серого
img_gr = cv2.imread('D:/LAB_PYTHON/LAB_3/test.jpeg', cv2.IMREAD_GRAYSCALE)
#Открытие изображений в окнах и запись изображения в оттенках серого
cv2.imshow('RGB', img)
cv2.imshow('GRAYSCALE', img_gr)
cv2.imwrite('D:/LAB_PYTHON/LAB_3/test_gr.jpeg', img_gr)
#Инвертирование изображения в оттенках серого, вывод его на экран, и запись
img_gr2 = numpy.copy(img_gr)
img_gr2 = 255-img_gr2
cv2.imshow('INVERT_GRAYSCALE', img_gr2)
cv2.imwrite('D:/LAB_PYTHON/LAB_3/test_gr_inv.jpeg',img_gr2)
'''
Чтение изображения,
Замена местами значений красного и зеленого каналов,
Вывод результата на экран и его запись
'''
img2 = cv2.imread('D:/LAB_PYTHON/LAB_3/test_RGB.jpg', cv2.IMREAD_COLOR)
for i in range(len(img2)):
    for j in range(len(img2[i])):
        a = img2[i][j][1]
        img2[i][j][1] = img2[i][j][2]
        img2[i][j][2] = a
cv2.imshow('INVERT_BGR', img2)
cv2.imwrite('D:/LAB_PYTHON/LAB_3/test_BGR2BRG.jpg',img2)

cv2.waitKey(-1)
cv2.destroyAllWindows()