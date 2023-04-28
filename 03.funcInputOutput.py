basemulti =2
def multifunc( multiple, *args ):
    global basemulti    #함수 내부에서 global 접근 가능.
    if multiple <= 0 :
        multiple = basemulti
    #print(args)
    return [ multiple * var for var in args if var > 0 ]

# 위 함수를 lambda로 multivalue 리턴으로 변경.
multi2 = lambda multiple, *args : ( multiple, [ multiple * var for var in args if var > 0 ])

# 숫자인지 체크 함수 (이게 이렇게도 어렵나 ...)
def checkNum ( var ) :
    if len(var) > 0 and var[0] == '-' :
        var = var[1:]
    if '.' in var :
        var.replace('.','')
    return var.isdigit();


### input 그리고 함수 테스트.
lst1 = [ -1, 0, 1, 2, 3 ]
#print( multifunc(3,lst1) )         # 안된다 ...   함수내 vars 값이 ([ -1, 0, 1, 2,3 ]) 이 됨... tuple로 자동변환 되므로 ...
one, two, three, four, five = lst1  # 사용하고 싶다면 분해해서 대입할것.
print( multifunc(-3, one, two, three, four, five) )  # 이렇게 해야 돌아감.. 즉, 변수의 나열이지 list 나 tuple을 받을 순 없음.

# 키보드 입력을 받아서 lambda로 돌리자
inNum = input("숫자 입력 요망 :")     # 무조건 str로 받음.
import getpass
# 파이참 에디터에서 getpass 얘가 제대로 안돌아감... 콘솔에서는 잘 돌아가기에 ...
# 파이참에서는 테스트 안하는 걸 추천 ....
#inNum = getpass.getpass('숫자 입력 요망 (화면엔 안보임) :')    # 입력값이 *표 로 보임... 비번모드로 입력받기.

inNum = int(inNum) if checkNum(inNum) else inNum

if type(inNum) is int :     # int 인지 체크.
    pass
elif type(inNum) is str :
    print('str','type','is','not' + ' allowed')
    exit(10)
else:
    print(type(inNum), "is Wrong Type")
    exit(11)

multivalue, resarr = multi2( inNum, one, two, three, four )
print( 'multiple value is ' + str(multivalue), end=" list value is " )
print( resarr )

res = [ 3 * var for var in lst1 if var > 0 ]
print(res)



print( '-- args test --')
# 명령인자 args 확인.
# python .\실행파일명.py holla hello sidney
# 이후 파일명 뒤의 파라메터들 저장 ....
import sys
args = sys.argv[0:]     # 파일명 argv[0], 이후 입력값들이 1 부터 시작 ...
params = sys.argv[1:]     # 파일명 argv[0], 이후 입력값들이 1 부터 시작 ...
print(args)
print(params)

# argparse 를 이용한 방식
print( '-- argparse test --')
# python .\실행파일명.py -d200 -f
# 위처럼 아래 정의된 파라메터를 받을 수 있음 ...
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--decimal", dest="decimal", action="store")          # 값을 추가로 받음
parser.add_argument("-f", "--fast", "-fa", dest="fast", action="store_true")           # 걍 flag값으로 처리 ...
args = parser.parse_args()

print(args)
print(args.decimal)
print(args.fast)