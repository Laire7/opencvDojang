import os

# 시작 디렉토리 설정
start_dir = "C:/Users/SBA/opencvDojang/ex1" 

# os.walk 함수 사용
for root, dirs, files in os.walk(start_dir):
    print("현재 디렉토리:", root)
    print("서브 디렉토리:", dirs)
    print("파일:", files)
    print("-" * 20)  # 구분선 출력