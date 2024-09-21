import cv2, sys, shutil
import numpy as np
import os
from glob import glob

# 1. 배경 : 흰색 책상, 우드 테이블
# 2. 데이터 증식 조건
#    2.0 스마트폰으로 사진 촬영 후 이미지 크기를 줄여주자 (224px x 224px)
#           대상물 촬영을 어떻게 해야할지 확인
#    2.1 rotate : 회전(10~30도)범위 안에서 어느 정도 각도를 넣어야 인식이 잘되는가?
#    2.2 hflip, vflip : 도움이 되는가? 넣을 것인가?
#    2.3 resize, crop : 가능하면 적용해 보자.
#    2.4 파일명을 다르게 저장 cf) jelly_wood.jpg, jelly_white.jpg
#        jelly_wood_rot_15.jpg, jelly_wood_hflip.jpg,jelly_wood_resize.jpg
#    2.5 클래스 별로 폴더를 생성
#    2.6 데이터를 어떻게 넣느냐에 따라 어떻게 동작되는지 1~2줄로 요약

# 구성 순서
# 1. 촬영한다.
# 2. 이미지를 컴퓨터로 복사, resize한다
# 3. 육안으로 확인, 이렇게 사용해도 되는가?
# 4. 함수들을 만든다, resize, rotate, hflip, vflip (연습 겸), crop
#      원본 파일명을 생성하는 기능은 모든 함수에 있어야 한다 (함수)
#      함수 각자 -> 한번에 모듈화, 함수 묶는 것
# 5. 단일 함수들 검증
# 6. 함수를 활용해서 기능 구현
# 7. 테스트(경우의수)
# 8. 데이터셋을 teachable machine사이트에 올려서 테스트
# 9. 인식이 잘 안되는 케이스를 분석하고 케이스 추가 1~8에서 구현된 기능을 이용

###### 전역 변수 목록 #######

####### 함수 목록 #######

### 이미지들 불러오기 ###
def getImgList():
    baseDir = os.getcwd() # 현재 작업 directory 확인
    print("current directory:", os.getcwd())
    imgFoldr = os.path.join(baseDir,'org/') # 이미지들이 저장된 폴더로 directory 바꾸기
    fileDirs = glob(os.path.join(imgFoldr,'*.jpg')) # 폴더 안에 있는 모든 이미지들을 불러오기    
    return fileDirs

### 이미지 파일 생성하기 ###
def genData(orgPath, transformList, ext):
    # 이미지 파일 생성할 변수
    dataDirList = {}
    basePath = os.getcwd()
    # 이미지 파일 경로 지정하기
    dataPath = os.path.join(os.getcwd(), 'DataAug') # 생성한 파일들 별도 폴더에다가 저장하기
    obj = str(orgPath).split(os.path.join(os.getcwd(), 'org\\'))[1].split("_", 1)[0] # 분류 할 오브젝트 정의하고
    dataPath = os.path.join(dataPath, obj) #분류 할 오브젝트 폴더에 따라 저장하기
    # 폴더가 존재한다면
    if os.path.isdir(dataPath):
        shutil.rmtree(dataPath)
    # os.mkdir(dataPath) # print(path, "폴더 만들기 성공!")
    os.makedirs(dataPath,exist_ok=True)
    os.chdir(dataPath) # go inside directory   
    orgFileName = os.path.splitext(os.path.basename(orgPath))[0] # 원본 파일 (분류 할 오브젝트 + 배경을 정의한) 
    dataPath = os.path.join(dataPath, orgFileName)
    img = cv2.imread(orgPath)
    dataDirList[-1] = [list((dataPath, img))] # 이미지 변환을 주기 전, 원본 불러오기 
    for ord, trans in enumerate(transformList):
        for prevTrans in dataDirList.get(ord-1): 
            prevTrans[0] += "_" + trans
            # delPrevData(dataPath, trans)
            if(trans == "rotate"):
                step = 30
            else:
                step = 1
            dataLoop = genTransformData(prevTrans[1], prevTrans[0], "rotate", step)
            dataDirList[ord] = dataLoop
    #이미지 변환을 주고 난 후, 이미지들 뒤에 .jpg extension 붙이고 생성하기
    for file in dataDirList.get(len(transformList)-1):
        file[0] += ext
        cv2.imwrite(str(file[0]), file[1])
    os.chdir(basePath) # go back inside orgPath directory
    # print(f'dataDirList:{dataDirList}')
    # cv2.imwrite(str(dataDirList[-1][0][0]), dataDirList[-1][0][1])
### 이미지 변환 함수 목록 ###
def resize224(img): # 이미지를 ML 프로그램이 요구하는 사이즈에 맞춘다
    img_resize224 = cv2.resize(img, (224,224))
    return img_resize224

def rotate(img, angle=30):
    h, w = img.shape[:2]
    centerPt = (w/2, h/2)
    rotate_matrix = cv2.getRotationMatrix2D(centerPt, angle, 1)
    img_rotate = cv2.warpAffine(img, rotate_matrix, (w,h))
    return img_rotate

def hflip(img):
    img_hflip = cv2.flip(img, 0)
    return img_hflip

def vflip(img):
    img_vflip = cv2.flip(img, 1)
    return img_vflip

def resize(img, factor=2):
    if factor <=1:
        interpolation = cv2.INTER_AREA
    else:
        interpolation = cv2.INTER_LANCZOS4
    img_resize = cv2.resize(img, (0,0), fx=factor, fy=factor, interpolation=cv2.INTER_AREA)
    return img_resize

def crop(img):
    h, w = img.shape[:2]
    img_crop = img[int(round(h/4)):int(round(3*h/4)), int(round(w/4)):int(round(3 * w/4))]
    return img_crop

### 이미지 생성 함수 ###
def genTransformData(img, dataPath, trans, loopStep):
    dataLoop = []
    if trans == "rotate":
        stopLoop = 360  
        if not loopStep:
            loopStep = 20
    else:
        stopLoop = 1
    for loop in range(loopStep, stopLoop, loopStep):
        img = chooseTransform(img, trans)        
        dataLoop.append(list((dataPath+str(loop), img))) 
    return dataLoop

### 이미지 변환 고르고 기록하기 ###
def chooseTransform(img, transformFx): 
    match transformFx:
        case "rotate":
            return rotate(img)
        case "hflip":
            return hflip(img)
        case "vflip":
            return vflip(img)
        case "resize":
            return resize(img)
        case "crop":
            return crop(img)
        case _ :
            print(f'Returning original')
            return img
             
####### 프로그램 실행 #######
## 원본 이미지 불러오기
imgDirs = getImgList()

## 변환 적용한 함수들 저장하기
for num, img in enumerate(imgDirs):
    transformList = ["rotate", "hflip"]
    genData(imgDirs[num], transformList, ".jpg")
    
# 이미지 파일 생성 잘 되는지 확인



