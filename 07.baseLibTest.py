import datetime

print( dir(datetime) )  #return all var/function list.
print( dir(datetime.datetime) )     # 하나 더 들어가야 하나 ...

fixdate = datetime.date(2019,12,31)
print(fixdate)
nowdate = datetime.datetime.now().date()
print(nowdate)
print( nowdate - fixdate )
print( type(datetime.datetime.now) )    # <class 'builtin_function_or_method'>  ... 함수인지 체크 가능.
print( type(datetime.MAXYEAR) )         # <class 'int'>                         ... 변수 타입 확인 가능.

import time
print( dir(time) )
time.sleep(1.5)         # sleep 1.5 second.
print( time.time() )    # timestamp.

import random
print( random.random() + random.randint(1,10) )

import os
sysres = os.system("dir/w")
#print( str(sysres).encode( encoding='utf8' ) )       # 한글 깨지구 지랄 ...
#print( str(sysres).encode( encoding='cp949') )       # 한글 깨지구 지랄 ...
#print( str(sysres).encode( encoding='EUC-KR') )       # 한글 깨지구 지랄 ...
print( sysres )                                     # 한글이 ...
# 뭔 짓을 해도 한글이 깨지니 아래 import 를 사용하고, subprocess 를 확인해서 조합해야 한다.


import chardet
import subprocess       # subprocess 를 통한 실행 캡춰.
#subprocess.run("dir/w", shell=True) # 그냥 실행.
#result = subprocess.run("dir/w", capture_output=True, shell=True)  #실행 캡춰.
#print(chardet.detect(result.stdout) )                              # 인코딩 타입을 알아보고, 확실하면 아래문으로 진행.
result = subprocess.run("dir/w", capture_output=True, shell=True, encoding='EUC-KR') #실행 캡춰.
print(result.stdout)


from collections import namedtuple

Book = namedtuple('Book', ['title', 'price'])
mybook3 = Book("hellohello", 27000)
print( mybook3 )
print(mybook3.title)
print(mybook3.price)

#import webbrowser
#webbrowser.open_new('http://python.org')
# 브라우저 에서 웹 사이트 띄워줌 ...

import uuid
print('uuid 1 - ', uuid.uuid1())
print('uuid 4 - ', uuid.uuid4())