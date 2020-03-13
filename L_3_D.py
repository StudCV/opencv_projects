import cv2.cv2 as cv2
import numpy
#BGR
white = (255, 255, 255)
blue = (255, 0, 0)
red = (0, 0, 255)
#((ч строк, ч столбцов, ч в элем), тип данных)
IMG = numpy.zeros((450, 800, 3), dtype = numpy.uint8)
'''
Syntax: cv2.rectangle(image, start_point, end_point, color, thickness)
start_point: It is the starting coordinates of rectangle.
end_point: It is the ending coordinates of rectangle. 
color: It is the color of border line of rectangle to be drawn. 
thickness(толщина): It is the thickness of the rectangle border line in px. 
Thickness of -1 px will fill the rectangle shape by the specified color.
'''
cv2.rectangle(IMG, (0, 0), (800, 150), white, -1 )
cv2.rectangle(IMG, (0, 150), (800, 300), blue, -1 )
cv2.rectangle(IMG, (0, 300), (800, 450), red, -1 )
cv2.imshow('Flag', IMG)

IMG_C = numpy.zeros((700, 200, 3), dtype = numpy.uint8)
#Проверка порядка записи каналов (B, G, R)
cv2.rectangle(IMG_C, (0, 0), (200, 100), (255, 0, 0), -1 )
cv2.rectangle(IMG_C, (0, 100), (200, 200), (0, 255, 0), -1 )
cv2.rectangle(IMG_C, (0, 200), (200, 300), (0, 0, 255), -1 )
#silver
cv2.rectangle(IMG_C, (0, 300), (200, 400), (192, 192, 192), -1 )
#yellow
cv2.rectangle(IMG_C, (0, 400), (200, 500), (0, 255, 255), -1 )
#orange
cv2.rectangle(IMG_C, (0, 500), (200, 600), (0, 165, 255), -1 )
#chocolate
cv2.rectangle(IMG_C, (0, 600), (200, 700), (30, 105, 210), -1 )

cv2.imshow('Color', IMG_C)
cv2.waitKey(-1)
cv2.destroyAllWindows()