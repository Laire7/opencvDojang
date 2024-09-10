#1. ERROR
# corners = [(0,1), (2,3)]
# print(type(corners[0]))
# print(corners[0])

#2. ERROR
# list = [0,1,2,3]
# print(list[-2]%len(list))

#3. ERROR 
# import os
# from glob import glob

# def getImageList():
#     #현재 작업 디렉토리 확인
#     basePath = os.getcwd() # 현재 작업 directory 확인
#     dataPath = os.path.join(basePath,'images/')
#     # print(dataPath)
#     fileNames = glob(os.path.join(dataPath,'*.jpg'))
#     #print(fileNames)
    
#     return fileNames

# fileNames = getImageList()

# f = 0

# fileName =  list(os.path.splitext(fileNames[0]))
# print(fileName)
# print(type(fileName))
# print(fileName[0])
# print(type(fileName[0]))
# result = (lambda f: list(os.path.splitext(fileNames[f]))[0])(f)
# print(result)
# print(type(result))
# result2 = (lambda f: list(os.path.splitext(fileNames[f]))[0])(f)+'.txt'
# print(result2)
# print(type(result2))

#4. ERROR
import os
from glob import glob

def getImageList():
    #현재 작업 디렉토리 확인
    basePath = os.getcwd() # 현재 작업 directory 확인
    dataPath = os.path.join(basePath,'images/')
    # print(dataPath)
    fileNames = glob(os.path.join(dataPath,'*.txt'))
    #print(fileNames)
    
    return fileNames

fileNames = getImageList()

f = 0
ptList = []

fileName = (lambda f: list(os.path.splitext(fileNames[f]))[0])(f)+'.txt'
print(fileName)

# readFile = open(fileNames[f], 'r').read()
# # print(readFile)
# print(readFile)

# numList = []
# # for i, ch in enumerate(readFile[2:-2:]):
# #     print(f'i:{i}, ch:{ch}')
# #     if(ch.isdigit()):
# #         print(f'{ch} is digit')
# num = ''
# print(len(readFile))
# for i in range(2,len(readFile)-2):
#     # print(f'i:{i}, readFile[i]: {readFile[i]}')
#     if(readFile[i].isdigit()):
#         num +=readFile[i]
#     if(not readFile[i+1].isdigit() and num):
#         # print(f'num:{num}')
#         numList.append(int(num))
#         num = ''
# # print(numList)
# # startPt, endPt = tuple(numList[0:2]), tuple(numList[1:3])
# # print(f'startPt:{startPt}, endPt:{endPt}')
# ptList.insert(0, tuple(numList[0:2]))
# ptList.insert(1, tuple(numList[1:3]))
# # print(ptList)
# # if(len(ptList)==0):
# #     ptList.append(tuple(numList[0:2]), tuple(numList[1:3]))
# # else:
# #     ptList[0], ptList[1] = tuple(numList[0:2]), tuple(numList[1:3])
# # print(ptList)
# #     if(not readFile[i+1].isdigit()):
# #         print(f'num:{num}')
# #         numList.append(int(num))
# #         num=''
# # print(numList)
# # ptList = openFile.split("," or " " or "(" or ")")
# # print(openFile.split("), ("))
# # print(ptList)
# # print(type(ptList))
# # print(list(openFile))
# # print(type(list(openFile)))
# # print(enumerate(openFile))
# # print(type(enumerate(openFile)))
# # for i, pt in enumerate(list(openFile)): 
# #     print(f'i:{i}, pt:{pt}')
# # print(f'ptList[0]: {ptList[0]}, ptList[1]: {ptList[1]}')
# # (lambda fileName: open(fileName, 'r').read())(fileName)