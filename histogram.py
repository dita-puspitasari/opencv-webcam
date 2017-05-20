import cv2
import numpy as np
from matplotlib import pyplot as plt #Matplotlib hadir dengan fungsi merencanakan histogram: matplotlib.pyplot.hist (). Ini langsung menemukan histogram dan plot itu. Anda tidak perlu menggunakan fungsi calcHist () atau np.histogram () untuk menemukan histogram.

img = cv2.imread('rose.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

equ = cv2.equalizeHist(gray)    #rumus equalization

cv2.imshow('Gambar Asli',gray)
cv2.imshow('Histogram Equalization', equ)

plt.figure('Histogram Equalization')
plt.subplot(2,1,1),plt.hist(gray.ravel(),256,[0,256]),plt.title('Histogram awal')
plt.subplot(2,1,2),plt.hist(equ.ravel(),256,[0,256]),plt.title('Histogram hasil equalization')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()