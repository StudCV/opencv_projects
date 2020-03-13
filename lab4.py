import numpy as np
import cv2
# img = cv2.imread('Documents/91-Gog/lab4/cat.jpeg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('Cat', img)
# img_filtr = np.copy(img)
# tresh = 127
# maxVal = 255

# def treshold_binary(tresh):
#     (a, b) = np.shape(img_filtr)
#     for i in range(0,a):
#         for j in range(0,b):
#             if img_filtr[i][j] > tresh:
#                 img_filtr[i][j] = maxVal
#             else:
#                 img_filtr[i][j] = 0
# treshold_binary(tresh)
# cv2.imshow('Cat_filtr', img_filtr)

razm = cv2.imread('Documents/91-Gog/lab4/разметка.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Razm', razm)

razm1 = cv2.imread('Documents/91-Gog/lab4/разметка1.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Razm1', razm1)

razm2 = cv2.imread('Documents/91-Gog/lab4/разметка2.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Razm2', razm2)

write = cv2.imread('Documents/91-Gog/lab4/Надпись.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Надпись', write)

write1 = cv2.imread('Documents/91-Gog/lab4/Надпись1.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Надпись1', write1)

write2 = cv2.imread('Documents/91-Gog/lab4/Надпись2.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Надпись2', write2)

#:

    # #Пороговые #binary #Разметка 

    # thresh = 127
    # maxVal = 255

    # new_threshold, new_razm = cv2.threshold(razm, thresh, maxVal, cv2.THRESH_BINARY)
    # cv2.imshow('1_1', new_razm)

    # new_threshold, new_razm1 = cv2.threshold(razm1, thresh, maxVal, cv2.THRESH_BINARY)
    # cv2.imshow('1_2', new_razm1)

    # new_threshold, new_razm2 = cv2.threshold(razm2, thresh, maxVal, cv2.THRESH_BINARY)
    # cv2.imshow('1_3', new_razm2)

    # #Пороговые #binary #Надпись

    # new_threshold, new_write = cv2.threshold(write, thresh, maxVal, cv2.THRESH_BINARY)
    # cv2.imshow('1_4', new_write)

    # new_threshold, new_write1 = cv2.threshold(write1, thresh, maxVal, cv2.THRESH_BINARY)
    # cv2.imshow('1_5', new_write1)

    # new_threshold, new_write2 = cv2.threshold(write2, thresh, maxVal, cv2.THRESH_BINARY)
    # cv2.imshow('1_6', new_write2)

    # #Пороговые #TRUNC #Разметка

    # thresh = 100
    # maxVal = 255

    # new_threshold, new1_razm = cv2.threshold(razm, thresh, maxVal, cv2.THRESH_TRUNC)
    # cv2.imshow('2_1', new1_razm)

    # new_threshold, new1_razm1 = cv2.threshold(razm1, thresh, maxVal, cv2.THRESH_TRUNC)
    # cv2.imshow('2_2', new1_razm1)

    # new_threshold, new1_razm2 = cv2.threshold(razm2, thresh, maxVal, cv2.THRESH_TRUNC)
    # cv2.imshow('2_3', new1_razm2)

    # #Пороговые #TRUNC #Надпись

    # new_threshold, new1_write = cv2.threshold(write, thresh, maxVal, cv2.THRESH_TRUNC)
    # cv2.imshow('2_4', new1_write)

    # new_threshold, new1_write1 = cv2.threshold(write1, thresh, maxVal, cv2.THRESH_TRUNC)
    # cv2.imshow('2_5', new1_write1)

    # new_threshold, new1_write2 = cv2.threshold(write2, thresh, maxVal, cv2.THRESH_TRUNC)
    # cv2.imshow('2_6', new1_write2)

    # #Пороговые #TOZERO #Разметка

    # thresh = 127
    # maxVal = 255

    # new_threshold, new2_razm = cv2.threshold(razm, thresh, maxVal, cv2.THRESH_TOZERO)
    # cv2.imshow('3_1', new2_razm)

    # new_threshold, new2_razm1 = cv2.threshold(razm1, thresh, maxVal, cv2.THRESH_TOZERO)
    # cv2.imshow('3_2', new2_razm1)

    # new_threshold, new2_razm2 = cv2.threshold(razm2, thresh, maxVal, cv2.THRESH_TOZERO)
    # cv2.imshow('3_3', new2_razm2)

    # #Пороговые #TOZERO #Надпись

    # new_threshold, new2_write = cv2.threshold(write, thresh, maxVal, cv2.THRESH_TOZERO)
    # cv2.imshow('3_4', new2_write)

    # new_threshold, new2_write1 = cv2.threshold(write1, thresh, maxVal, cv2.THRESH_TOZERO)
    # cv2.imshow('3_5', new2_write1)

    # new_threshold, new2_write2 = cv2.threshold(write2, thresh, maxVal, cv2.THRESH_TOZERO)
    # cv2.imshow('3_6', new2_write2)


    # #Автоматические #OTSU #Разметка

    # thresh = 100
    # maxVal = 255

    # new_threshold, new3_razm = cv2.threshold(razm, thresh, maxVal, cv2.THRESH_OTSU)
    # cv2.imshow('4_1', new3_razm)

    # new_threshold, new3_razm1 = cv2.threshold(razm1, thresh, maxVal, cv2.THRESH_OTSU)
    # cv2.imshow('4_2', new3_razm1)

    # new_threshold, new3_razm2 = cv2.threshold(razm2, thresh, maxVal, cv2.THRESH_OTSU)
    # cv2.imshow('4_3', new3_razm2)

    # #Автоматические #OTSU #Надпись

    # new_threshold, new3_write = cv2.threshold(write, thresh, maxVal, cv2.THRESH_OTSU)
    # cv2.imshow('4_4', new3_write)

    # new_threshold, new3_write1 = cv2.threshold(write1, thresh, maxVal, cv2.THRESH_OTSU)
    # cv2.imshow('4_5', new3_write1)

    # new_threshold, new3_write2 = cv2.threshold(write2, thresh, maxVal, cv2.THRESH_OTSU)
    # cv2.imshow('4_6', new3_write2)

    # #Автоматические #TRIANGLE #Разметка

    # thresh = 255
    # maxVal = 255

    # new_threshold, new4_razm = cv2.threshold(razm, thresh, maxVal, cv2.THRESH_TRIANGLE)
    # cv2.imshow('5_1', new4_razm)

    # new_threshold, new4_razm1 = cv2.threshold(razm1, thresh, maxVal, cv2.THRESH_TRIANGLE)
    # cv2.imshow('5_2', new4_razm1)

    # new_threshold, new4_razm2 = cv2.threshold(razm2, thresh, maxVal, cv2.THRESH_TRIANGLE)
    # cv2.imshow('5_3', new4_razm2)

    # #Автоматические #TRIANGLE #Надпись

    # new_threshold, new4_write = cv2.threshold(write, thresh, maxVal, cv2.THRESH_TRIANGLE)
    # cv2.imshow('5_4', new4_write)

    # new_threshold, new4_write1 = cv2.threshold(write1, thresh, maxVal, cv2.THRESH_TRIANGLE)
    # cv2.imshow('5_5', new4_write1)

    # new_threshold, new4_write2 = cv2.threshold(write2, thresh, maxVal, cv2.THRESH_TRIANGLE)
    # cv2.imshow('5_6', new4_write2)

    # #Адаптивные #MEAN_C #Разметка

    # thresh = 127
    # maxVal = 255
    # blocksize = 7
    # C = 8
    # # adapt_razm = cv2.adaptiveThreshold(razm, maxVal, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blocksize, C)
    # # cv2.imshow('ad_1', adapt_razm)

    # # adapt_razm1 = cv2.adaptiveThreshold(razm1, maxVal, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blocksize, C)
    # # cv2.imshow('ad_2', adapt_razm1)

    # # adapt_razm2 = cv2.adaptiveThreshold(razm2, maxVal, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blocksize, C)
    # # cv2.imshow('ad_3', adapt_razm2)

    # #Автоматические #MEAN_C #Надпись

    # adapt_write = cv2.adaptiveThreshold(write, maxVal, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blocksize, C)
    # cv2.imshow('ad_4', adapt_write)

    # adapt_write1 = cv2.adaptiveThreshold(write1, maxVal, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blocksize, C)
    # cv2.imshow('ad_5', adapt_write1)

    # adapt_write2 = cv2.adaptiveThreshold(write2, maxVal, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blocksize, C)
    # cv2.imshow('ad_6', adapt_write2)

    #Адаптивные #GAUSSIAN_C #Разметка

thresh = 127
maxVal = 255
blocksize = 9
C = 9
# adapt1_razm = cv2.adaptiveThreshold(razm, maxVal, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blocksize, C)
# cv2.imshow('ad1_1', adapt1_razm)

# adapt1_razm1 = cv2.adaptiveThreshold(razm1, maxVal, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blocksize, C)
# cv2.imshow('ad1_2', adapt1_razm1)

# adapt1_razm2 = cv2.adaptiveThreshold(razm2, maxVal, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blocksize, C)
# cv2.imshow('ad1_3', adapt1_razm2)

#Автоматические #GAUSSIAN_C #Надпись

adapt1_write = cv2.adaptiveThreshold(write, maxVal, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blocksize, C)
cv2.imshow('ad1_4', adapt1_write)

adapt1_write1 = cv2.adaptiveThreshold(write1, maxVal, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blocksize, C)
cv2.imshow('ad1_5', adapt1_write1)

adapt1_write2 = cv2.adaptiveThreshold(write2, maxVal, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blocksize, C)
cv2.imshow('ad1_6', adapt1_write2)


cv2.waitKey(-1)