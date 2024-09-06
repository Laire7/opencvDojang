import cv2
import numpy as np

isColor = True

if not isColor:
    #grayScale
    src = cv2.imread('data/cat.jpg', cv2.IMREAD_GRAYSCALE)
    #밝기 변화
    dst1 = cv2.add(src, 100)
    # dst1 = cv2.add(src, (100, 100, 100))

if isColor:
    src = cv2.imread('data/cat.jpg')
    #채널별로 100씩 더한다. 채절의 순서는 BGR
    #더하는 값은 튜풀로 입력
    dst1 = cv2.add(src, (100, 100, 100))
    #dst1 = cv2.add(src, 100)
        
cv2.imshow('img', src)
cv2.imshow('dst1', dst1)
cv2.waitKey()
cv2.destroyAllWindows()