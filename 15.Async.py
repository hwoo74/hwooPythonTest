import asyncio
import time


async def sleep():
    await asyncio.sleep(1)


async def sumsum(name, numbers):
    start = time.time()
    total = 0
    for number in numbers:
        await sleep()
        total += number
        print(f'작업중={name}, number={number}, total={total}')
    end = time.time()
    print(f'작업명={name}, 걸린시간={end-start}')
    return total


async def main():
    start = time.time()

    task1 = asyncio.create_task(sumsum("A", [1, 2]))
    task2 = asyncio.create_task(sumsum("B", [1, 2, 3]))

    await task1
    await task2

    result1 = task1.result()
    result2 = task2.result()

    end = time.time()
    print(f'총합={result1+result2}, 총시간={end-start}')


# 테스트 프로그램... 2
async def find_users_async(n):
    for i in range(1, n + 1):
        print(f'{n}명 중 {i}번 째 사용자 조회 중 ...')
        await asyncio.sleep(1)
    print(f'> 총 {n} 명 사용자 비동기 조회 완료!')
    return n

async def process_async():
    start = time.time()
    tasklist = [
        asyncio.create_task( find_users_async(4) ),
        asyncio.create_task( find_users_async(3) ),
        asyncio.create_task( find_users_async(2) ),
        asyncio.create_task( find_users_async(1) )
    ]

    done, pending = await asyncio.wait( tasklist, timeout=2.5 )
    end = time.time()
    print(f'>>> 비동기 처리 총 소요 시간: {end - start}')

    print( '종료 프로세스 숫자 - ', len(done) )
    print( '남은 프로세스 숫자 - ', len(pending) )

    res = [res.result() for res in done]
    print( '종료 프로세스의 결과값 - ', res, ' 결과값의 합은 ', sum(res) )

    print( '--- pending 된 프로세스 다시 돌리기 ---' )

    start = time.time()
    done, pending = await asyncio.wait( pending )
    end = time.time()
    print(f'>>> 두번째 비동기 처리 총 소요 시간: {end - start}')

    print('종료 프로세스 숫자 - ', len(done))
    print('남은 프로세스 숫자 - ', len(pending))

    res = [res.result() for res in done]
    print('종료 프로세스의 결과값 - ', res, ' 결과값의 합은 ', sum(res))

# test 3
async def coro1():
    await asyncio.sleep(1)
    return 'coro1'

async def coro2():
    await asyncio.sleep(2)
    return 'coro2'

async def main3():
    done, pending = await asyncio.wait([coro1(), coro2()], timeout=1.5)
    for task in done:
        print(task.result())


if __name__ == "__main__":
    print('-- test program 1 --')
    asyncio.run(main())

    print( '-- test program 2 --')
    asyncio.run(process_async())    # 비동기 함수 에서 async를 호출할때는 asyncio.run() 을 실행.. python 3.7 부터 가능..

    #print( '--- test program 3 --')
    #asyncio.run(main3())   # 이건 오류가 난다...
    """
    Passing coroutines is forbidden, use tasks explicitly.” 오류는 asyncio.wait() 함수에 코루틴을 직접 전달하면 발생합니다. 
    이 함수는 asyncio.Task 객체의 리스트를 받아서 모든 Task가 완료될 때까지 기다리는 코루틴입니다
    따라서 asyncio.Task 객체를 생성하고 이를 asyncio.wait() 함수에 전달해야 합니다.
    """