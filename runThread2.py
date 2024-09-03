import threading
import time

# 스레드 함수 정의
def sum_numbers(start, end, result):
    global sum_of_numbers
    local_sum=0
    for i in range(start, end + 1):
        local_sum += i
    with lock:
        sum_of_numbers += local_sum

if __name__ == '__main__':
    # 시작 시간 측정
    start_time = time.time()

    # 결과 저장을 위한 리스트
    result = []

    # 스레드 생성 및 시작
    thread1 = threading.Thread(target=sum_numbers, args=(1, 50000000, result))
    thread2 = threading.Thread(target=sum_numbers, args=(50000001, 100000000, result))
    thread1.start()
    thread2.start()

    # 스레드가 종료될 때까지 대기
    thread1.join()
    thread2.join()

    # 결과 합산
    total_sum = sum(result)

    # 종료 시간 측정
    end_time = time.time()

    # 결과 출력
    print("1부터 100000000까지의 합:", total_sum)
    print("실행 시간:", end_time - start_time, "초")