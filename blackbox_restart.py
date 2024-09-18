import multiprocessing
import cv2 

def createBlackbox(running, queue):
    print("running createBlackBox")
    running = False
    queue.put(running)

def checkStorageFunc(running, queue):
    print("running check storage function")
    running = False
    queue.put(running)

###메인 프로그램 실행
if __name__ == "__main__":
    running = True #프로그램 종료 변수 일단 True로 할당하기
    
    # 멀티프로세싱 큐 생성
    queue = multiprocessing.Queue()
    # 첫 번째 프로세스 생성 및 시작
    p1 = multiprocessing.Process(target=createBlackbox, args=(running, queue))
    p1.start()

    # 두 번째 프로세스 생성 및 시작
    p2 = multiprocessing.Process(target=checkStorageFunc, args=(running, queue))
    p2.start()
    
    p1.join()
    p2.join()
    running = queue.get() and queue.get()
    print(f'running: {running}')
    print(f'블랙박스 프로그램이 종료되었습니다. 프로그램을 이용해 주셔서 감사합니다.')