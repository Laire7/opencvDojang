import sys
import numpy as np
import cv2

hmin=50
hmax=70
smin=150
smax=255

#동영상 파일명
fileName1 = "data2/woman.mp4"
fileName2 = "data2/raining.mp4"

#동영상 불러오기
cap1 = cv2.VideoCapture(fileName1) # 1번영상 불러오기
cap2 = cv2.VideoCapture(fileName2) # 2번영상 불러오기

#동영상을 열지 못하면 해당 오류에 대해 출력하기
if not cap1.isOpened():
    sys.exit('video1 open failed')
    
if not cap2.isOpened():
    sys.exit('video2 open failed')

#동영상 읽기
ret1, frame1 = cap1.read()
ret2, frame2 = cap2.read()
hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV) #동영상 원본(BGR)->색감 조정하기 쉬운 HSV로 바꾸기
# h: 50~70, s:150~255, v:0~255
mask = cv2.inRange(hsv,(hmin,smin,0),(hmax,smax,255))
cv2.copyTo(frame2, mask, frame1)


#동영상 종료하기
cap1.release()
cap2.release()
cv2.destroyAllWindows()