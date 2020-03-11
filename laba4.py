import cv2
img1 = '/home/user/Documents/radmir6491/Kiany.jpg'
maxValue = 255
def treshold(image, Value):
    img = cv2.imread(img1, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('img before', img1)
    for i in range(len(img)):
        for j in range(len(img[1])):
            if img[i, j] > maxValue:
                img[i, j] = Value
            else:
                img[i, j] = 0