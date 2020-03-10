import cv2
import numpy as np

imagecolour = cv2.imread('/home/user/Documents/91-2/Materials_for_laba_3/kirby.jpg',cv2.IMREAD_COLOR)
imagegrey = cv2.imread('/home/user/Documents/91-2/Materials_for_laba_3/kirby.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow ('RGB',imagecolour)
cv2.imshow ('GRAYSCALE',imagegrey)


cv2.imwrite('/home/user/Documents/91-2/Materials_for_laba_3/kirbygrey.jpg',imagegrey)

invertkirby = np.copy(imagegrey)
invertkirby = 255-invertkirby
cv2.imshow ('GRAYSCALEINVERT',invertkirby)

kibyrgb = cv2.imread('/home/user/Documents/91-2/Materials_for_laba_3/kirby.jpg',cv2.IMREAD_COLOR)
(x,y,z)=kibyrgb.shape
for i in range (0,x):
    for j in range (0,y):
        kibyrgb [i][j][1], kibyrgb [i][j][2]= kibyrgb [i][j][2], kibyrgb [i][j][1]
cv2.imshow ('rgbinvert',kibyrgb)
cv2.waitKey(-1)
