# 파일에서 이미지를 읽어서 출력

import cv2

fileName = 'cat.jpg'

#이미지를 불러오는 함수
img = cv2.imread(fileName)

#예외처리 루틴 : 이미지를 읽어오지 못했을 때 
if img is None:
    print("Image load fail")
    sys.exit()