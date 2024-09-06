import cv2, sys
import numpy as np

src = cv2.imread('data2/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('Image load failed')
    
kernel = 

dst1 = cv2.blur(src, kernel=kernel)

cv2.imshow('src', src)
cv2.imshow('dst1', dst)
cv2.waitKey()
cv2.destroyAllWindows()