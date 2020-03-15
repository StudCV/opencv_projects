import cv2 #включение библиотеки opencv
import numpy as np

imagecolour = cv2.imread('/home/user/Documents/91-2/Materials_for_laba_3/kirby.jpg',cv2.IMREAD_COLOR) 
#считываем файл, который возвращает массив с данными об изображении, читается в GRB (цветное изображение)
imagegrey = cv2.imread('/home/user/Documents/91-2/Materials_for_laba_3/kirby.jpg',cv2.IMREAD_GRAYSCALE)
#считываем файл, который возвращает массив с данными об изображении, читается в GRAYSCALE (серый оттенок)
cv2.imshow ('RGB',imagecolour)#вывод обоих изображений на экран под окнами 'RGB' и 'GRAYSCALE' соответственно
cv2.imshow ('GRAYSCALE',imagegrey)

cv2.imwrite('/home/user/Documents/91-2/Materials_for_laba_3/kirbygrey.jpg',imagegrey)
#запись серого изображения в файл kirbygrey

#процесс инвертирования цветов серого изображения
invertkirby = np.copy(imagegrey)#копирование
invertkirby = 255-invertkirby#каждое значение пикселя инвертируется
cv2.imshow ('GRAYSCALEINVERT',invertkirby)#выводим результат

#процесс инвертирования зеленого и красного цветов 
kibyrgb = cv2.imread('/home/user/Documents/91-2/Materials_for_laba_3/kirby.jpg',cv2.IMREAD_COLOR)
#считываем файл, который возвращает массив с данными об изображении, читается в GRB (цветное изображение)
(x,y,z)=kibyrgb.shape#данная функция возвращает размерность массива и значение пикселей
for i in range (0,x):
    for j in range (0,y):
        kibyrgb [i][j][1], kibyrgb [i][j][2]= kibyrgb [i][j][2], kibyrgb [i][j][1]
#каждому пикселю меняем значение второго и третьего какалов (зеленого и красного)        
cv2.imshow ('rgbinvert',kibyrgb)#выводим результат
cv2.waitKey(-1)#ожидание нажатия клавиши
