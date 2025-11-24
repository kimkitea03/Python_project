import somefolder.mymath.MathModule

print('# import 구문 사용하기')
su =4
result = somefolder.mymath.MathModule.square_root(su)
print('루트 01 : ',result)

su1=2
su2=3
result = somefolder.mymath.MathModule.jegob(su1,su2)
print('제곱의 합 01 : ',result)

print('# from 패키지 경로. 모듈이름 import 함수')
from somefolder.mymath.MathModule import square_root, jegob
# from somefolder.mymath.MathModule import *

# from somefolder.mymath.MathModule import square_root
su=3
resurt = square_root(su)
print('루트 02: ',resurt)

# from somefolder.mymath.MathModule import jegob
su1=3
su2 =4
result= jegob(su1,su2)
print('제곱의 합 02 : ',result)

print('# from 패키지 경로 import 모듈이름')
from somefolder.mymath import MathModule
su = 5
resurt = MathModule.square_root(su)
print('루트 03: ',resurt)

su1=5
su2=6
resurt = MathModule.jegob(su1,su2)
print('제곱의 합 03 : ',resurt)

print('# 별칭 사용하기')
import somefolder.mymath.MathModule as imsi
su = 9
resurt = imsi.square_root(su)
print('루트 04: ',resurt)

