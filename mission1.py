# 1 =======================================================================================================================================
# 이런 저런 필더들을 chatGPT한태 물어보고 적용하다가, 강사님이 추천해주신 필터들로 적용을 했더니, 파라미터가 잘 적용이 되지 않아서 그런지, 강사님 처럼 깔금하게 나오지 않았습니다
# import cv2, sys
# import numpy as np

# src = cv2.imread('misson/01.png')
# # src = cv2.imread('misson/01.png')

# if src is None:
#     sys.exit('Image load failed')

# # dst = cv2.GaussianBlur(src, 3)

# dst1 = cv2.bilateralFilter(src, -1,10,5)
# dst2 = cv2.fastNlMeansDenoising(src, None, 30, 7, 21)

# cv2.imshow('src1', src)
# cv2.imshow('dst', dst2)
# cv2.waitKey()
# cv2.destroyAllWindows()

# # Display the manually created color image
# cv2.imshow('Color Image', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 2 =======================================================================================================================================
# ChatGPT한테 parameter을 바꾸어서 이미지 처리를 해주라고 했더니, 오히려 img가 더 뭉계지는 현상이 이렇났습니다 

# import cv2, sys
# import numpy as np

# src = cv2.imread('misson/01.png')

# if src is None:
#     sys.exit('Image load failed')
    
# # Bilateral filter with adjusted parameters
# dst1 = cv2.bilateralFilter(src, -1, 20, 5)

# # FastNlMeansDenoising with adjusted parameters
# dst2 = cv2.fastNlMeansDenoising(src, None, 35, 7, 21)

# # Combine denoising techniques (optional)
# dst = cv2.addWeighted(dst1, 0.7, dst2, 0.3, 0)

# # Apply sharpening (optional)
# dst = cv2.GaussianBlur(dst, (3, 3), 0)
# dst = cv2.addWeighted(src, 1.5, dst, -0.5, 0)

# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 3 ========================================================================================================================================
# 그래서 trackerbar을 추가해서 더 넣어주라고 했더니, 너무 많은 용량을 차지 해서 그런지, 컴퓨터가 자꾸만 끝겨지는 현상이 일어났습니다
# 시간 사항, 일단 다른 미션부터 하고 돌아가기로 했습니다

import cv2, sys
import numpy as np

def denoise(src, d, sigmaColor, sigmaSpace, h, templateWindowSize, searchWindowSize):
    # Bilateral filter
    dst1 = cv2.bilateralFilter(src, -1, d, sigmaColor, sigmaSpace)

    # FastNlMeansDenoising
    dst2 = cv2.fastNlMeansDenoising(src, None, h, templateWindowSize, searchWindowSize)

    # Combine denoising techniques (optional)
    dst = cv2.addWeighted(dst1, 0.7, dst2, 0.3, 0)

    # Apply sharpening (optional)
    dst = cv2.GaussianBlur(dst, (3, 3), 0)
    dst = cv2.addWeighted(src, 1.5, dst, -0.5, 0)

    return dst

def on_bilateral_trackbar(val):
    global d, sigmaColor, sigmaSpace, src, dst
    d = cv2.getTrackbarPos('d', 'Parameters')
    sigmaColor = cv2.getTrackbarPos('sigmaColor', 'Parameters')
    sigmaSpace = cv2.getTrackbarPos('sigmaSpace', 'Parameters')
    dst = denoise(src, d, sigmaColor, sigmaSpace, h, templateWindowSize, searchWindowSize)
    cv2.imshow('dst', dst)

def on_fastnlmeans_trackbar(val):
    global h, templateWindowSize, searchWindowSize, src, dst
    h = cv2.getTrackbarPos('h', 'Parameters')
    templateWindowSize = cv2.getTrackbarPos('templateWindowSize', 'Parameters')
    searchWindowSize = cv2.getTrackbarPos('searchWindowSize', 'Parameters')
    dst = denoise(src, d, sigmaColor, sigmaSpace, h, templateWindowSize, searchWindowSize)
    cv2.imshow('dst', dst)

src = cv2.imread('misson/01.png')

if src is None:
    sys.exit('Image load failed')

# Initial parameter values
d = 20
sigmaColor = 5
sigmaSpace = 5
h = 35
templateWindowSize = 7
searchWindowSize = 21

cv2.namedWindow('Parameters')
cv2.createTrackbar('d', 'Parameters', 1, 50, on_bilateral_trackbar)
cv2.createTrackbar('sigmaColor', 'Parameters', 1, 255, on_bilateral_trackbar)
cv2.createTrackbar('sigmaSpace', 'Parameters', 1, 255, on_bilateral_trackbar)
cv2.createTrackbar('h', 'Parameters', 1, 100, on_fastnlmeans_trackbar)
cv2.createTrackbar('templateWindowSize', 'Parameters', 1, 255, on_fastnlmeans_trackbar)
cv2.createTrackbar('searchWindowSize', 'Parameters', 1, 255, on_fastnlmeans_trackbar)

dst = denoise(src, d, sigmaColor, sigmaSpace, h, templateWindowSize, searchWindowSize)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
