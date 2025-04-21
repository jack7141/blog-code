import asyncio
import time
import os
import threading


async def io_bound_work(n):
    """I/O를 기다리는 비동기 작업"""
    print(f"작업 {n} 시작 - {time.strftime('%H:%M:%S')}")
    print(f"현재 프로세스: {os.getpid()}, 현재 스레드: {threading.get_ident()}")
    await asyncio.sleep(n)  # 비동기 대기 - 이 시간 동안 다른 작업이 실행될 수 있음
    return f"결과 {n}"


async def main():
    print(f"메인 함수 - 프로세스 ID: {os.getpid()}, 스레드 ID: {threading.get_ident()}")
    start = time.time()

    # 모든 작업을 동시에 시작하고 완료될 때까지 기다림
    tasks = [io_bound_work(i) for i in range(1, 4)]
    results = await asyncio.gather(*tasks)

    end = time.time()
    print(f"총 실행 시간: {end - start:.2f}초")
    print(f"결과: {results}")

if __name__ == "__main__":
    # 핵심 포인트:
    # 1. 모든 작업이 동일한 프로세스와 스레드에서 실행됨 (싱글 스레드)
    # 2. 하지만 I/O 대기 중에 다른 작업이 실행되어 총 시간이 크게 단축됨
    # 3. 이는 이벤트 루프가 await 지점에서 작업을 전환하기 때문
    asyncio.run(main())
