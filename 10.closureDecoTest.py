# class 형 closer, 직접 호출시 __call__ 이 호출됨.
class Mul:
    def __init__(self, m):
        self.m = m

    def __call__(self, n):
        return self.m * n

mul3 = Mul(3)
print( mul3(3) )

# 함수형 closer
def mul(m):
    def wrapper(n):
        return m * n
    return wrapper

mul4 = mul(4)
print( mul4(5) )


import sys      # 함수 이름 가져오려고 ... import.

# 일반적 클로저 .... 함수를 인자로 받아 함수를 실행.
def closerPrint( func, *name ):
    print('This is closer func - ' + sys._getframe(0).f_code.co_name )
    func( *name )

def hihi( name = 'sidney') :
    print( "hello %s" % name )

# 데코레이터 ... 함수를 인자로 받아 함수를 실행.
def closerPrint2( func ):
    def rtnfunc(*name) :
        print( '-'*3 + 'inside' + '-'*3)
        #print( func )
        #print( name )
        print('This is closer func - ' + sys._getframe(0).f_code.co_name)  # 지금 함수 이름.
        print('This is closer func - ' + sys._getframe(1).f_code.co_name)  # 한단계 위 함수 이름.
        #print('This is closer func - ' + sys._getframe(2).f_code.co_name)  # 한단계 위 함수 이름.
        func( *name )
    return rtnfunc

@closerPrint2
def hihi2( name = 'balbatos') :
    print( "nice %s" % name )

closerPrint(hihi, 'james')
closerPrint(hihi)

hihi2('zodiac')
hihi2()

print( '-- hasattr, getattr -- ')
class Bao:
    def __init__(self, x):
        self.xbox = x
    def showBox(self):
        return self.xbox

baba = Bao('hi')
print( hasattr(baba, 'xbox'))
print( hasattr(baba, 'showbox'))    # false 대소문자 가림.
print( hasattr(baba, 'showBox'))
showboxfunc = getattr(baba,'showBox');
print( showboxfunc() )

print( '--closer variable--')
def functest() :
    mas = 99
    def func() :
        nonlocal mas    # only python 3 !!
        mas += 1
        return mas
    return func

zz1 = functest()
zz2 = functest()
print( 'zz1', zz1() )
print( 'zz1', zz1() )
print( 'zz2', zz2() )
print( 'zz1', zz1() )

"""
#example 
def decoratorFunctionWithArguments(arg1, arg2, arg3):
    def wrap(f):
        print("Inside wrap()")
        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", arg1, arg2, arg3)
            f(*args)
            print("After f(*args)")
        return wrapped_f
    return wrap

@decoratorFunctionWithArguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print ('sayHello arguments:', a1, a2, a3, a4)

print ("After decoration")

print ("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print ("after first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print ("after second sayHello() call")
"""