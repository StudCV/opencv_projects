import cv2

img = cv2.imread('/home/user/Documents/92-2/lab3/img.jpg', cv2.IMREAD_COLOR)
img_gs = cv2.imread('/home/user/Documents/92-2/lab3/img.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('RGB', img)
cv2.imshow('GRAYSCALE', img_gs)
cv2.waitKey(0)
cv2.imwrite('/home/user/Documents/92-2/lab3/img_gs.jpg', img_gs)