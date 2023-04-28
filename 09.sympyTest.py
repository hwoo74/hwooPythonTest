import sympy
import fractions    # 유리수 게산용 ..
import math

print( 'math.gcd 최대공약수 :', math.gcd(20,30,50) )
print( 'math.lcm 최소공배수 :', math.lcm(2,3,5))
print( 'float 비교 오류 0.1 * 3 == 0.3', 0.1*3 == 0.3)      # 소숫점 연산은 오류가 잘 난다 ...
print( 'float 오류 수정 math.isclose(0.1*3, 0.3)', math.isclose(0.1*3,0.3) )

print( fractions.Fraction('1/4') )
res = fractions.Fraction('1/4') * fractions.Fraction('1/3')
print( r"분자 : %d, 분모 : %d, 결과값 : %s, 결과값(소수) : %0.50f" % ( res.numerator, res.denominator, res, float(res) ))
print( "소숫점이 뒤로가면 값이 틀어진다 .... 원래 계속33333... 이 나와야 하는데...")
print( "%0.60f" % float(fractions.Fraction('1/3')) )    # 틀어짐 ;;;

# 미지수 연산 1차 방정식.. 결과값은 list
x = sympy.symbols('x')
#f1 = sympy.Lt(x+10, 20)    # res = (-oo < x) & (x < 10)        ... 공식으로 나오니 멋지다 ...
f1 = sympy.Eq(x+10, 20)     # res = [10]            ... list 로 준다.
res = sympy.solve(f1)
print(res)

# 미지수 연산 2차 방정식.. 결과값은 딕셔너리.
x, y = sympy.symbols('x y')     # 미지수 2개 선언.
f1 = sympy.Eq( x+y, 15 )
f2 = sympy.Eq( x*y, 56 )
res = sympy.solve([f1,f2])  # res = [{x: 7, y: 8}, {x: 8, y: 7}]
print(res)

res = sympy.solve([f1])
print(res)                  # res = {x: 15 - y}         ... 멋진데 ???


import statistics   # 평균, 중간값 연산용.
lala = [ 13, 13,44,23, 83, 92,48,77 ]
print( '평균값', statistics.mean(lala) )
print( '중간값', statistics.median(lala) )    # 짝수일때는 중간값 2개를 구한다음에 평균으로 줌.
