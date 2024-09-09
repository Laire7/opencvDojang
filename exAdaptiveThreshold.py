import cv2, sys
import matplotlib.pyplot as plt
import myLib

src = cv2.imread('data/srcThreshold.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('Image load failed')
    
myLib.hist_gray(src)

# threshold함수를 이용해서 흑과 백으로 나눈다
ret, src_th = cv2.threshold(src, 175, 255, cv2.THRESH_BINARY)
src_adTh_mean = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 7)
src_adTh_gauss = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 7)

cv2.imshow('src', src)
cv2.imshow('src_th', src_th)
cv2.imshow('src_adTh_mean', src_adTh_mean)
cv2.imshow('src_adTh_gauss', src_adTh_gauss)
cv2.waitKey()
cv2.destroyAllWindows()