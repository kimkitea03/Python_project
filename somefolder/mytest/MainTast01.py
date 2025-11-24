import somefolder.mysansu.Sansumodule

print('# import 구문 사용하기')
su1 = 14
su2 = 5
result = somefolder.mysansu.Sansumodule.add(su1, su2)
print('더하기 01 :', result)

result = somefolder.mysansu.Sansumodule.sub(su1, su2)
print('빼기 01 :', result)

print('# from 패키지경로.모듈이름 import 함수')
from somefolder.mysansu.Sansumodule import add

result = add(su1, su2)
print('더하기 02 :', result)

from somefolder.mysansu.Sansumodule import sub
result = sub(su1, su2)
print('빼기 02 :', result)

print('# from 패키지경로 import 모듈이름')
from somefolder.mysansu import Sansumodule
result = Sansumodule.add(su1, su2)
print('더하기 03 :', result)

result = Sansumodule.sub(su1, su2)
print('빼기 03 :', result)

print('# 별칭 사용하기')
import somefolder.mysansu.Sansumodule as imsi
result = imsi.add(su1, su2)
print('더하기 04 :', result)