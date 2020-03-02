import cv2
import numpy as np

#OpenCV по умолчанию использует BGR, а не RGB

#указывем путь к изображению; цифра указывает на цветовое отображение картинки
#-1 - Загружает изображение таким какое есть, включая альфа канал (если имеется)
#0 - Загружает изображение в оттенках серого
#1 - Стандартный флаг - загружает цветное изображение, игнорируя альфа-канал
img = cv2.imread("E:/work/Python/001.jpg", 1);
#показываем изображение
cv2.imshow("BGR", img);
cv2.waitKey (0)
cv2.destroyAllWindows()
# изображение показывается пока не будет нажата любая клавиша,
# об этом говорит 0 в скобках; в скобках указывается время в миллисекундах
img_grey = cv2.imread("E:/work/Python/001.jpg", 0);
cv2.imshow("GRAYSCALE", img_grey);
cv2.waitKey (0)
cv2.destroyAllWindows()
#сохраняем изображение в оттенках серого
cv2.imwrite ( 'mops_grey.jpg' , img_grey)

#инвертированное изображение
img_invert = cv2.bitwise_not(img_grey)
cv2.imshow("Invert", img_invert);
cv2.waitKey (0)
cv2.destroyAllWindows()
#меняем зеленый и красный канал местами
g1=np.copy(img[:,:,1]);
img[:,:,1] = np.copy(img[:,:,2])
img[:,:,2] = np.copy(g1)

cv2.imshow("BRG", img);
cv2.waitKey (0)
cv2.destroyAllWindows()
#доп1 - создаем пустое полноцветное изображение
img_extra=np.zeros((300,500,3))
cv2.imshow("empty",img_extra)
cv2.waitKey (0)
cv2.destroyAllWindows()
#рисуем флаг
#изображение,координаты первой точки, координаты второй точкиб цветб толщина линии
#если толщина линии задана отрицательным числом, то прямоугольник закрашивается цветом линии
cv2.rectangle(img_extra,(0,0),(500,100),(255,255,255),-1)
cv2.rectangle(img_extra,(0,100),(500,200),(255,0,0),-1)
cv2.rectangle(img_extra,(0,200),(500,300),(0,0,255),-1)

cv2.imshow("Flag",img_extra)
cv2.waitKey (0)
cv2.destroyAllWindows()
#доп2
#проверка цвета первого канала
img_extra=np.zeros((300,500,3), np.uint8)
img_extra[:,:,0] = 255;
cv2.imshow("first_chanel",img_extra)
cv2.waitKey (0)
cv2.destroyAllWindows()
#проверка цвета второго канала
img_extra=np.zeros((300,500,3), np.uint8)
img_extra[:,:,1] = 255;
cv2.imshow("second_chanel",img_extra)
cv2.waitKey (0)
cv2.destroyAllWindows()
#проверка цвета третьего канала
img_extra=np.zeros((300,500,3), np.uint8)
img_extra[:,:,2] = 255;
print(img_extra)
cv2.imshow("third_chanel",img_extra)
cv2.waitKey (0)
cv2.destroyAllWindows()
#комбинация цветов
while True:
    img_extra = np.zeros((300, 500, 3), np.uint8)
    b=input("Введите оттенок синего: ")
    g=input("Введите оттенок зеленого: ")
    r=input("Введите оттенок красного: ")
    img_extra[:,:] = (b,g,r);
    #print(img_extra)
    #print(type(img_extra[0,0,0]))
    cv2.imshow("combination",img_extra)
    cv2.waitKey (0)
    cv2.destroyAllWindows()
    while True:
        cont = input("Желаете продолжить [Y/N]: ");
        if cont == "Y":
            break
        elif cont != "Y" and cont != "N":
            print("попробуйте снова")
        else:
            break
    if cont == "N":
        break