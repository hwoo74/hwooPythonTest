def add(x,y):
    return x+y
def boolchk( param ):
    if param :
        return True
    else :
        return False

"""
a = 'hello sidney'
print(a)
print(id(a))    # 주소값 리턴 ... pointer ? 
b = 3
c = 3.14E5
print(b + c)
d = "31"
#print( "hello %d" % d )     # 동작안함 형태 안맞음.
print("hello %s, %d, %s" %(d,int(d),type(d)))     # 동작. 형태 맞춰야 한다. float 는 float() 함수로 ..
print("hihi {0}, {1}, [{title:=^20}]".format(c, d, title=a))     # 문자열 중앙정렬 빈칸 =로 채우기 포함 ...
print(f"Hi {a}")
print("="*20)
print(a.split())
"""

"""
# list test.
l1 = [ 1, 3, 'aa', [ 21, 'bobobo'], ['babe','one','more'] ]
print(add(l1[0],l1[3][0]))
print(l1[2:4]+[13,14,15])
print(str(l1[0])+l1[2].upper()) # 형태가 다르면 형태 통일해서.
print(str(l1[0]).join(l1[3][1]))
#print('X'.lower().join(l1[4].upper()))     #오류, li[4]가 list라서 upper 안먹힘.
print( l1[4][0].upper() )
print(l1[3:4])  # 4번째는 포함 안됨...
del(l1[3:4])    # 3번째만 자르는 게 됨...
print(l1)
"""

# tuple test    .. tuple 은 값 변경 불가.
print("--- tuple test ---");
t1 = 1,2,3,4
t2 = (1, 2, ('a',23))
print( t1 + t2 )
t3, t4, t5, t6 = t1
print( t6 )

def read4( s1, s2, s3, s4 ) :
    print( s1, s2, s3, s4 )

#read4( t1 )    # 오류발생
read4( *t1 )    # 순서대로 대입시킴. 함수 돌아감. 단 길이가 안맞으면 오류남 (입력값 4면 tuple 길이도 4로 .. )


# dictionary
import pprint

print( '-- dictionary test --')
gundam = {
    0 : { 'num' : 1, 'code' : 'rx-78', 'name' : 'gundam' },
    1 : { 'num' : 2, 'code' : 'msz-199', 'name' : 'z-gundam'},
    2 : { 'num' : 37, 'code' : 'mx-104A', 'name' : 'Freedom'}
}
print(gundam)
pprint.pprint( gundam )        # 예쁘게 프린트 !!! pprint !
print(gundam[0].keys())
print(gundam.values())
print(gundam[1].get('code'))
print(gundam[1].get('weapon'))      # if not exist return None
print(gundam[1].get('weapon', 'sword'))      # if not exist get default value 'sword',
print('code' in gundam)     # false
print('code' in gundam[2])  # true

newGundam = dict( num=123, code='cheap-100', name='made in china gundam' )
print( newGundam )

gname = [ 'turnA', 'turnX']
gweapon = [ 'butterfly', 'sword' ]
print( dict(zip(gname,gweapon)) )
print({ k:v+' plus' for k,v in zip(gname,gweapon) })


"""
# set - 집합자료형.
s1 = set([1,2,3,'h'])
print(s1)
s2 = set("hello")
print(s2)       # {'e', 'H', 'l', 'o'}  ... 순서가 없고, 중복을 허용하지 않음. 중복방지의 효과가 있음.
print(s1 & s2)  # 교집합 = s1.intersection(s2)
print(s1 | s2)  # 합집합 = s1.union(s2)
print(s1 - s2)  # 차집합 - s1.difference(s2)
print('-'*15)
# print(s1.add('moo'))    # add 하나. 같이 실행하는건 안먹히고 ....
s1.add('moo')             # 개별로 돌려야 함...
s1.update(['ba','ha','ma','ma','ma'])
s1.remove(2)
print(s1)

# boolean .
# list, dictionary, set 모두 값이 없으면 boolean 타입에서는 false, 문자열이 "" 일때도 false, 숫자는 0 일때 false.
print( boolchk("") )   # false
print( boolchk([]) )   # false
"""

# list 복사 .. 변수선언.
print("--- list 복사 테스트 ---")
la = [1,2,3]
lb = la
lc = la[:]
la[1] = 9
print(lb)   # 같은 주소를 가지고 있으므로 같이 바뀜.        id(la) == id(lb) 임..
print(lc)   # 데이터 복사를 통한 부분이라 별개의 주소를 가지고 있음.
lza, lzb = 'lala', 'land'
print( lza + lzb )
lzb, lza = lza, lzb     # 변수 교차 대입이 가능함 ...
print( lza + lzb )


print( '-- deque --')
# deque 테스트.
import collections
a = [ 1,2,3,4,5 ]
q = collections.deque(a)
print(q)
q.append(6)
q.appendleft(0)
q.rotate(2)
q.rotate(-3)
print(q)
print( q.pop() )
print( q.popleft() )
print(q)

print( '--- use ENUM ---')
import enum

class Week(enum.IntEnum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

print( Week.MONDAY );

print("--- Str Test ---")
import textwrap
import re   # reqular express...

msg = "Life is 1234567890 too short, you need python"

print( textwrap.shorten(msg, width=15) )

# placehodler 포함해서 총 10자로 자름 ... width 11 일때 ;;
print( textwrap.shorten(msg, width=15, placeholder='...') )

print( textwrap.wrap(msg,10))
print( textwrap.fill(msg,10))

# 정규식 패턴 정하고 ..패턴에 맞는 문자열 변환 ...
ptrn = re.compile("\d{1}")
print( ptrn.sub("#",msg) )