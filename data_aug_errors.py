import cv2, sys
import numpy as np
import os
from glob import glob

# org = cv2.imread('org/pen_white.jpg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('org', org)

# dataDirList = {}
# dataDirList[-1] = ["original"]
# print(dataDirList.get(-1))

# h, w = img.shape[:2]
# print(f'h:{h}, w:{w}')
def getImgList():
    baseDir = os.getcwd() # 현재 작업 directory 확인
    imgFoldr = os.path.join(baseDir,'org/') # 이미지들이 저장된 폴더 확인하기
    fileDirs = glob(os.path.join(imgFoldr,'*.jpg')) # 폴더 안에 있는 모든 이미지들을 불러오기    
    return fileDirs

fileDirs = getImgList()


img = cv2.imread(fileDirs[0])
dir= cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()