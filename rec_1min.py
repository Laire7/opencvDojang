import cv2
import threading
import time

# 1분 타이머 스레드 함수
def timer_thread(stop_event):
    global recording
    time.sleep(60)  # 60초 (1분) 대기
    stop_event.set()  # 이벤트 설정 (녹화 중지)

# 녹화 중지 이벤트 생성
stop_recording = threading.Event()

# 타이머 스레드 생성 및 시작
timer = threading.Thread(target=timer_thread, args=(stop_recording,))
timer.start()

# 웹캠 캡처 객체 생성
cap = cv2.VideoCapture(0)

# 녹화 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 코덱 설정
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))  # 프레임 레이트 설정
print(fps)
out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))  # 출력 파일 설정

# 녹화 시작
recording = True
while recording:
    ret, frame = cap.read()  # 프레임 읽기
    if ret:
        out.write(frame)  # 프레임 저장
        cv2.imshow('Webcam Recording', frame)  # 미리보기 표시

        # 'q' 키를 누르면 즉시 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            recording = False
            break

    # 타이머 이벤트 확인 (1분 경과 여부)
    if stop_recording.is_set():
        recording = False

# 녹화 종료
cap.release()
out.release()
cv2.destroyAllWindows()

# import cv2
# import threading
# import time
# import datetime

# # 웹캠 녹화 스레드
# class WebcamRecorder(threading.Thread):
#     def __init__(self, output_dir):
#         super().__init__()
#         self.output_dir = output_dir
#         self.cap = cv2.VideoCapture(0)  # 웹캠 0번 연결
#         self.running = True

#     def run(self):
#         while self.running:
#             ret, frame = self.cap.read()
#             if not ret:
#                 print("웹캠 연결 실패")
#                 break

#             timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#             filename = f"{self.output_dir}/{timestamp}.avi"

#             # 비디오 코덱 설정 (XVID)
#             fourcc = cv2.VideoWriter_fourcc(*'XVID')
#             out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

#             out.write(frame)  # 현재 프레임 쓰기
#             out.release()

#             time.sleep(1)  # 1초 대기

#         self.cap.release()

# # 1분 타이머 스레드
# class TimerThread(threading.Thread):
#     def __init__(self, recorder):
#         super().__init__()
#         self.recorder = recorder

#     def run(self):
#         while True:
#             time.sleep(60)  # 1분 대기
#             print("1분 경과 - 새로운 비디오 파일 생성")

# # 메인 함수
# if __name__ == "__main__":
#     output_dir = "videos"  # 비디오 저장 경로

#     # 웹캠 녹화 스레드 생성 및 시작
#     recorder = WebcamRecorder(output_dir)
#     recorder.start()

#     # 1분 타이머 스레드 생성 및 시작
#     timer = TimerThread(recorder)
#     timer.start()

#     try:
#         while True:
#             time.sleep(1)  # 1초 대기 (메인 스레드 유지)
#     except KeyboardInterrupt:
#         print("종료")
#         recorder.running = False
#         recorder.join()  # 녹화 스레드 종료 대기
#         timer.join()  # 타이머 스레드 종료 대기