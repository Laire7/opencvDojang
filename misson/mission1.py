import cv2
import numpy as np
image = cv2.imread("misson/01.png")
# IMREAD_UNCHANGED는 png 이미지의 alpha 체널 (투명도) 정보를 포함해서 가지고 온다
src = cv2.imread('misson/01.png', cv2.IMREAD_UNCHANGED) 
org = cv2.imread('misson/01.png', cv2.IMREAD_UNCHANGED)

# BGR->HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 밤 하늘과 밝게 빛나는 건물들을 밝기로 (50보다 더 밝은 값을 가진 픽셀들) 구분하기
# 50보나 큰 밝기를 가진 픽셀들만 살리고, 어두운 픽셀들은 False(0값)으로 처리한다
# 기존 목표와 (밤 하늘을 포함한 어두운 값들만 살리고 나머지 마스크 처리하기) 반대로 보이지만
# 밤 하늘에 밝은 픽셀 값들을 뭉그러트려 하늘 밝기를 좀 더 통일하고
# 건물들과 밤 하늘을 경계하는 선은 유지해서
# 비록 햇갈리지만, 시도한 여러게 중에 제일 결과가 좋았던 것 같다
unMask = hsv[:, :, 0] >= 50 # Boolean array

# 마스크 만들기 
mask = image.copy() # 기존 이미지를 먼저 복사하고 (deep copy)
mask = unMask.astype(np.uint8) # 밝은 픽셀들은 True -> 1, 어두은 픽셀들은 False ->0로 변한다
# uint8은 부호 없는 8bit 정수를 의미하며 (0~255), 보통 uint8으로 이미지 픽셀 정보를 저장한다

# denoise 효과를 기존 이미지에 적용
denoise = cv2.fastNlMeansDenoisingColored(src,None,10,10,21,21)
# median = cv2.medianBlur(src,9)
# blur = cv2.bilateralFilter(image,-1, -10,-100)

# denoise 효과를 마사크 영역에만 적용
denoiseWithMask = cv2.copyTo(denoise, mask, src)

#sharpen 이미지 선명도 높이기
# 노이즈 처리를 위해 흐려진 이미지를 kernel 곱셈으로 복구하려 한다 
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
src = cv2.filter2D(src, -1, kernel)

# 이미지 출력
cv2.imshow("Original", org)
cv2.imshow("1.Denoised Image", denoise)
cv2.imshow("2.Denoised Image with mask", denoiseWithMask)
cv2.imshow("3.Denoised Image with mask, then sharpen", src)
cv2.waitKey()
cv2.destroyAllWindows()