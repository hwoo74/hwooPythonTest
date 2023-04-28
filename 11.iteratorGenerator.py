import itertools

li1 = [1,2,4]
li2 = li1[:]    #복사 ... address 가 아닌 데이터 복사로 ..

print( id(li1) )
print( id(li2) )
print( li1 )
print( li2 )

li2 = iter(li2);    # li2 만 iteration 으로 변경.
print( li2 )        # 이젠 데이터가 아닌 주소값이 보인다...

print(len(li1))
#print(len(li2))     # 이건 안돌아감...

for ii in li1 : print( ii )
print( '-'*10 )

for ii in li2: print( ii )
print( '-'*10 )

for ii in li1: print(ii)
print('-' * 10)

for ii in li2: print(ii)    # iteration 으로 지정된 li2 데이터는 한번 위에서 사용되었으므로 이 루프는 돌지 않는다 .. !
print(li2)                  # 주소값이 나옴.
print('-' * 10)

print('='*20)
li1 = iter([ 3,1,9,2 ])
li2 = iter(( 3,1,4,1,5,9,2 ))

while True:
    pick = next(li2, -1)    # 더이상 없으면 두번째 인자 -1 리턴 ....
    print( pick, end="," )
    if pick == -1 :
        print( '-1 found')
        break



# 조합쪽으로 itertool 사용. 쓸 일이 많네 ...
print( '-- itertool for combine --')
ptn1 = "ABCDEFG"
ptn2 = [ 1, 2, 9 ]
print( list(zip(ptn1, ptn2)) )     # 조합... 꼭 list 로 감싸야 함.
print( list(itertools.zip_longest(ptn1,ptn2)) )    # 조합 ... 최대한 뽑아냄 ..
print( list(itertools.zip_longest(ptn1,ptn2, fillvalue='XX')) )    # 조합 ... 최대한 뽑아냄 ..

print( list(itertools.permutations(ptn2,2)) )   # ptn2 의 2개 선택 가능한 조합.    (순서 필요)
print( list(itertools.combinations(ptn2,2)) )   # ptn2 의 2개 선택 가능 조합 갯수. (순서 무시)
print( len(list(itertools.permutations(ptn2,2))) ) # ptn2 의 2개 선택 가능 조합 갯수.



# object sorting !!!
import operator
students = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B'),
]
print( sorted(students, key=operator.itemgetter(1)) )
print( sorted(students, key=operator.itemgetter(2,1)) )      # 리스트가 아닌 duple 의 경우엔 키 이름 넣어주면 됨.
                                    # class 에서 self 로 지정된 값도 처리가능, key=attrgetter('age') 로..

print( '-- itertools groupby -- 조금 복잡하당 ... ')
# group by itertools
import pprint       #예쁜 print ;;
dc = [
    { 'name' : 'superman', 'hobby' : 'flying', 'blood' : 'A' },
    { 'name' : 'greenman', 'hobby' : 'lantern making', 'blood' : 'B'},
    { 'name' : 'rainman', 'hobby' : 'gamble', 'blood' : 'A'}
]
dc = sorted(dc, key=operator.itemgetter('blood') )  # 일단 1차로 정렬을 하고,
print( dc )
groupped = itertools.groupby( dc, key=operator.itemgetter('blood') )    # 2차로.. group by 를 key이름으로 잡아 돌림..
print( groupped )   # 엉뚱한 주소값 나옴 ...
# 3차로.. 바로 사용 못하고, 아래처럼 key, item 매핑을 통하여 한번 변환해서 써야 함...
result = {}
for key, item in groupped:
    result[key] = list(item)  # group_data는 이터레이터이므로 리스트로 변경
pprint.pprint( result )


# generator
print('-- generator test --')
def getMsg() :
    yield 1
    yield 2
    yield 3

msgBox = getMsg()
while True:
    try :
        print(next(msgBox))
    except StopIteration :  # 더이상 값이 없으면 여기로 ..
        break


# list & duple case in Generator ...
def longtime_job(i : int = 0) -> str :      # 함수 지정시, 입력값 지정, 함수 리턴값 선언 ... 하지만 힌트일뿐 틀려도 오류가 나지는 않음.
    print("job start", i)
    return "done"

list_job = [longtime_job() for i in range(5)]   # 미리 다 실행시켜놓고, 하나씩 가져오는 방식.
print(type(list_job))   # class list
print(list_job[0])
#print(next(list_job))  # 오류남..

list_job = (longtime_job() for i in range(5))   # 호출될때마다 하나씩 실행 ...
print(type(list_job))   # class generator
#print(list_job[0])     # 오류남..
print(next(list_job))

print('-- 무한 반복 iternation --')
list = ['zephy', 'cy', 'full']
list_cycle = itertools.cycle(list)
for i in range(5):
    print( next(list_cycle) )