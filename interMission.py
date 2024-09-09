import cv2, sys
import numpy as np
import math

# 마우스 콜백 함수 구현
# 마우스에서 이벤트가 발생하면서 호출되는 함수
# 버튼 클릭, 마우스 좌표를 이동

pt1 = (0,0)
pt2 = (0,0)
polyPt = []
running = True

def mouse_callback(event, x, y, flags, param):
    #global img 
    img = param[0]
    global polyPt, pt1, pt2
    # 기본 waitKey + Extension키 입력까지 받아들임
    key = cv2.waitKeyEx(1) #timeout=30ms
    #waitKeyEx waitKey와 비슷하지만, waitKey가 인식하지 못하는 특수키들을 받아 4자리->6자리 용량을 늘린다, 여기에서는 방향키를 받는다 (다른 키 예.PageDown)
    #waitKey 'q' Esc는 ASCII가 있는 key들          
    if event==cv2.EVENT_LBUTTONDOWN:
        if(flags & cv2.EVENT_FLAG_SHIFTKEY):
            cv2.circle(img, (x,y),1,(255,0,0),1)
            polyPt.append([x,y])
            print(polyPt)
        elif(len(polyPt)==0):
            pt1 = (x,y)
    elif not(flags and cv2.EVENT_FLAG_SHIFTKEY) and len(polyPt)!=0:
        numpyPt = np.array(polyPt, np.int32)
        cv2.polylines(img, [numpyPt], True, (255,0,0),1,cv2.LINE_AA)
        polyPt.clear()
    elif event==cv2.EVENT_LBUTTONUP:
        if(len(polyPt)==0):
            pt2 = (x,y)
            cv2.rectangle(img, pt1, pt2, (100,100,100),2)
    elif event==cv2.EVENT_RBUTTONDOWN:
        pt1 = (x,y)
        cv2.circle(img, (x,y), 1, (0,175,0),1)        
    elif event == cv2.EVENT_RBUTTONUP: 
        pt2 = (x,y) 
        radius = max((pt2[0]-pt1[0]),(pt2[1]-pt1[1]))
        cv2.circle(img, pt1, radius, (0,175,0),1)

def resize():
    #blur 필터 넣기
    blur = cv2.blur(img, (9,9))
    cv2.imshow('blur', blur)
    #화면 사이즈 줄이기
    reduce = cv2.resize(blur, (0,0), fx=0.25, fy=0.25, interpolation=cv2.INTER_LANCZOS4)
    cv2.imshow('reduce', reduce)
    #화면 사이즈 다시 키우기 설정(해상도입력X)
    dst1 = cv2.resize(reduce, (0,0), fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
    dst2 = cv2.resize(reduce, (0,0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
    dst3 = cv2.resize(reduce, (0,0), fx=4, fy=4, interpolation=cv2.INTER_LANCZOS4)
    #새로운 이미지 출력
    cv2.imshow('Inter_CUBIC', dst1)
    cv2.imshow('INTER_NEAREST', dst2)
    cv2.imshow('INTER_LANCZOS4', dst3)

# 흰색 캔버스를 생성
# img = np.zeros((512,512,3), np.uint8)+ 255
img = np.ones((512, 512, 3), np.uint8) * 255
cv2.namedWindow('img')
cv2.imshow('img', img)

#메인에서 setMouseCallback함수를 실행하면서 콜백 함수를 지정
while running:
    key = cv2.waitKey(30)
    if key == 27:
        running=False
        break
    cv2.setMouseCallback('img', mouse_callback, [img])
    cv2.imshow('img', img)
resize()
cv2.waitKey()
cv2.destroyAllWindows()
