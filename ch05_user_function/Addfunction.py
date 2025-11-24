# 함수의 정의
# 매개 변수 : parameter, argument, 인자, 인수라고 부르기도 합니다.
# 자바와는 달리 매개 변수의 기본 값을 입력할 수 있습니다.
# 오버 로딩 개념이 없습니다.(내부에 연산자 오버로딩은 있음, 함수 오버로딩은 없음)
def add(first, second=15):
    return first + second
# end def

su01 = 14
su02 = 5

# positional argument : index를 이용하여 매개 변수에 할당하는 방식
result = add(su01, su02) # 함수의 호출
print('%d + %d = %d' % (su01, su02, result))

print('%d + %d = %d' % (100, 200, add(100, 200)))

# keyword argument : 매개 변수 키워드를 이용하여 매개 변수에 할당하는 방식
result = add(second=su01, first=su02)
print('%d + %d = %d' % (su01, su02, result))

# 2방식의 혼합 (positional 방식과 keyword 방식이 혼합)
result = add(15, second=20)
print('%d + %d = %d'%(15,20,result))

result = add(10)
print('%d'%result)
