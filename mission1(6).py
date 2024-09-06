import cv2, sys

#이미지 불러오기
# 대상이미지 01.png
# png파일을 읽을때는 cv2.IMREAD_UNCHANGED 적용필요!!
src = cv2.imread('misson/01.png', cv2.IMREAD_UNCHANGED)
dst = cv2.imread('misson/01.png', cv2.IMREAD_UNCHANGED)

# 파일이 정상적으로 읽히지 않았다면
if src is None:
    sys.exit("Image Load failed!")
    
# Experiment with FastNlMeansDenoising Parameters:
# h: Increase this value to reduce noise.
# templateWindowSize: Adjust this value to control the size of the search window for similar patches.
# searchWindowSize: Adjust this value to control the size of the search window for similar patches.
denoise = cv2.fastNlMeansDenoisingColored(src,None,10,10,21,21)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)
h_min = 0
h_max = 50
mask = cv2.inRange(hsv,(h_min,0,100),(h_max,255,255))

# cv2.imshow('denoise',denoise)
cv2.copyTo(denoise,mask,dst)
cv2.imshow('src',src)
cv2.imshow('mask', mask)
cv2.imshow('denoise', denoise)
cv2.imshow('dst',dst) 
cv2.waitKey()
cv2.destroyAllWindows()