class NullClass:
    pass    #빈클래스 선언.

"""
# 추상 클래스 선언.
# 상속 클래스에서 함수 구현 안하면 오류남...
import abc      # 추상 클래스 사용을 위한 import
 
class NullClass(metaclass=abc.ABCMeta) :
    @abc.abstractmethod
    def decr(self) :
        pass    # 빈클래스 선언.
"""

class Tclass(NullClass) :       # NullClass 상속 ... !
    __privateVar = 'private variable'
    _protectedVar = 'protected variable'
    publicVar = 'public variable'           # 앞의 밑줄 갯수에 따라 값이 변경됨 ....
    base = 99
    def __init__(self, var):    # constructor
        if type(var) is int:
            self.base = var     # 이게 상단의 클래스 변수 base ( = Tclass.base ) 값을 변경한다고 생각하면 안됨.
                                # self.base 와 Tclass.base 는 서로 다른 값임 ... !!!!
    def rtnVar(self):
        return self.base

    def incr(self):
        self.base += 1;

    def echo(self, inStr):
        print(inStr)

    def chkAll(self):
        print( 'self.base is ' + str(self.base) )       # 이거는 내부에서 변환 사용하는 변수.
        print( 'Tclass.base is ' + str(Tclass.base) )   # 이거는 파생된 모든 클래스가 사용되는 공용값. !!!!!!
                                                        # 걍 클래스 명으로 땡기면 Static 이라 생각하면 된다.

leah = Tclass(10)
leah.incr()
print( leah.rtnVar() )
leah.echo('hi')
Tclass.echo( leah, 'hi')     # 타입으로 선언해서 호출할때는, self 에 해당하는 클래스 변수가 전달되어야 한다.

leah2 = Tclass('hooolla')
leah2.incr()
print( leah2.rtnVar() )

print( 'change variable')
Tclass.base = 1024

print( leah.rtnVar() )
print( leah2.rtnVar() )
leah.chkAll()
leah2.chkAll()

print( "="*20)

#print( leah.__privateVar )     # error
print( leah._protectedVar )     # python에서 protected는 실제 제약되지는 않고 일종의 경고 표시로 사용됨 !!!!!
leah._protectedVar = 3
print( leah._protectedVar )
print( leah.publicVar )
#print( Tclass.__privateVar )   # error ... private 에 접근할 수는 없는데 ..
Tclass.__privateVar = '2133'    # 이렇게 강제로 접근해서 ..
print( Tclass.__privateVar )    # 찍으면 또 돌아간다 .... ;;;; -_- ?????
print( Tclass._protectedVar )
print( Tclass.publicVar )

print( "="*20)
dir(leah2)

"""
python 의 class method 에서 private public protected 는 명확하게 막아주는 방식이 아니다........ 
"""