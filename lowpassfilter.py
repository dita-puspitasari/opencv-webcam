import numpy as np
import cv2


img = cv2.imread('rose.jpg')
lpf = cv2.filter2D(img,-1,np.ones((5,5),np.float32)/25) #membuat low pass filter dengan kernel 5x5

cv2.imshow('Gambar Asli',img)
cv2.imshow('Low Pass Filter',lpf)


cv2.waitKey()
cv2.destroyAllWindows()

