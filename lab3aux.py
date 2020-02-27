#дополнительные
#флаг РФ
RFflag = np.empty((300, 200, 3))
for y in range(300):
    for x in range(200):
        for c in range(3):
            if y<100:
                if c==0
                  RFflag[y][x][c]
cv2.imshow('RGB' ,RFflag)

#cv2.imwrite('test.jpg',img )
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#cv2.imshow('inv',img[:,:,1])
#invert= np.copy(imggrey)


cv2.waitKey(0)
