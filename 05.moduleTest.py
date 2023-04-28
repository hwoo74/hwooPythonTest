import sys                      # subdirectory 의 module 을 땡기기 위해선,
sys.path.append("./module")     # sys 로딩하고 모듈 path에 디렉토리를 넣어줘야
import modulePi                 # 그제서야 땡길 수 있다.

print( modulePi.PI )            # 모듈내의 함수 호출
Fac = modulePi.Factoria()       # 모듈내 클래스 선언.
print( Fac.get(-3) )            # 모듈내 클래스 함수 호출.

from modulePi import fibonacci, ROOT1   # 모듈 선언 없이 바로 땡기려면 from ~ import ~ 로... 몽땅 땡기려면 import *

print( fibonacci(6) )
print( ROOT1 )

# 패키지 로딩.
#print( sys.path )               # 경로 확인 ...
"""
['D:\\pythonTest\\test', 'D:\\pythonTest\\test', 
'C:\\Users\\NSTAGE\\AppData\\Local\\Programs\\Python\\Python311\\python311.zip', 
'C:\\Users\\NSTAGE\\AppData\\Local\\Programs\\Python\\Python311\\DLLs', 
'C:\\Users\\NSTAGE\\AppData\\Local\\Programs\\Python\\Python311\\Lib', 
'C:\\Users\\NSTAGE\\AppData\\Local\\Programs\\Python\\Python311', 
'D:\\pythonTest\\test\\venv', 
'D:\\pythonTest\\test\\venv\\Lib\\site-packages', 
'./module']
"""

from bubblesort import bubbleSort
piList = [ 3,1,4,1,5,6,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6 ]
bubbleSort(piList)
print(piList)

print('-- make function from function with partial by partial --')
import functools # for functools.partial
def hello( msg='hello', *args ):
    rtnstr = [ f"{msg} {str}" for str in args]   # 일단 리스트로 만들어서,
    return tuple(rtnstr)                        # 튜를로 변환 리턴.

users = ( 'sidney', 'tomas', 'david' )
print( hello( 'hello', *users ) )

hello2 = functools.partial(hello, 'Hi')
print( hello2( *users ) )


print( '-- functool.reduce using --')
data = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x, y: x + y, data)
print(result)  # 15 출력


help(hello) # 함수설명 ;;;