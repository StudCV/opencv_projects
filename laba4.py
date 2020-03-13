import cv2
import numpy
import random

foto = cv2.imread('/home/user/Documents/91-2/laba4/BIGCAT',cv2.IMREAD_GRAYSCALE)
cv2.imshow('icxodnik', foto)
for i in range(0,1000):
    for ii in range(0,1600):
        if foto[i][ii] >= 122: 
            foto[i][ii] = 255  
        else:
            foto[i][ii] = 0
cv2.imshow('moi filtr', foto)
cv2.waitKey(0)
cv2.destroyAllWindows()


fotodorogi1 = cv2.imread('/home/user/Documents/91-2/laba4/doroga1',cv2.IMREAD_GRAYSCALE)
fotodorogi2 = cv2.imread('/home/user/Documents/91-2/laba4/doroga2',cv2.IMREAD_GRAYSCALE)
fotodorogi3 = cv2.imread('/home/user/Documents/91-2/laba4/doroga3',cv2.IMREAD_GRAYSCALE)

fotodorogi4 =cv2.imread('/home/user/Documents/91-2/laba4/ckan',cv2.IMREAD_GRAYSCALE)

fotodorogi5 =cv2.imread('/home/user/Documents/91-2/laba4/nadpic',cv2.IMREAD_GRAYSCALE)
fotodorogi6 =cv2.imread('/home/user/Documents/91-2/laba4/nadpic1',cv2.IMREAD_GRAYSCALE)


ing ,  img = cv2.threshold(fotodorogi1, 122, 255 , cv2.THRESH_BINARY) 
cv2.imshow('doroga1', fotodorogi1)
cv2.imshow('THRESH_BINARY doroga1 122', img)


ing1 ,  img1 = cv2.threshold(fotodorogi2, 200, 255 , cv2.THRESH_BINARY) 
cv2.imshow('doroga2', fotodorogi2)
cv2.imshow('THRESH_BINARY doroga2 200', img1)

ing2 ,  img2 = cv2.threshold(fotodorogi3, 122, 255 , cv2.THRESH_BINARY) 
cv2.imshow('doroga3', fotodorogi3)
cv2.imshow('THRESH_BINARY doroga3 122', img2)
 
ing3 ,  img3 = cv2.threshold(fotodorogi4, 122, 255 , cv2.THRESH_BINARY) 
cv2.imshow('ckan', fotodorogi4)
cv2.imshow('THRESH_BINARY ckan 122', img3)

ing4 ,  img4 = cv2.threshold(fotodorogi5, 122, 255 , cv2.THRESH_BINARY) 
cv2.imshow('nadpic', fotodorogi5)
cv2.imshow('THRESH_BINARY nadpic 122', img4)

ing5 ,  img5 = cv2.threshold(fotodorogi6, 122, 255 , cv2.THRESH_BINARY) 
cv2.imshow('nadpic1', fotodorogi6)
cv2.imshow('THRESH_BINARY nadpic1 122', img5) 

cv2.waitKey(0)
cv2.destroyAllWindows()


ing ,  img = cv2.threshold(fotodorogi1, 122, 255 , cv2.THRESH_TRUNC) 
cv2.imshow('doroga1', fotodorogi1)
cv2.imshow('THRESH_TRUNC doroga1 122', img)


ing1 ,  img1 = cv2.threshold(fotodorogi2, 122, 255 , cv2.THRESH_TRUNC) 
cv2.imshow('doroga2', fotodorogi2)
cv2.imshow('THRESH_TRUNC doroga2 122', img1)

ing2 ,  img2 = cv2.threshold(fotodorogi3, 200, 255 , cv2.THRESH_TRUNC) 
cv2.imshow('doroga3', fotodorogi3)
cv2.imshow('THRESH_TRUNC doroga3 200', img2)
 
ing3 ,  img3 = cv2.threshold(fotodorogi4, 122, 255 , cv2.THRESH_TRUNC) 
cv2.imshow('ckan', fotodorogi4)
cv2.imshow('THRESH_TRUNC ckan 122', img3)

ing4 ,  img4 = cv2.threshold(fotodorogi5, 122, 255 , cv2.THRESH_TRUNC) 
cv2.imshow('nadpic', fotodorogi5)
cv2.imshow('THRESH_TRUNC nadpic 122', img4)

ing5 ,  img5 = cv2.threshold(fotodorogi6, 122, 255 , cv2.THRESH_TRUNC) 
cv2.imshow('nadpic1', fotodorogi6)
cv2.imshow('THRESH_TRUNC nadpic1 122', img5)

cv2.waitKey(0)
cv2.destroyAllWindows() 



ing ,  img = cv2.threshold(fotodorogi1, 122, 255 , cv2.THRESH_TOZERO) 
cv2.imshow('doroga1', fotodorogi1)
cv2.imshow('THRESH_TOZERO doroga1 122', img)


ing1 ,  img1 = cv2.threshold(fotodorogi2, 122, 255 , cv2.THRESH_TOZERO) 
cv2.imshow('doroga2', fotodorogi2)
cv2.imshow('THRESH_TOZERO doroga2 122', img1)

ing2 ,  img2 = cv2.threshold(fotodorogi3, 200, 255 , cv2.THRESH_TOZERO) 
cv2.imshow('doroga3', fotodorogi3)
cv2.imshow('THRESH_TOZERO doroga3 200', img2)
 
ing3 ,  img3 = cv2.threshold(fotodorogi4, 122, 255 , cv2.THRESH_TOZERO) 
cv2.imshow('ckan', fotodorogi4)
cv2.imshow('THRESH_TOZERO ckan 122', img3)

ing4 ,  img4 = cv2.threshold(fotodorogi5, 122, 255 , cv2.THRESH_TOZERO) 
cv2.imshow('nadpic', fotodorogi5)
cv2.imshow('THRESH_TOZERO nadpic 122', img4)

ing5 ,  img5 = cv2.threshold(fotodorogi6, 122, 255 , cv2.THRESH_TOZERO) 
cv2.imshow('nadpic1', fotodorogi6)
cv2.imshow('THRESH_TOZERO nadpic1 122', img5)

cv2.waitKey(0)
cv2.destroyAllWindows() 



ing ,  img = cv2.threshold(fotodorogi1, 122, 255 , cv2.THRESH_OTSU) 
cv2.imshow('doroga1', fotodorogi1)
cv2.imshow('THRESH_OTSU doroga1 ', img)


ing1 ,  img1 = cv2.threshold(fotodorogi2, 122, 255 , cv2.THRESH_OTSU) 
cv2.imshow('doroga2', fotodorogi2)
cv2.imshow('THRESH_OTSU doroga2', img1)

ing2 ,  img2 = cv2.threshold(fotodorogi3, 200, 255 , cv2.THRESH_OTSU) 
cv2.imshow('doroga3', fotodorogi3)
cv2.imshow('THRESH_OTSU doroga3', img2)
 
ing3 ,  img3 = cv2.threshold(fotodorogi4, 122, 255 , cv2.THRESH_OTSU) 
cv2.imshow('ckan', fotodorogi4)
cv2.imshow('THRESH_OTSU ckan', img3)

ing4 ,  img4 = cv2.threshold(fotodorogi5, 122, 255 , cv2.THRESH_OTSU) 
cv2.imshow('nadpic', fotodorogi5)
cv2.imshow('THRESH_OTSU nadpic', img4)

ing5 ,  img5 = cv2.threshold(fotodorogi6, 122, 255 , cv2.THRESH_OTSU) 
cv2.imshow('nadpic1', fotodorogi6)
cv2.imshow('THRESH_OTSU nadpic1', img5)

cv2.waitKey(0)
cv2.destroyAllWindows() 


ing ,  img = cv2.threshold(fotodorogi1, 122, 255 , cv2.THRESH_TRIANGLE) 
cv2.imshow('doroga1', fotodorogi1)
cv2.imshow('THRESH_TRIANGLE doroga1 ', img)


ing1 ,  img1 = cv2.threshold(fotodorogi2, 122, 255 , cv2.THRESH_TRIANGLE) 
cv2.imshow('doroga2', fotodorogi2)
cv2.imshow('THRESH_TRIANGLE doroga2', img1)

ing2 ,  img2 = cv2.threshold(fotodorogi3, 200, 255 , cv2.THRESH_TRIANGLE) 
cv2.imshow('doroga3', fotodorogi3)
cv2.imshow('THRESH_TRIANGLE doroga3', img2)
 
ing3 ,  img3 = cv2.threshold(fotodorogi4, 122, 255 , cv2.THRESH_TRIANGLE) 
cv2.imshow('ckan', fotodorogi4)
cv2.imshow('THRESH_TRIANGLE ckan', img3)

ing4 ,  img4 = cv2.threshold(fotodorogi5, 122, 255 , cv2.THRESH_TRIANGLE) 
cv2.imshow('nadpic', fotodorogi5)
cv2.imshow('THRESH_TRIANGLE nadpic', img4)

ing5 ,  img5 = cv2.threshold(fotodorogi6, 122, 255 , cv2.THRESH_TRIANGLE) 
cv2.imshow('nadpic1', fotodorogi6)
cv2.imshow('THRESH_TRIANGLE nadpic1', img5)

cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.adaptiveThreshold(fotodorogi1, 255, cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY , 5 ,20)
cv2.imshow('doroga1', fotodorogi1)
cv2.imshow('ADAPTIVE_THRESH_MEAN_C doroga1 ', img)


img1 = cv2.adaptiveThreshold(fotodorogi2, 255, cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY , 5 ,20)
cv2.imshow('doroga2', fotodorogi2)
cv2.imshow('ADAPTIVE_THRESH_MEAN_C doroga2', img1)

img2 = cv2.adaptiveThreshold(fotodorogi3, 255, cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY , 5 ,20)
cv2.imshow('doroga3', fotodorogi3)
cv2.imshow('ADAPTIVE_THRESH_MEAN_C doroga3', img2)
 
img3 = cv2.adaptiveThreshold(fotodorogi4, 255, cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY , 5 ,20)
cv2.imshow('ckan', fotodorogi4)
cv2.imshow('ADAPTIVE_THRESH_MEAN_C ckan', img3)

img4 = cv2.adaptiveThreshold(fotodorogi5, 255, cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY , 5 ,20)
cv2.imshow('nadpic', fotodorogi5)
cv2.imshow('ADAPTIVE_THRESH_MEAN_C nadpic', img4)

img5 = cv2.adaptiveThreshold(fotodorogi6, 255, cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY , 5 ,20)
cv2.imshow('nadpic1', fotodorogi6)
cv2.imshow('ADAPTIVE_THRESH_MEAN_C nadpic1', img5)

cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.adaptiveThreshold(fotodorogi1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 5 ,20)
cv2.imshow('doroga1', fotodorogi1)
cv2.imshow('ADAPTIVE_THRESH_GAUSSIAN_C doroga1 ', img)


img1 = cv2.adaptiveThreshold(fotodorogi2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 5 ,20)
cv2.imshow('doroga2', fotodorogi2)
cv2.imshow('ADAPTIVE_THRESH_GAUSSIAN_C doroga2', img1)

img2 = cv2.adaptiveThreshold(fotodorogi3, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 5 ,20)
cv2.imshow('doroga3', fotodorogi3)
cv2.imshow('ADAPTIVE_THRESH_GAUSSIAN_C doroga3', img2)
 
img3 = cv2.adaptiveThreshold(fotodorogi4, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 5 ,20)
cv2.imshow('ckan', fotodorogi4)
cv2.imshow('ADAPTIVE_THRESH_GAUSSIAN_C ckan', img3)

img4 = cv2.adaptiveThreshold(fotodorogi5, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 5 ,20)
cv2.imshow('nadpic', fotodorogi5)
cv2.imshow('ADAPTIVE_THRESH_GAUSSIAN_C nadpic', img4)

img5 = cv2.adaptiveThreshold(fotodorogi6, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 5 ,20)
cv2.imshow('nadpic1', fotodorogi6)
cv2.imshow('ADAPTIVE_THRESH_GAUSSIAN_C nadpic1', img5)

cv2.waitKey(0)
cv2.destroyAllWindows()

