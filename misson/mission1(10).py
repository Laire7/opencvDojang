import cv2
import numpy as np
image = cv2.imread("misson/01.png")
# IMREAD_UNCHANGED는 png 이미지의 alpha 체널 (투명도) 정보를 포함해서 가지고 온다
src = cv2.imread('misson/01.png', cv2.IMREAD_UNCHANGED) 
org = cv2.imread('misson/01.png', cv2.IMREAD_UNCHANGED)

# BGR->HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 밤 하늘과 밝게 빛나는 건물들을 밝기로 (50보다 더 밝은 값을 가진 픽셀들) 구분하기
# mask는 밝은 값들의 픽셀들을 덮어 씌우므로, 어두운 밤 하늘이 아닌 밝은 건물들에 속한 픽셀들 (50보다 더 큰 값들을) 지정한다
# return: Boolean array
# toDenoise = hsv[0, :, :] <=127 and hsv[0, :, :]<=255 and hsv[:, :, 0] >= 31 and  hsv[:, :, 0] <=84

# Define the min and max HSV values (from the previous result)
hsv_min = np.array([0, 0, 31])
hsv_max = np.array([127, 255, 84])

# Create a mask that identifies pixels within the given HSV range
mask = cv2.inRange(hsv, hsv_min, hsv_max)
# cv2.imshow('Mask', mask)

# denoise 효과를 기존 이미지에 적용
# blur = cv2.blur(src, (5,5)) 
denoise = cv2.fastNlMeansDenoisingColored(image,None,10,10,21,21)
blur = cv2.medianBlur(denoise, 9)
cv2.imshow('Denoise', denoise)

# # median = cv2.medianBlur(src,9)
# # blur = cv2.bilateralFilter(image,-1, -10,-100)

# # denoise 효과를 마사크 영역에만 적용
# denoiseWithMask = cv2.copyTo(denoise, mask, src)
# cv2.imshow('Denoise With Mask', denoiseWithMask)

# #sharpen 이미지 선명도 높이기
# # 노이즈 처리를 위해 흐려진 이미지를 kernel 곱셈으로 복구하려 한다 
# kernel = np.array([[0, -1, 0],
#                    [-1, 5,-1],
#                    [0, -1, 0]])
# src = cv2.filter2D(src, -1, kernel)
# # cv2.imshow("3.Denoised Image with mask, then sharpen", src)
# cv2.imshow("orig", org) #기존과 비교

# # 이미지 출력
# cv2.imshow("Original", org)
# cv2.imshow("1.Denoised Image", denoise)
# cv2.imshow("2.Denoised Image with mask", denoiseWithMask)

cv2.waitKey()
cv2.destroyAllWindows()