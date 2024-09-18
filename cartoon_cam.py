# 카툰 필터 카메라

import sys
import numpy as np
import cv2


def cartoon_filter(img):
    h, w = img.shape[:2]
    img2 = cv2.resize(img, (w//2, h//2))

    blr = cv2.bilateralFilter(img2, -1, 20, 7)
    # edge = cv2.Canny(img2, 80, 120) # black with white borders
    edge = 255 - cv2.Canny(img2, 80, 120) # white with black borders
    # 80: pixel gradient lower than 80 is rejected
    # 120: pixel gradient higher than 120 is made into an edge
    # pixels between 80-120 is made into an edge only if it is connected to a pixel that is above 120
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR) # 

    dst = cv2.bitwise_and(blr, edge) 
    dst = cv2.resize(dst, (w, h), interpolation=cv2.INTER_NEAREST)

    return dst


def pencil_sketch(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blr = cv2.GaussianBlur(gray, (0, 0), 3)
    dst = cv2.divide(blr, gray, scale=255)
    return dst

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

fileName = 'data/vtest.avi'
# VideoCapture 클래스 객체 생성 + 생성자가 호출 (파일열기)
cap = cv2.VideoCapture(fileName)

if not cap.isOpened():
    print('video open failed!')
    sys.exit()

cam_mode = 1

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if cam_mode == 1:
        frame = cartoon_filter(frame)
    elif cam_mode == 2:
        frame = pencil_sketch(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)

    if key == 27:
        break
    elif key == ord(' '):
        cam_mode += 1
        if cam_mode == 3:
            cam_mode = 0


cap.release()
cv2.destroyAllWindows()
