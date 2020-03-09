import cv2
import numpy as numpy

imagecolour = cv2.imread('/home/user/Documents/91-2/Materials_for_laba_3/kirby.jpg',cv2.IMREAD_COLOR)
imagegrey = cv2.imread('/home/user/Documents/91-2/Materials_for_laba_3/kirby.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow = ('RGB',imagecolour)
cv2.imshow = ('GRAYSCALE',imagegrey)


'''cv2.imwrite('/home/user/Documents/91-2/Materials_for_laba_3/kirbygrey.jpg',imagegrey)'
'cv2.waitKey(-1)'''

'''
color_image_rgb = cv2.cvtColor(imagecolour, cv2.COLOR_BGR2RGB) %maybe from BGR2BRG?%
cv2.imshow('Color RGB', color_image_rgb)
cv2.waitKey(0)
'''
