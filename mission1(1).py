import cv2, sys

#이미지 불러오기
# 대상이미지 01.png
# png파일을 읽을때는 cv2.IMREAD_UNCHANGED 적용필요!!
src = cv2.imread('misson/01.png', cv2.IMREAD_UNCHANGED)
dst = cv2.imread('misson/01.png', cv2.IMREAD_UNCHANGED)

# 파일이 정상적으로 읽히지 않았다면
if dst is None:
    sys.exit("Image Load failed!")

# hsv 색공간에서 영역을 검출해서 합성
# src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
# dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
# h: 50~70, s:150~255, v:0~255
# mask = cv2.inRange(hsv,(0,0,100),(255,255,255))

# 1. Adjust Bilateral Filter Parameters:
# d: Increase this value to consider pixels further away from the central pixel, which can help preserve edges and details in the buildings.
# sigmaColor: Increase this value to reduce noise in color.
# sigmaSpace: Decrease this value to focus on local details in the buildings.


# 2. Experiment with FastNlMeansDenoising Parameters:
# h: Increase this value to reduce noise.
# templateWindowSize: Adjust this value to control the size of the search window for similar patches.
# searchWindowSize: Adjust this value to control the size of the search window for similar patches.
denoise = cv2.fastNlMeansDenoisingColored(src,None,10,10,21,21)

hsv = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)
h_min = 0
h_max = 100
mask = cv2.inRange(hsv, h_min, h_max)
cv2.imshow('mask', denoise)

# 마스크 연산은 마스크 크기 만큼만
# crop은 src배열을 부르는 또 따른 이름
cv2.copyTo(denoise,mask,dst)
cv2.imshow('src',src)
cv2.imshow('dst',dst) 
cv2.waitKey()
cv2.destroyAllWindows()