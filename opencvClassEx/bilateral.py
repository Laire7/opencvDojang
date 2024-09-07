import cv2, sys
import numpy as np

# cartoon filter 

src =cv2.imread('../data/lena.bmp')

if src is None:
    sys.exit('Image load failed')

dst = cv2.bilateralFilter(src, -1,10,5)
dst1 = cv2.bilateralFilter(src, 5,10,5)
dst2 = cv2.bilateralFilter(src, -1,100,5)
dst3 = cv2.bilateralFilter(src, -1,10,50)

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)
cv2.imshow('dst3',dst3)
cv2.waitKey()
cv2.destroyAllWindows()
