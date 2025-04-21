import multiprocessing
import time
import os
import threading


def cpu_bound_work(n):
    """CPU를 사용하는 계산 작업"""
    print(f"작업 {n} 시작 - {time.strftime('%H:%M:%S')}")
    print(f"현재 프로세스: {os.getpid()}, 현재 스레드: {threading.get_ident()}")
    # CPU 집약적 계산
    result = sum(i * i for i in range(10000000 * n))
    return f"결과 {n}: {result % 10000}"


def main():
    print(f"메인 프로세스 - 프로세스 ID: {os.getpid()}, 스레드 ID: {threading.get_ident()}")
    start = time.time()

    # 프로세스 풀 생성 (CPU 코어 수만큼의 프로세스)
    with multiprocessing.Pool() as pool:
        # 작업 제출
        results = pool.map(cpu_bound_work, range(1, 4))

    end = time.time()
    print(f"총 실행 시간: {end - start:.2f}초")
    print(f"결과: {results}")


if __name__ == "__main__":
    # 핵심 포인트:
    # 1. 각 작업이 다른 프로세스 ID를 가짐 (별도의 Python 인터프리터)
    # 2. 각 프로세스 내에서는 기본 스레드 ID를 가짐
    # 3. CPU 바운드 작업에서 큰 성능 향상을 보임 (실제로 병렬 처리가 일어남)
    # 4. 프로세스 생성과 데이터 전송 오버헤드로 인해 약간의 추가 시간이 소요됨
    main()
