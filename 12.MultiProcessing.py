import time
import faker            # 임의의 데이터를 얻을 수 있는 외부 라이브러리 ....
import multiprocessing as mp    # 이름이 기니까 짧게 갑시다...

Faker = faker.Faker('ko-KR')
parentProcess = mp.current_process()

#print("-- Start of source --", parentProcess.pid )

def mainProc(msg) :
    print(parentProcess.name, parentProcess.pid, end=" --- ")
    #childproc = mp.current_process()
    print('start ', msg )
    time.sleep(1)
    print( Faker.email() )
    return Faker.email()

#multifunc('singleton')

if __name__ == "__main__":
    # 멀티 프로세싱의 다른 애들은 돌아가지 않게 막아주기 위해서 main 만 돌리는 개념.
    print('... multi processing start', parentProcess.pid )

    subproclist = {}
    processCount = range(5)        # 우리는 2개를 더 돌릴꺼얌..
    processPool = []

    for i in processCount:
        print('multi func run - ', i)
        p = mp.Process( name="myChildProc", target=mainProc, daemon=True, args=(i,) )
            # daemon=True 의 경우, 메인 사망시 같이 사망함.
        p.start()                                       # 하나만 실행할땐 가능하지만 ..
        processPool.append(p)

    # 일단 실행은 다 시켜놓고, 하단에서 join 을 잡아서 처리함.
    for i in processPool:
        i.join()    # 종료대기

    print('... multiprocessing ended')

    print('... multiprocessing.pool start ')
    pool = mp.Pool(processes=4)
    pool.map(mainProc, range(4))
    pool.close()
    pool.join()
    print('... multiprocessing.pool ended ')

    print('... concurrent.futures start')
    import concurrent.futures

    pool = concurrent.futures.ProcessPoolExecutor(max_workers=4)
    processPool = []
    processResult = []
    for i in range(4):
        processPool.append(pool.submit(mainProc, i))

    for p in concurrent.futures.as_completed(processPool):
        processResult.append( p.result() )  # 여기서 프로세스별 결과값을 조합한다 ...

    print( processResult )
    print('... concurrent.futures start')

else:
    print( 'this process is', __name__ )


#print("-- End of Source --", parentProcess.pid )
