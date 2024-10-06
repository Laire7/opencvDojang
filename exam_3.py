# 주어진 이미지 파일 img.jpg에서 얼굴을 사각형으로 표시하는 코드를 작성하세요.

# 아래 예시처럼 얼굴에 사각형을 표시 후 이미지를 확인할 수 있게 띄워주세요.

import cv2
import matplotlib.pyplot as plt

# img = cv2.imread('img.jpg')
# img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 네모 그리기            
def drawRect(img, cpy, ptList, saved=False):
    # 그려낼 네모의 컬러와 두깨 지정
    c = (101, 147, 245) # 원의 색상 (연한 분홍색)
    line_c = (255, 0, 0) # 직선의 색상 (찐한 분홍색)
    lineWidth = 2 # 선 두깨
    
    # 사용자가 지정한 좌표값에 따라 레이블 직사각형 그리기
    for i in range(0,len(ptList)-1,2):
        cv2.rectangle(cpy, ptList[i], ptList[i+1], color=line_c, thickness=lineWidth)
    return cv2.addWeighted(img, 0.3, cpy, 0.7, 0) # 기존 이미지 위에 마우스로 그린 직사각형 종합해서 -> 새로운 이미지로 저장하기   
    
# 3. 콜백함수 안에서 박스를 그리고, 박스 좌표를 뽑아낸다 (마우스 좌표2개)
def onMouse(event, x, y, flags, param):
    #! 변수 정의
    global cpy, ptList, img
    cpy = img.copy()

    # ! 마우스 움직임에 따라 좌표 그리기
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(ptList)==0 or len(ptList)==2:
            ptList.append((x,y)) # 새로 그리는 좌표를 전역 변수 목록에 저장하기
    
    # Click and drag으로 마우스가 실시간으로 가르키는 두번째 좌표 가지고 네모 그리기 (마우스 좌 클릭으로 네모의 첫번째 좌표를 지정한 후)
    elif event == cv2.EVENT_MOUSEMOVE: 
        if len(ptList)==1 or len(ptList)==3: # 그릴 네모(들)의 첫번째 좌표를 지정했는지 확인 (새로 그린 네모를 지정하기 전에 직전에 그린 네모도 볼 수 있게 두 조건을 줬다)
            ptList.append((x,y)) # 새로운 좌표를 전역 변수에 저장하고
            cpy = drawRect(img,cpy, ptList) # 새로운 좌표를 반영한 이미지를 만들어서
            cv2.imshow('label',cpy) # 실시간으로 변해가는 네모 좌표를 화면에 띄우기
            ptList.pop() # 마우스를 띄우지 않은면, 좌표 지우기
    
    # 마우스를 땔 때 네모의 두 번째 좌표를 임시적으로 저장하고, 전에 그려낸 네모가 있으면 지우기   
    elif event == cv2.EVENT_LBUTTONUP: 
        if len(ptList)>0: # (좌 클릭 후) 새로 네모를 그리는 중에 화면을 백지화 하는 경우, 네모가 좌 클릭으로 두 번째 좌표를 지정하는 것을 막기 위해
            ptList.append((x,y)) # 새로운 좌표를 전역 변수에 저장하고
            if len(ptList)==4:
                del ptList[:-2] # 새로운 네모를 지정한 후, 예전에 지정한 네모가 있으면 지우기       
            cpy = drawRect(img, cpy, ptList)
            cv2.imshow('label',cpy) 
    
    return cpy

def createImgWithBox():
    global ptList
    img2 = drawRect(img, cpy, ptList)
    cv2.imwrite('img2.jpg', img2)
    img2_read = cv2.imread('img2.jpg')
    # cv2.imshow('img2', img2_read)
    img2_rgb = cv2.cvtColor(img2_read, cv2.COLOR_BGR2RGB)
    plt.imshow(img2_rgb)
    plt.axis('off')
    plt.show()
        
#! 메인 함수 샐행
if __name__ == "__main__":
    #! 변수 정의
    cpy = None 
    ptList = [] # 박스 좌표 목록
    saving = False # 사용자가 그리는 도중, 좌표를 저장하고 싶을 때
    cv2.namedWindow('label') # 마우스 움직임을 추적할 수 있는 창 만들기 
    
    #! 프로그램 실행 반복문
    running = True # 프로그램 종료 변수
    
    while running:
        #셋업
        ptList.clear()
        
        # 1. 이미지 불러오기
        img = cv2.imread('img.jpg') # 이미지 불러오기
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imshow('label', img)
        
        #! 새로운 이미지 띄우고 난 후, 좌표 그리기 반복문
        while running:
            # 2. 마우스 콜백함수 생성
            cv2.setMouseCallback('label', onMouse) # 마우스 움직임을 추적하기              
            
            #! 추가 기능 설정
            key = cv2.waitKeyEx() # 프로그램 실행 명렁어들을 키보드로 입력
            # 추가 기능0: 박스를 잘못 쳤을때 'c'를 누르면 현재 파일의 박스 내용 초기화
            if key == ord('c'):
                ptList.clear()
                cv2.imshow('label', img)
            
            elif key == ord('s'):
                cv2.destroyWindow('label')
                createImgWithBox()
                # plt.imshow('img with face labeled', img2)
                # plt.axis('off')
                # plt.show()
                running = False
                break
                    
            #! 프로그램 종료하기    
            elif key == ord('q'):
                running = False
                break


#### 모든 창들 닫고 프로그램 종료 ####
print('Exiting out of the program')
cv2.destroyAllWindows()
