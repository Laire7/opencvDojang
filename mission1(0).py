import sys
import numpy as np
import cv2

hmin=50
hmax=70
mask=None

# 트랙바 콜백 함수 생성
def on_trackbar(pos):
    global hmin, hmax
    hmin = cv2.getTrackbarPos('H_min', 'frame')
    hmax = cv2.getTrackbarPos('H_max', 'frame')
    
    # inRange함수에 적용
    global mask
    mask = cv2.inRange(src_hsv, (hmin,150,0), (hmax,255,255))
    cv2.imshow('frame', mask) # 트랙바 지정 된 값을 이미지에 적용

# 이미지 파일명
fileName = "misson/01.png"
fileName1 = "misson/01.png"

src = cv2.imread(fileName)
src1 = cv2.imread(fileName1)

if src is None: # 이미지 경로가 틀렸을 때
    sys.exit("Image Load failed!")
    
# 색상의 범위를 잘 지정하려면 bgr->hsv
src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# 창을 먼저 생성, 트랙바 추가
cv2.namedWindow('frame')
cv2.imshow('frame', src_hsv)

# H_min : 40~60
cv2.createTrackbar('H_min', 'frame', 40, 60, on_trackbar)
cv2.createTrackbar('H_max', 'frame', 60, 80, on_trackbar)

on_trackbar(0)
cv2.copyTo(src1, mask, src)

cv2.waitKey()
cv2.destroyAllWindows()

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt 

# orig_img = cv2.imread('misson/01.png')[...,::-1]
# # Convert the image to HSV color space
# orig_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2RGB)
# # Create a sharpening kernel
# kernel = np.array([[0, -1, 0],
#                    [-1, 5,-1],
#                    [0, -1, 0]])

# dst = cv2.filter2D(orig_img, -1, kernel)
# dst = cv2.fastNlMeansDenoisingColored(dst,None,10,10,7,21)

# # Apply the sharpening filter

# plt.figure(figsize=(12,8))
# # plt.subplot(121), plt.imshow(orig_img),plt.title("Original Image")
# # plt.subplot(122), plt.imshow(dst), plt.title("Denoised Image")
# cv2.imshow('src1', orig_img)
# cv2.imshow('dst', dst)
# plt.show()

# # 1 =======================================================================================================================================
# # 이런 저런 필더들을 chatGPT한태 물어보고 적용하다가, 강사님이 추천해주신 필터들로 적용을 했더니, 파라미터가 잘 적용이 되지 않아서 그런지, 강사님 처럼 깔금하게 나오지 않았습니다
# import cv2, sys
# import numpy as np

# src = cv2.imread('misson/01.png')
# # src = cv2.imread('misson/01.png')

# if src is None:
#     sys.exit('Image load failed')

# # dst = cv2.GaussianBlur(src, 3)

# # dst1 = cv2.bilateralFilter(src, -1,10,5)
# # dst1 = cv2.bilateralFilter(src, d=5, sigmaColor=5, sigmaSpace=5)
# # dst2 = cv2.fastNlMeansDenoising(src, None, 30, 7, 21)
# dst2 = cv2.fastNlMeansDenoising(src, None, 30, 7, 21)

# cv2.imshow('src1', src)
# cv2.imshow('dst', dst2)
# cv2.waitKey()
# cv2.destroyAllWindows()

# # Display the manually created color image
# cv2.imshow('Color Image', dst2)
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

# import cv2, sys
# import numpy as np

# def denoise(src, d, sigmaColor, sigmaSpace, h, templateWindowSize, searchWindowSize):
#     # Bilateral filter
#     dst1 = cv2.bilateralFilter(src, -1, d, sigmaColor, sigmaSpace)

#     # FastNlMeansDenoising
#     dst2 = cv2.fastNlMeansDenoising(src, None, h, templateWindowSize, searchWindowSize)

#     # Combine denoising techniques (optional)
#     dst = cv2.addWeighted(dst1, 0.7, dst2, 0.3, 0)

#     # Apply sharpening (optional)
#     dst = cv2.GaussianBlur(dst, (3, 3), 0)
#     dst = cv2.addWeighted(src, 1.5, dst, -0.5, 0)

#     return dst

# def on_bilateral_trackbar(val):
#     global d, sigmaColor, sigmaSpace, src, dst
#     d = cv2.getTrackbarPos('d', 'Parameters')
#     sigmaColor = cv2.getTrackbarPos('sigmaColor', 'Parameters')
#     sigmaSpace = cv2.getTrackbarPos('sigmaSpace', 'Parameters')
#     dst = denoise(src, d, sigmaColor, sigmaSpace, h, templateWindowSize, searchWindowSize)
#     cv2.imshow('dst', dst)

# def on_fastnlmeans_trackbar(val):
#     global h, templateWindowSize, searchWindowSize, src, dst
#     h = cv2.getTrackbarPos('h', 'Parameters')
#     templateWindowSize = cv2.getTrackbarPos('templateWindowSize', 'Parameters')
#     searchWindowSize = cv2.getTrackbarPos('searchWindowSize', 'Parameters')
#     dst = denoise(src, d, sigmaColor, sigmaSpace, h, templateWindowSize, searchWindowSize)
#     cv2.imshow('dst', dst)

# src = cv2.imread('misson/01.png')

# if src is None:
#     sys.exit('Image load failed')

# # Initial parameter values
# d = 20
# sigmaColor = 5
# sigmaSpace = 5
# h = 35
# templateWindowSize = 7
# searchWindowSize = 21

# cv2.namedWindow('Parameters')
# cv2.createTrackbar('d', 'Parameters', 1, 50, on_bilateral_trackbar)
# cv2.createTrackbar('sigmaColor', 'Parameters', 1, 255, on_bilateral_trackbar)
# cv2.createTrackbar('sigmaSpace', 'Parameters', 1, 255, on_bilateral_trackbar)
# cv2.createTrackbar('h', 'Parameters', 1, 100, on_fastnlmeans_trackbar)
# cv2.createTrackbar('templateWindowSize', 'Parameters', 1, 255, on_fastnlmeans_trackbar)
# cv2.createTrackbar('searchWindowSize', 'Parameters', 1, 255, on_fastnlmeans_trackbar)

# dst = denoise(src, d, sigmaColor, sigmaSpace, h, templateWindowSize, searchWindowSize)

# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 4 ========================================================================================
# import cv2
# import numpy as np

# def denoise_sky(image_path):
#     # Load the image
#     img = cv2.imread(image_path)

#     # Convert the image to HSV color space
#     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#     # Define the range for the sky (adjust as needed)
#     lower_sky = np.array([0, 0, 100])  # Adjust the lower bound for hue, saturation, and value
#     upper_sky = np.array([180, 255, 255])  # Adjust the upper bound

#     # Create a mask for the sky
#     mask = cv2.inRange(hsv, lower_sky, upper_sky)

#     # Apply Gaussian blur to the masked image to denoise the sky
#     blurred_mask = cv2.GaussianBlur(mask, (5, 5), 0)  # Adjust kernel size and sigmaX

#     # Create a new image with the denoised sky
#     denoised_img = img.copy()
#     denoised_img[blurred_mask == 0] = 0

#     return denoised_img

# # Example usage
# image_path = "misson/01.png"
# denoised_img = denoise_sky(image_path)

# # Display the denoised image
# cv2.imshow("Denoised Image", denoised_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 5 ========================================================================================
# import cv2
# import numpy as np

# def denoise_sky(image_path, lower_h, upper_h, lower_s, upper_s, lower_v, upper_v):
#     # Load the image
#     img = cv2.imread(image_path)

#     # Convert the image to HSV color space
#     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#     # Define the range for the sky (adjust as needed)
#     lower_sky = np.array([lower_h, lower_s, lower_v])
#     upper_sky = np.array([upper_h, upper_s, upper_v])

#     # Create a mask for the sky
#     mask = cv2.inRange(hsv, lower_sky, upper_sky)

#     # Apply Gaussian blur to the masked image to denoise the sky
#     blurred_mask = cv2.GaussianBlur(mask, (5, 5), 0)

#     # Create a new image with the denoised sky
#     denoised_img = img.copy()
#     denoised_img[blurred_mask == 0] = 0

#     return denoised_img

# def on_trackbar(val):
#     global lower_h, upper_h, lower_s, upper_s, lower_v, upper_v, image_path, denoised_img

#     lower_h = cv2.getTrackbarPos('lower_h', 'HSV Range')
#     upper_h = cv2.getTrackbarPos('upper_h', 'HSV Range')
#     lower_s = cv2.getTrackbarPos('lower_s', 'HSV Range')
#     upper_s = cv2.getTrackbarPos('upper_s', 'HSV Range')
#     lower_v = cv2.getTrackbarPos('lower_v', 'HSV Range')
#     upper_v = cv2.getTrackbarPos('upper_v', 'HSV Range')

#     denoised_img = denoise_sky(image_path, lower_h, upper_h, lower_s, upper_s, lower_v, upper_v)
#     cv2.imshow("Denoised Image", denoised_img)

# # Example usage
# image_path = "misson/01.png"

# # Initial values for HSV range
# lower_h = 0
# upper_h = 180
# lower_s = 0
# upper_s = 255
# lower_v = 100
# upper_v = 255

# denoised_img = denoise_sky(image_path, lower_h, upper_h, lower_s, upper_s, lower_v, upper_v)

# cv2.namedWindow("HSV Range")
# cv2.createTrackbar('lower_h', 'HSV Range', 0, 180, on_trackbar)
# cv2.createTrackbar('upper_h', 'HSV Range', 0, 180, on_trackbar)
# cv2.createTrackbar('lower_s', 'HSV Range', 0, 255, on_trackbar)
# cv2.createTrackbar('upper_s', 'HSV Range', 0, 255, on_trackbar)
# cv2.createTrackbar('lower_v', 'HSV Range', 0, 255, on_trackbar)
# cv2.createTrackbar('upper_v', 'HSV Range', 0, 255, on_trackbar)
# on_trackbar(0)

# cv2.imshow("Denoised Image", denoised_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
