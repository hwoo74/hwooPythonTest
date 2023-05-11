import time
import threading
import faker            # 임의의 데이터를 얻을 수 있는 외부 라이브러리 ....

Faker = faker.Faker('ko-KR')

def long_task():
    for i in range(3):
        time.sleep(1)
        print("working:%s, %s" % (i, Faker.name() ))

print("-- Start Thread TEST --")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    t.start()   # 바로 실행시키고 ... 나중에 실행 시킬꺼면 밑에 루틴으로 ...
    threads.append(t)

print('thread list is', threads)

#for t in threads:  # 나중에 실행시킬꺼면 주석 풀것 ..
#    t.start()

for t in threads:
    t.join()  # join으로 스레드가 종료될때까지 기다린다.

print("-- End --")

# 파이썬 스레드는 메모리 관리를 위해 하나의 스레드만이 파이썬 객체에 접근할 수 있도록 제한하는데,
# 이것을 GIL(Global Interpreter Lock)이라 한다. 이러한 이유로 스레드는 GIL에 영향을 받지 않는
# I/O가 주로 발생하는 네트워크 통신 또는 파일 읽고 쓰기와 같은 작업에 유리하다.
# 즉, 메모리 연산이 많은 작업에는 쓰레드가 유효하지 않음...