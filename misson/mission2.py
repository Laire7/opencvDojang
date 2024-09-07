import cv2
import numpy as np

# 어둡게 하는 필터 만들기
def darken_image(img, darken_factor=0.5):
    """Darkens an image while preserving sharpness.

    Args:
        img: The input image.
        darken_factor: The factor by which to darken the image (0-1).

    Returns:
        The darkened image.
    """


    # BGR-> HSV (밝기 조정을 위해)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # np.clip 함수 적용
    v = hsv[:, :, 2] #밝기를 지정한 값들만 불러오기
    v = np.clip(v * (1 - darken_factor), 0, 255).astype(np.uint8) 
    #np는 int8만 적용해서, 기존 이미지 값을 int8으로 바꿈
    hsv[:, :, 2] = v  #기존 이미지에 적용

    # HSV -> BGR (화면 출력을 위해)
    darkened_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    return darkened_img

# 이미지 불러오기
image = cv2.imread("misson/03.png")

# 어둡게 하는 함수 불러오기
darkened_image = darken_image(image, darken_factor=0.3)  # 0<darken_factor<1 1에 가까울 수록 더 어둡게 

# 이미지 출력
cv2.imshow("Original Image", image)
cv2.imshow("Darkened Image", darkened_image)
cv2.waitKey()
cv2.destroyAllWindows()

# # 1 ============================================================================
# # inRange함수를 사용하여 h_min과 h_max값을 구했다

# # # inRange함수를 잘 설정하려면 trackBar기능이 필요하다.
# # import sys
# # import numpy as np
# # import cv2

# # # 트랙바 콜백 함수 생성
# # def on_trackbar(pos):
# #     hmin = cv2.getTrackbarPos('H_min', 'Trackbar')
# #     hmax = cv2.getTrackbarPos('H_max', 'Trackbar')
    
# #     # inRange함수에 적용
# #     dst = cv2.inRange(src_hsv, (hmin,150,0), (hmax,255,255))
# #     cv2.imshow('Trackbar', dst)

# # src = cv2.imread('misson/03.png')

# # if src is None:
# #     sys.exit("Image Load failed!")
    
# # # 색상의 범위를 잘 지정하려면 bgr->hsv
# # src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# # # 창에 트랙바를 넣기 위해서는 창을 먼저 생성
# # cv2.namedWindow('Trackbar')
# # cv2.imshow('Trackbar', src)

# # # 트랙바 생성 : 'H_min' 트랙바의 이름, 범위 0~255,  
# # # on_trackbar : 트랙바를 움직일때 호출되는 함수(콜백함수)
# # cv2.createTrackbar('H_min', 'Trackbar', 0, 180, on_trackbar)
# # cv2.createTrackbar('H_max', 'Trackbar', 0, 180, on_trackbar)
# # on_trackbar(0)

# # cv2.waitKey()
# # cv2.destroyAllWindows()

# # 2 =================================================================================
# # inRange 함수에 적용하기

# h_min = 0
# h_max = 74