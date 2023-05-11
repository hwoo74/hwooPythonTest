import traceback
# Exception 발생시 정확한 위치를 추적한다.
# print(traceback.format_exc())

class MyException(Exception):   # 오류 지정, 반드시 Exception 상속필요.
    def __init__(self, code, msg):      # 초기화
        self.code = code
        self.msg = msg
    def __str__(self):                  # 오류를 받아서 출력하려면 구현 필요.
        return "[{0}] {1}".format(self.code, self.msg)

try :
    invarOrg = input('반드시 숫자 입력:')
    invar = int(invarOrg)
    if invar <= 0 :
        raise MyException(invar, 'This number is not positive') # 정의된 오류 던지기
except MyException as err:  # 정의된 오류의 경우 err로 __str__함수값을 받는다.
    print( err )
except Exception as err:                     # 정의되지 않은 오류.
    print('exception occurred.')
    print( err )
    print( type(err) )                      # <class 'ValueError'>
    # Exception 발생시 정확한 위치를 추적한다.
    print( '-'*10)
    print(traceback.format_exc())
    print('-' * 10)
else:
    invarOrg = "Input Number is %d" % invar     # 오류 없으면 실행.
finally:                                        # 항상 실행.
    print(invarOrg)

print("-"*20)
print("done")
