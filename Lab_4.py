import cv2
import numpy
'''
def FUN(img, treshold):
    for i in range(len(img)):
        for j in range(len(img[i])):
            if img[i][j] > treshold:
                img[i][j] = 255
            else:
                img[i][j] = 0
    return img

IMG = cv2.imread('/home/user/Documents/6491_Baburin/LAB_3/test_2.jpeg',cv2.IMREAD_GRAYSCALE)
IMG = FUN(IMG, 50)
cv2.imshow('F', IMG)
cv2.imwrite('/home/user/Documents/6491_Baburin/LAB_4/test_F.jpeg',IMG)
'''
road1 = cv2.imread('/home/user/Documents/6491_Baburin/LAB_4/R_1.jpeg',cv2.IMREAD_REDUCED_GRAYSCALE_2)
new_threshold, new_road1 = cv2.threshold(road1, 200, 255, cv2.THRESH_BINARY)
cv2.imshow('R1', new_road1)

road2 = cv2.imread('/home/user/Documents/6491_Baburin/LAB_4/R_2.jpeg',cv2.IMREAD_REDUCED_GRAYSCALE_8)
new_road2 = cv2.adaptiveThreshold(road2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 701, -49)
cv2.imshow('R2', new_road2)

T1 = cv2.imread('/home/user/Documents/6491_Baburin/LAB_4/T_1.jpeg',cv2.IMREAD_GRAYSCALE)
new_threshold, new_T1 = cv2.threshold(T1, 180, 255, cv2.THRESH_BINARY)
cv2.imshow('T1', new_T1)

T2 = cv2.imread('/home/user/Documents/6491_Baburin/LAB_4/T_2.jpg',cv2.IMREAD_GRAYSCALE)
new_threshold, new_T2 = cv2.threshold(T2, 180, 255, cv2.THRESH_BINARY)
cv2.imshow('T2', new_T2)
new_T = cv2.adaptiveThreshold(T1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 50)
cv2.imshow('T1A', new_T)

T3 = cv2.imread('/home/user/Documents/6491_Baburin/LAB_4/T_3.jpeg',cv2.IMREAD_GRAYSCALE)
new_threshold, new_T3 = cv2.threshold(T3, 180, 255, cv2.THRESH_OTSU)
cv2.imshow('T3', new_T3)
new_T33 = cv2.adaptiveThreshold(T3, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 50)
cv2.imshow('T3A', new_T33)

cv2.waitKey(-1)
cv2.destroyAllWindows() 
        
