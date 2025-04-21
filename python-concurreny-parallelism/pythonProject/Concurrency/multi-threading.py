import threading
import time
import os


def io_bound_work(n, results):
    """I/O를 기다리는 작업"""
    print(f"작업 {n} 시작 - {time.strftime('%H:%M:%S')}")
    print(f"현재 프로세스: {os.getpid()}, 현재 스레드: {threading.get_ident()}")
    time.sleep(n)  # 스레드는 블로킹되지만 다른 스레드는 실행될 수 있음
    results[n - 1] = f"결과 {n}"


def cpu_bound_work(n, results):
    """CPU를 사용하는 계산 작업"""
    print(f"작업 {n} 시작 - {time.strftime('%H:%M:%S')}")
    print(f"현재 프로세스: {os.getpid()}, 현재 스레드: {threading.get_ident()}")
    # CPU 집약적 계산
    result = sum(i * i for i in range(10000000 * n))
    results[n - 1] = f"결과 {n}: {result % 10000}"


def main_io_bound():
    print(f"메인 스레드 - 프로세스 ID: {os.getpid()}, 스레드 ID: {threading.get_ident()}")
    start = time.time()

    # 공유 결과 리스트
    results = [None] * 3

    # 스레드 생성 (I/O 바운드 작업)
    threads = []
    for i in range(1, 4):
        thread = threading.Thread(target=io_bound_work, args=(i, results))
        threads.append(thread)
        thread.start()

    # 모든 스레드가 완료될 때까지 기다림
    for thread in threads:
        thread.join()

    end = time.time()
    print(f"총 실행 시간 (I/O 바운드): {end - start:.2f}초")
    print(f"결과: {results}")


def main_cpu_bound():
    print(f"메인 스레드 - 프로세스 ID: {os.getpid()}, 스레드 ID: {threading.get_ident()}")
    start = time.time()

    # 공유 결과 리스트
    results = [None] * 3

    # 스레드 생성 (CPU 바운드 작업)
    threads = []
    for i in range(1, 4):
        thread = threading.Thread(target=cpu_bound_work, args=(i, results))
        threads.append(thread)
        thread.start()

    # 모든 스레드가 완료될 때까지 기다림
    for thread in threads:
        thread.join()

    end = time.time()
    print(f"총 실행 시간 (CPU 바운드): {end - start:.2f}초")
    print(f"결과: {results}")

if __name__ == '__main__':
    # 핵심 포인트:
    # 1. 각 작업이 다른 스레드 ID를 가짐 (멀티스레드 실행)
    # 2. 모든 작업이 동일한 프로세스 내에서 실행됨
    # 3. I/O 바운드 작업에서는 효율적이지만, CPU 바운드 작업에서는 GIL로 인해 성능 향상이 제한됨
    main_io_bound()
    main_cpu_bound()

