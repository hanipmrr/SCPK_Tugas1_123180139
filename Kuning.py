import cv2
import numpy as np
for i in range(1,4): 
 img=cv2.imread('gb'+str(i)+'.png',1)
 hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

 lower_warna = np.array([20, 100, 100])
 upper_warna = np.array([40, 255, 255])
 mask1 = cv2.inRange(hsv, lower_warna, upper_warna)

 mask = mask1

 new_img = cv2.bitwise_and(img, img, mask = mask)
 
 cv2.imshow('mask',mask)
 cv2.imshow('image', img)
 
 cv2.waitKey(0)
 cv2.destroyAllWindows()
