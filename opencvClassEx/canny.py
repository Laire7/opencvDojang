import cv2, sys
import numpy as np

src =cv2.imread('data2/road.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('Image load failed')


dst = cv2.Canny(src, 64, 128)
dst1 = cv2.Canny(src, 5, 128)
dst2 = cv2.Canny(src, 64, 20)

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)
cv2.waitKey()
cv2.destroyAllWindows()
