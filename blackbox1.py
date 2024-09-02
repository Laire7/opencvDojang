# 1. 60초에 동영상 한 개가 생성되도록 한다.
import cv2, sys
import numpy as np
import time

# specify the path for the directory – make sure to surround it with quotation marks
basic_path = 'C:/Users/SBA/opencvDojang/'

isWEBCAM = False
# webcam인 경우 카메라 번호를 입력
if isWEBCAM: 
    cap = cv2.VideoCapture(0)
else:
    video_fileName = basic_path + 'data/vtest.avi'
    cap = cv2.VideoCapture(video_fileName)
    # print("retrievedFile!!!")

# Parameters
capture_duration = 3  # Duration of the video in seconds
fps = int(cap.get(cv2.CAP_PROP_FPS))      # Frames per second
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frameSize = (width,height)

def createVideo():
    cap = cv2.VideoCapture(video_fileName)
    # Create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out60_color = cv2.VideoWriter('record0.mp4', fourcc, fps, frameSize)
    out60_grayscale = cv2.VideoWriter('record0.mp4', fourcc, fps, frameSize, isColor=False)
    
    # Generate and write frames
    start_time = time.time()
    while( int(time.time() - start_time) < capture_duration ):

        # 한 프레임 영상 읽어오기
        retval, frame = cap.read()
    
        # 카메라에서부터 영상이 정상적으로 전달되었는지 확인
        if not retval:
            print("Video not retrieved")
            break
        # 동영상 녹화기에 프레임 전달
        out60_color.write(frame)
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out60_grayscale.write(grayFrame)

        cv2.imshow('frame', frame)
        cv2.imshow('gray', grayFrame)
        delay = int(1000/fps)
        
        # if cv2.waitKey(delay) == 27:
        #     break

    cap.release()
    out60_color.release()
    out60_grayscale.release()
    cv2.destroyAllWindows()

######### 파일명은 20240902-161903.avi


# 2. 폴더 생성은 날짜 + 현재 시간
# 20240902 - 1619     00분~59분 
# 한 시간 마다 폴더 생성
import os
# import time
from datetime import datetime

folder_duration = 5
loop = 0
# while (loop<3):
while 1:
    start_time = time.time()
    def reformatDateTime():
        now = datetime.now()
        print(now)
        now_toStr = now.strftime("%Y%m%d-%H%M"+str(loop)) 
        return now_toStr

    new_folder =  reformatDateTime()
    path = basic_path + new_folder 
    print(path)
    # create new single directory
    os.mkdir(path) # print(path, "폴더 만들기 성공!")
    # go inside directory
    os.chdir(path)

    try:
        createVideo()
    except FileNotFoundError as e:
        print(f'An error occurred: {e}')    
    print(loop, path, "IN!")
    loop = loop + 1
    sleep = 0
    while(int(time.time() - start_time) < folder_duration):
        print(sleep, "Slept one second")
        time.sleep(1)
        sleep=sleep+1

# # write new csv 
# import csv
# with open('data.csv', 'w', newline='') as file:
#     writer = csv.writer(file)

# write new text file        

# import os, cv2
# import time, datetime
# from pathlib import Path

# # Specify the directory path
# directory = Path("new_folder")

# # Create the directory
# directory.mkdir(parents=True, exist_ok=True)

# def create_hourly_file(base_filename, directory="."):
#     """
#     Creates a new file with a timestamped filename every hour.

#     Args:
#         base_filename (str): The base name for the files.
#         directory (str, optional): The directory to create the files in. Defaults to the current directory.
#     """

#     while True:
#         # Get the current time
#         current_time = datetime.datetime.now()

#         # Create the filename with the hour and minute
#         filename = f"{base_filename}_{current_time.strftime('%Y-%m-%d_%H-%M')}.txt"
#         filepath = os.path.join(directory, filename)

#         # Create the file if it doesn't exist
#         if not os.path.exists(filepath):
#             with open(filepath, "w") as f:
#                 f.write(f"New file created at {current_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
#                 print(f"Created new file: {filepath}")

#         # Wait for the next hour
#         time.sleep(5)  # 3600 seconds = 1 hour
#         if cv2.waitKey() == 27:
#             break

# if __name__ == "__main__":
#     base_filename = "hourly_log"
#     directory = "C:/SBA/openCVDojang"  # Replace with your desired directory
#     create_hourly_file(base_filename, directory)


# 3. 블랙박스 녹화 폴더가 1GB이면
# 가장 오래된 녹화 폴더 삭제


# # 블랙박스 동영상 만들기
# import cv2, sys
# isWEBCAM = False

# if isWEBCAM: 
#     # webcam인 경우 카메라 번호를 입력
#     cap = cv2.VideoCapture(0)
# else:
#     fileName = 'data/vtest.avi'
#     cap = cv2.VideoCapture(fileName)

# # 카메라의 이미지 사이즈
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# frameSize = (width,height)

# print(frameSize)
# # 카메라에서 전달되는 초당 프레임 수
# fps = int(cap.get(cv2.CAP_PROP_FPS))

# # 코덱 설정
# fourcc = cv2.VideoWriter_fourcc(*'XVID')

# # 컬러 동영상 녹화를 위해
# out_color = cv2.VideoWriter('record0.mp4', fourcc, fps, frameSize)
# # grayscale 동영상 녹화를 위해
# out_grayscale = cv2.VideoWriter('record0.mp4', fourcc, fps, frameSize, isColor=False)

# while(True):
    
#     # 한 프레임 영상 읽어오기
#     retval, frame = cap.read()
   
#     # 카메라에서부터 영상이 정상적으로 전달되었는지 확인
#     if not retval:
#         break
#     # 동영상 녹화기에 프레임 전달
#     out_color.write(frame)
#     grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     out_grayscale.write(grayFrame)

#     cv2.imshow('frame', frame)
#     cv2.imshow('gray', grayFrame)
#     delay = int(1000/fps)
    
#     if cv2.waitKey(delay) == 27:
#         break

# cap.release()
# out_color.release()
# out_grayscale.release()
# cv2.destroyAllWindows()

# #1. 60초에 동영상 한 개가 생성되도록 한다.

# import cv2, sys
# import numpy as np

# # Parameters
# duration = 1  # Duration of the video in seconds
# fps = int(cap.get(cv2.CAP_PROP_FPS))      # Frames per second
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # Calculate the total number of frames
# total_frames = int(duration * fps)

# # Create a VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out60_color = cv2.VideoWriter('record0.mp4', fourcc, fps, frameSize)
# out60_grayscale = cv2.VideoWriter('record0.mp4', fourcc, fps, frameSize, isColor=False)

# # Generate and write frames
# for i in range(total_frames):
#     # 한 프레임 영상 읽어오기
#     retval, frame = cap.read()
   
#     # 카메라에서부터 영상이 정상적으로 전달되었는지 확인
#     if not retval:
#         break
#     # 동영상 녹화기에 프레임 전달
#     out_color.write(frame)
#     grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     out_grayscale.write(grayFrame)

#     cv2.imshow('frame', frame)
#     cv2.imshow('gray', grayFrame)
#     delay = int(1000/fps)
    
#     if cv2.waitKey(delay) == 27:
#         break

# cap.release()
# out_color.release()
# out_grayscale.release()
# cv2.destroyAllWindows()
