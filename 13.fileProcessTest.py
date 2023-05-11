# 파일관리
print('--write test--')
f = open(r"./log.txt", "w")         # 같은 방식으로 r - read, a - append.
for i in range(1,4):
    f.write( "%d is added\n" % i )
f.close()

print('--read test--')
with open(r"./log.txt", "r") as f:
    while True:     # 없을때까지 루프로 읽기.
        buf = f.readline()
        if not buf:
            break
        print(buf.strip())      # 입력값에 \n 가 있으므로 print 를 쓰면 두번 \n 이 출력되므로 입력값에서 제거.
        print(buf, end="")      # 아니면 이렇게 가든지 ..
        print(f.tell())         # 현재 파일 포인터 위치.

    print( '-'*5 )
    f.seek(0)                   # 파일 포인터 다시 맨 앞으로 !! (다시 읽기 위해)
    bufs = f.readlines()        # 몽땅 다 읽어서
    print(bufs)
    for buf in bufs :           # 출력 루프
        print( buf, end="" )

    print('-' *5)
    f.seek(0)  # 파일 포인터 다시 맨 앞으로 !! (다시 읽기 위해)
    for buf in f:       # 위에서 readLines() 를 생략하여 루프 처리 가능한 구조.
        print(buf, end="")

    print('-' *5)
    f.seek(0)  # 파일 포인터 다시 맨 앞으로 !! (다시 읽기 위해)
    print( f.read() )   # 몽땅 읽어서 출력 ...

print( '-- write log with loggin module -- ')
import logging  # 로그 남기기.
#logging.basicConfig(filename="./log.txt", level=logging.INFO)      # 쉼게 로그 설정하기
import logging.config   # 상세하게 설정하기 ...
logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',    # DEBUG < INFO < WARNING < ERROR < CRITICAL
            'class': 'logging.FileHandler',
            'filename': './log.txt',
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})

def writelog( code = 0, message = ""):
    logging.info(f"code: {code}, msg :  {message}")         # 설정 레벨이 info면 상위인 INFO 는 로그에 저장됨.
    #logging.debug(f"code: {code}, msg :  {message}")       # 야는 지정레벨이 INFO 라서 낮은 DEBUG는 안찍힘...

writelog(message='hahaha logloglog')

print( '--tempfile test--')
import tempfile
with tempfile.TemporaryFile("w+") as tf:
    tf.write('mamama\n')
    tf.write('moomoomoo\n')

    tf.seek(0)        # 포인터 맨 앞으로 ...
    print(tf.read())  # 몽땅 읽어서 출력 ...

print( '--data save to file--')
import pickle
import faker
import pprint

Faker = faker.Faker('ko-KR')

orgData = [ { 'name' : Faker.name(), 'address' : Faker.address() } for i in range(5) ]
print( '- pickle 로 처리 -')
with open('./data.p', 'wb') as pkfile:
    pickle.dump(orgData, pkfile)
with open('./data.p', 'rb') as pkfile:
    readData = pickle.load(pkfile)
pprint.pprint( readData )

import json
print( '- json으로 처리 -')
with open('./data.json', 'wt') as jsonfile:
    json.dump(orgData, jsonfile)
with open('./data.json', 'rt') as jsonfile:
    readData = json.load(jsonfile)
pprint.pprint( readData )