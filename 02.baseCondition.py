lst1 = [1, 3, 5, 7]
var1 = 4
str1 = "hooly4"

#if test.
if var1 < lst1[1] :
    print( str(var1) + ' less then ' + str(lst1[1]) )
elif var1 not in lst1 :
    print( str(var1) + ' is in lst array' )
    print( var1 )
    if str(var1) in str1 :          # string 에도 in 적용가능...
        pass                        # 걍 건너뛰기.
    else :
        print('and not in str1')
else :
    print('out of condition')

res = 'okay' if str(var1) in str1 else 'not okay'   # 결과값, 조건, 아닌경우 선언.
print(res)

# loop test.
money = 470
coffee = 31
while money and coffee :
    money -= 100
    if money < 0 :
        print('돈모잘라')
        break               # continue 도 사용가능.
    coffee -= 1
    print('I got a one 커퓌...')

googoodan = [ 2, 3, 4, 5 ]
for goo in googoodan :                  # 일반적 for ( forEach 같은 방식 )
    for goo2 in range(1,10) :           # 일반적 for 범위 ( 1 ~ 9 까지, 마지막은 실행안됨 )
        print( goo * goo2, end="")      # 행바꿈 표기 시정.. 행바꿈 안함.
        if goo2 == 9:
            print("")                   # 행바꿈.
        else:
            print(", ", end="")

# List comprehension 을 사용한 방법.
# 이중 루프에 조건을 추가해서 2중배열로 결과값을 얻음
resarr = [ [ goo * goo2 for goo2 in range(1,10) if goo2 != 9 ] for goo in googoodan if goo > 2 ]
print(resarr)
for res in resarr :
    print(res)


print("--- function test ---")
base = [1,0,2,-3]
print(all( base ))  # all condition is true is true. result is false.   0 is make it to false.
print(any( base ))  # any condition is true is true. result is true.
print(eval('1+1'))  # string to logic .. result is 2 (true).

print("--- is condition ---")
a = [1,2,3]
b = a
c = a[:]
print( 'a is b', a is b, 'address is ', id(a), id(b) )   # is 는 주소값 비교. 바로 할당하면 같은 주소.
print( 'a is C', a is c, 'address is ', id(a), id(c) )   # is 는 주소값 비교, 복제 할당하면 다른 주소.