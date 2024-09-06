import cv2
import numpy as np
import matplotlib.pyplot as plt

isColor = True

if not isColor:
    #grayScale
    src = cv2.imread('data/candies.png', cv2.IMREAD_GRAYSCALE)
    #밝기 변화
    dst1 = cv2.add(src, 50)
    hist1 = cv2.calcHist([src],[0], None, [256], [0,256])
    hist2 = cv2.calcHist([dst1],[0], None, [256], [0,256])

    #dit1 = src + 100

if isColor:
    src = cv2.imread('data/candies.jpg')
    #채널별로 100씩 더한다. 채절의 순서는 BGR
    #더하는 값은 튜풀로 입력
    dst1 = cv2.add(src, (100, 100, 100))
    #dst1 = cv2.add(src, 100)
        
plt.plot(hist1)
plt.plot(hist2)
plt.show()

