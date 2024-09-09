import cv2, sys
import numpy as np
import matplotlib.pyplot as plt

# 마우스 콜백 함수 구현
# 마우스에서 이벤트가 발생하면서 호출되는 함수

# 새로운 마우스 이벤트가 발생할 때 마다 해당 정보가 지워지지 않게 전역 변수 사용
pt1 = (0,0)
pt2 = (0,0)
polyPt = []

#마우스 행동 하나하나에 프로그램 행동 지정하기
def mouse_callback(event, x, y, flags, param):
    img = param[0]
    global polyPt, pt1, pt2
    # 기본 waitKey + Extension키 입력까지 받아들임
    key = cv2.waitKeyEx(1) #timeout=30ms
    #waitKeyEx waitKey와 비슷하지만, waitKey가 인식하지 못하는 특수키들을 받아 4자리->6자리 용량을 늘린다, 여기에서는 방향키를 받는다 (다른 키 예.PageDown)
    #waitKey 'q' Esc는 ASCII가 있는 key들          
    
    #다각형 그리기
    # Shift + 왼쪽 마우스 클릭
    # 왼쪽 마우스 클릭 할 때 마다->다각형에 새로운 점 추가
    # Shift 키를 때는 순간, 다각형이 그려진다
    if event==cv2.EVENT_LBUTTONDOWN:
        if(flags & cv2.EVENT_FLAG_SHIFTKEY):
            #flags는 mouse 이벤트가 발생할 때 keyboard 입력키도 확인 해준다
            cv2.circle(img, (x,y),1,(255,0,0),-1)
            #다격형에 새로운 점 추가
            polyPt.append([x,y]) 
        # 네모 그리기 (왼쪽 마우스 클릭 Only)
        elif(len(polyPt)==0):
            pt1 = (x,y)
    elif not flags and len(polyPt)!=0: #Shift 키를 때고 난 뒤, 모양 출력
        numpyPt = np.array(polyPt, np.int32) #다각형 점들의 배열을 >> cv2가 읽을 수 있는 np.int32 값들로 바꾸고, np.array로 변환!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        cv2.polylines(img, [numpyPt], True, (255,0,0),1,cv2.LINE_AA)
        polyPt.clear()
    # 네모 그리기 (왼쪽 마우스 클릭 Only)
    #  마우스를 땔 때, 마우스를 땐 위치에 따라 네모가 그려진다
    elif event==cv2.EVENT_LBUTTONUP:
        if(len(polyPt)==0):
            pt2 = (x,y) # 마우스 때는 위치 -> 네모의 반대편 점으로 저장
            cv2.rectangle(img, pt1, pt2, (100,100,100),2)
    #동그라미 그리기 (오른쪽 마우스 클릭 Only)
    elif event==cv2.EVENT_RBUTTONDOWN:
        pt1 = (x,y) 
        cv2.circle(img, (x,y), 1, (0,175,0),1)
    # 오른쪽 마우스 땐 위치에 따라 반지름을 지정하면서 원 그리기        
    elif event == cv2.EVENT_RBUTTONUP: 
        pt2 = (x,y) 
        radius = max((pt2[0]-pt1[0]),(pt2[1]-pt1[1])) # 마우스를 땐 위치에 따라 원의 반지름을 그리기
        cv2.circle(img, pt1, radius, (0,175,0),1)

# Interpolation 함수들 비교하기
#  이미지/영상을 줄이고 다시 키울 때, 중간에 사라진 정보를 주변 픽셀 값들 어떻게 사용하는가에 따라 원래데로 "복구하는" 방법들 탐색
#  Inter_Area VS Inter_Lancos4, Inter_Cubic, Inter_Nearest 
#  영상 처리 위해 유용함
def resize():
    #blur 필터 넣기
    blur = cv2.blur(img, (9,9))
    cv2.imshow('blur', blur)
    #화면 사이즈 줄이기
    reduce = cv2.resize(blur, (0,0), fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)
    cv2.imshow('reduce', reduce)
    #화면 사이즈 다시 키우기 설정(해상도입력X)
    area = cv2.resize(reduce, (0,0), fx=4, fy=4, interpolation=cv2.INTER_AREA)
    lanc = cv2.resize(reduce, (0,0), fx=4, fy=4, interpolation=cv2.INTER_LANCZOS4)
    cubic = cv2.resize(reduce, (0,0), fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
    near = cv2.resize(reduce, (0,0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
    #다시 키운 이미지 저장
    cv2.imwrite('area.jpg', area)
    cv2.imwrite('lanc.jpg', lanc)
    cv2.imwrite('cubic.jpg', cubic)
    cv2.imwrite('near.jpg', near)
    #다시 키운 이미지 출력
    cv2.imshow('INTER_AREA', area)
    cv2.imshow('INTER_LANCZOS4', lanc)
    cv2.imshow('Inter_CUBIC', cubic)
    cv2.imshow('INTER_NEAREST', near)

# 흰색 캔버스를 생성
# img = np.zeros((512,512,3), np.uint8)+ 255
img = np.ones((512, 512, 3), np.uint8) * 255
cv2.namedWindow('img')
cv2.imshow('img', img)

#메인에서 setMouseCallback함수를 실행하면서 콜백 함수를 지정
running = True
while running:
    key = cv2.waitKey(1)
    if key == 27:
        running=False
        break
    cv2.setMouseCallback('img', mouse_callback, [img])
    cv2.imshow('img', img)    
resize()
cv2.waitKey()
cv2.destroyAllWindows()