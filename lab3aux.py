#дополнительные
#флаг РФ
RFflag = np.empty((300, 200, 3))
for y in range(300):
    for x in range(200):
            if y<100:
                RFflag[y][x] = (255,255,255)
            elif y<200:
                RFflag[y][x] = (255,0,0) 
            else:
                RFflag[y][x] = (0,0,255) 
cv2.imshow('Rf flag' ,RFflag)

#палитра
cv2.namedWindow('Colorbars')
#
#cv2.imwrite('test.jpg',img )
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#cv2.imshow('inv',img[:,:,1])
#invert= np.copy(imggrey)


cv2.waitKey(0)
