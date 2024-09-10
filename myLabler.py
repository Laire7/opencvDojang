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
# 추가 기능2: 화살표(<-)를 눌렀을때 txt파일이 있다면 박스를 이미지 위에 띄워주면

# YOLO
# def 
#     x_center =
#     y_center =
#     width =
#     height = 

# 네모 만들기
# corners : 좌표(startPt, endPt)
# 2개 좌푤글 이용해서 직사각형 그리기
def drawROI(img, ptList):
    # 이미지 복사해서 레이어를 하나 추가 (가이드 라인과 모서리 포이트를 추가로 그려주는)
    # 박스를 그릴 레이어를 생성 : cpy
    cpy = img.copy() # deep copy
    # 컬러 지정
    c = (192, 192, 255) #원의 색상 (연한 분홍색)
    line_c = (128, 128, 255) #직선의 색상 (찐한 분홍색)
    lineWidth = 2 # 선 두깨

    for i in range(0,len(ptList),2):
        cv2.rectangle(cpy, ptList[i], ptList[i+1], color=line_c, thickness=lineWidth)
    # alpha=0.3, beta=0.7, gamma=0
    disp = cv2.addWeighted(img, 0.3, cpy, 0.7, 0)  
    return disp

def getPts(line):
    global ptList
    numList = []
    num = ''
    print(len(line))
    for i in range(2,len(line)-2):
        # print(f'i:{i}, readFile[i]: {readFile[i]}')
        if(line[i].isdigit()):
            num +=line[i]
        if(not line[i+1].isdigit() and num):
            numList.append(int(num))
            num = ''
    ptList.insert(0, tuple(numList[0:2]))
    ptList.insert(1, tuple(numList[1:3]))

# 데이터 집합
def getImageList():
    #현재 작업 디렉토리 확인
    basePath = os.getcwd() # 현재 작업 directory 확인
    dataPath = os.path.join(basePath,'images/')
    # print(dataPath)
    fileNames = glob(os.path.join(dataPath,'*.jpg'))
    #print(fileNames)
    
    return fileNames

# 마우스 콜백 함수 정의
def onMouse(event, x, y, flags, param):
    global ptList, img, cpy, txtWrData
    cpy = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:
        ptList.append((x,y))
    elif event == cv2.EVENT_LBUTTONUP:
        if len(ptList)>0:
            ptList.append((x,y))
        if len(ptList)>3:
            del ptList[0:2]       
        cpy = drawROI(cpy, ptList)
        cv2.imshow('label', cpy)
        print(ptList)
        txtWrData = str(ptList)
    elif event == cv2.EVENT_MOUSEMOVE:
        if len(ptList)==3 or len(ptList)==1:
            ptList.append((x,y))
            cpy = drawROI(cpy, ptList)
            ptList.pop()    
            cv2.imshow('label',cpy)
        
# 마우스가 눌리지 않으면 좌표값은 없음
fileNames = getImageList()
ptList = []
txtWrData = ''
f = 0
running = True

while running:
    img = cv2.imread(fileNames[f])
    cv2.namedWindow('label')
    cv2.setMouseCallback('label', onMouse, img)
    cv2.imshow('label', img)
    ptList.clear()

    while running:
        key = cv2.waitKeyEx()
        if key==27:
            running = False
            break
        elif key==ord('s'):
            if(len(ptList)>1):
                fileName, ext = os.path.splitext(fileNames[0])
                txtFileName = fileName + '.txt'
                f = open(txtFileName, 'w') # 만약 파일이 있으면, 다시 쓰기
                # print("before write txt : ", txtWrData)
                f.write(txtWrData)
                f.close()
            else:
                print(f'No rectangles to save!')
        elif key==ord('c'):
            ptList.clear()
            cv2.imshow('label', img)
        # left key
        elif key == 0x250000:
            txtFileName = (lambda f: list(os.path.splitext(fileNames[f]))[0])(f)+'.txt'
            print(txtFileName)
            print(type(txtFileName))
            if(os.path.exists(txtFileName)):
                # print(fileName, "exists")
                line = open(txtFileName, 'r').read()
                print(f'saved pt: {line}')
                if(len(ptList)>1):
                    print(f"Old pt1:{ptList[0]}, pt2:{ptList[1]}")
                else:
                    print(f'No new box drawn')
                getPts(line)
                print(f'New pt1:{ptList[0]}, pt2: {ptList[1]}')
                # print(f"New pt1:{ptList[0]}, pt2:{ptList[1]}")
            #     cpy = drawROI(cpy, ptList)
            #     cv2.imshow('label', cpy) 
            #     cv2.setMouseCallback('label', onMouse, cpy)
            else:
              print("No saved rectangle")                 
        # right key
        elif key== 0x270000:
            f = (f+1)%len(fileNames)
            break  
cv2.destroyAllWindows()