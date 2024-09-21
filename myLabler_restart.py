import cv2, os, sys
import numpy as np
from glob import glob

# 0. 파일 목록 읽기(data폴더) *.jpg -> 리스트
# 1. 이미지 불러오기
# 2. 마우스 콜백함수 생성
# 3. 콜백함수 안에서 박스를 그리고, 박스 좌표를 뽑아낸다 (마우스 좌표2개)
#    참고로 YOLO에서는 박스의 중심좌표(x,y), w, h
# 4. 이미지 파일명과 동일한 파일명으로 (확장자만 떼고) txt 파일 생성
# 추가 기능0: 박스를 잘못 쳤을때 'c'를 누르면 현재 파일의 박스 내용 초기화
# 추가 기능1: 화살표(->)를 누르면 다음 이미지 로딩되고(1~4)
# 추가 기능2: 그린 박스 좌표들을 txt파일을 만들어서 저장하기 (기존에 txt파일이 있다면 덮어쓰기)
# 추가 기능3: 화살표(<-)를 눌렀을때 txt파일이 있다면 박스를 이미지 위에 띄워주기

#! 함수 정의 
#### 0. 파일 목록 읽기(data폴더) *.jpg -> 리스트
# return : io.Textfile 집합한 배열
def getImageList():
    baseDir = os.getcwd() # 현재 작업 directory 확인
    imgFoldr = os.path.join(baseDir,'images/') # 이미지들이 저장된 폴더로 directory 정의하기
    fileDirs = glob(os.path.join(imgFoldr,'*.jpg')) # 폴더 안에 있는 모든 이미지들을 불러오기
    
    return fileDirs

# 네모 그리기            
def drawRect(cpy, ptList, saved=False):
    # 그려낼 네모의 컬러와 두깨 지정
    c = (192, 192, 255) # 원의 색상 (연한 분홍색)
    line_c = (128, 128, 255) # 직선의 색상 (찐한 분홍색)
    lineWidth = 2 # 선 두깨
    # if saved: # 저장 된 좌표는 다른 색으로 표현하기
    #     c = (101, 147, 245) # 원의 색상 (연한 파랑색)
    #     line_c = (25, 25, 112) # 직선의 색상 (밤 하늘 색)
    #     lineWidth = 3 # 선 두깨
    
    # 사용자가 지정한 좌표값에 따라 레이블 직사각형 그리기
    for i in range(0,len(ptList)-1,2):
        cv2.rectangle(cpy, ptList[i], ptList[i+1], color=line_c, thickness=lineWidth)
    return cv2.addWeighted(img, 0.3, cpy, 0.7, 0) # 기존 이미지 위에 마우스로 그린 직사각형 종합해서 -> 새로운 이미지로 저장하기      
    
#### 3. 콜백함수 안에서 박스를 그리고, 박스 좌표를 뽑아낸다 (마우스 좌표2개)
def onMouse(event, x, y, flags, param):
    # 전역 변수 정의
    global ptList, cpy
    cpy = img.copy() # 이미지 위에 그릴 수 있는 레이어 만들기

    if event == cv2.EVENT_LBUTTONDOWN:
        ptList.append((x,y)) # 새로 그리는 좌표를 전역 변수 목록에 저장하기
        print(f'LButtonDown:', ptList)
    
    # Click and drag으로 마우스가 실시간으로 가르키는 두번째 좌표 가지고 네모 그리기 (마우스 좌 클릭으로 네모의 첫번째 좌표를 지정한 후)
    elif event == cv2.EVENT_MOUSEMOVE: 
        if len(ptList)==3 or len(ptList)==1: # 그릴 네모(들)의 첫번째 좌표를 지정했는지 확인 (새로 그린 네모를 지정하기 전에 직전에 그린 네모도 볼 수 있게끔 두 조건 주었음)
            ptList.append((x,y)) # 새로운 좌표를 전역 변수에 저장하고 
            cpy = drawRect(cpy, ptList) # 새로운 좌표를 반영한 이미지를 만들어서
            cv2.imshow('label',cpy) # 실시간으로 변해가는 네모 좌표를 화면에 띄우기
            print(f'MouseMove:', ptList)   
    
    # 마우스를 땔 때 네모의 두 번째 좌표를 임시적으로 저장하고, 전에 그려낸 네모가 있으면 지우기   
    elif event == cv2.EVENT_LBUTTONUP: 
        if len(ptList)>0: # (좌 클릭 후) 새로 네모를 그리는 중에 화면을 백지화 하는 경우, 네모가 좌 클릭으로 두 번째 좌표를 지정하는 것을 막기 위해 
            ptList.append((x,y)) 
        if len(ptList)>3: # 네모가 두 개 이상 지정 되는 것을 방지 하기 위해
            del ptList[0:2] # 새로운 네모를 지정한 후, 예전에 지정한 네모가 있으면 지우고       
        cpy = drawRect(cpy, ptList) # 새로 지정한 네모만 화면에 띄우기 위해 새로 이미지 지정하기  
        cv2.imshow('label', cpy)
        print(f'LButtonUp:', ptList)      

if __name__ == "__main__":
    #! 변수 정의 
    imgList = getImageList() 
    imgId = 0 # 이미지 파일 지정
    ptList = [] # 박스 좌표 목록
    cv2.namedWindow('label') # 마우스 움직임을 추적할 수 있는 창 만들기 
    
    #! 프로그램 실행 반복문
    running = True # 프로그램 종료 변수
    
    while running:
        #셋업
        ptList.clear()
        
        #### 1. 이미지 불러오기
        img = cv2.imread(imgList[imgId]) # 이미지 불러오기

        #### 2. 마우스 콜백함수 생성
        cv2.setMouseCallback('label', onMouse, [img]) # 마우스 움직임을 추적하기
        cv2.imshow('label', img)
        
        #### 추가 기능1: 우 방향키 (->)를 누르면 다음 이미지 로딩하기(1~4)
        key = cv2.waitKeyEx() # 프로그램 실행 명렁어들을 키보드로 입력
        
        if key== 0x270000:
            imgId = (imgId+1)%len(imgList) # 파일 목록에 끝에 도달했으면 다시 첫번째 파일로 돌아가기
            cv2.destroyAllWindows()
            cv2.namedWindow('label') # 마우스 움직임을 추적할 수 있는 창 만들기 
        
        elif key == ord('q'):
            running = False
            break

#### 모든 창들 닫고 프로그램 종료 ####
print('Exiting out of the program')   
cv2.destroyAllWindows()

