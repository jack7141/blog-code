import threading
import time
import os


def cpu_bound_work(n):
    """CPU를 사용하는 계산 작업"""
    return sum(i * i for i in range(n))


def io_bound_work(n):
    """I/O를 기다리는 작업"""
    time.sleep(n)  # 네트워크나 디스크 I/O를 시뮬레이션
    return f"결과 {n}"


def main():
    print(f"프로세스 ID: {os.getpid()}, 스레드 ID: {threading.get_ident()}")
    start = time.time()

    # 모든 작업을 순차적으로 처리
    results = []
    for i in range(1, 4):
        print(f"작업 {i} 시작 - {time.strftime('%H:%M:%S')}")
        print(f"현재 스레드: {threading.get_ident()}")
        result = io_bound_work(i)
        results.append(result)

    end = time.time()
    print(f"총 실행 시간: {end - start:.2f}초")
    print(f"결과: {results}")

if __name__ == "__main__":
    main()