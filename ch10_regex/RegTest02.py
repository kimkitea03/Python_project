import re


# ########################################################################
# # RegTest02.py
# ########################################################################
#
print('===== 커피 데이터에서 숫자 찾기 =====')
coffee_info = '아메리카노 3500원입니다.'
regEx = '\d+'  # 숫자가 1개 이상
# match와 search 함수 테스트
pattern = re.compile(regEx)
result = pattern.match(coffee_info)
print('math 함수 결과 : %s'%result)

result = pattern.search(coffee_info)
print('search 결과 : %s' %result)

print('\n===== 특정 단어(latte)로 시작하는 커피 이름 찾기 =====')
coffee_list = ['latte123', 'mocha99', 'latte_special']
regEx = '^latte*'   # latte로 시작하는 항목들
pattern = re.compile(regEx)
# match 함수 실행 결과
print('match')
for item in coffee_list:
    if pattern.match(item):
        print('%s : True' % item)
    else:
        print('%s : False' % item)

print('\nsearch')

# search 함수 실행 결과
for item in coffee_list:
    if pattern.search(item):
        print('%s : True' % item)
    else:
        print('%s : False' % item)

print('\n===== match 함수의 반환 결과는 Match 객체입니다. =====')
coffee_name = 'espresso_2500'
regEx = '[a-z_]+'  # 알파벳 소문자 또는 _가 1번 이상
pattern = re.compile(regEx)
result = pattern.match(coffee_name)

start_idx, end_idx = result.start(), result.end()


print(f'슬라이싱 : {coffee_name[start_idx:end_idx]}')
print(f'조건에 맞는 문자열 : {result.group()}')
print(f'문자열 시작 인덱스 : {start_idx}')
print(f'문자열 끝 인덱스 : {end_idx}')
print(f'문자열 색인 tuple 정보 : {result.span()}')


print('\n===== search 함수의 반환 결과 역시 Match 객체입니다. =====')
order_info = '총 주문 금액은 4800원입니다.'
regEx = '\d+'  # 숫자 1번 이상
pattern = re.compile(regEx)
result = pattern.search(order_info)


start_idx, end_idx = result.start(), result.end()

print(f'슬라이싱 : {order_info[start_idx:end_idx]}')
print(f'조건에 맞는 문자열 : {result.group()}')
print(f'문자열 시작 인덱스 : {start_idx}')
print(f'문자열 끝 인덱스 : {end_idx}')
print(f'문자열 색인 tuple 정보 : {result.span()}')




# 실행 결과
# ===== 커피 데이터에서 숫자 찾기 =====
# match 함수는 문자열의 처음부터 체크합니다.
# match 결과 : None
# search 함수는 임의의 위치에서 조건에 맞으면 출력해 줍니다.
# search 결과 : <re.Match object; span=(6, 10), match='3500'>
#
# ===== 특정 단어로 시작하는 커피 이름 찾기 =====
# match 함수 실행 결과
# latte123 : True
# mocha99 : False
# latte_special : True
#
# search 함수 실행 결과
# latte123 : True
# mocha99 : False
# latte_special : True
#
# match 함수와 search 함수는 이 경우 동일한 결과를 보입니다.
#
# ===== match 함수의 반환 결과는 Match 객체입니다. =====
# <class 're.Match'>
# 슬라이싱 : espresso_
# 조건에 맞는 문자열 : espresso_
# 문자열 시작 인덱스 : 0
# 문자열 끝 인덱스 : 9
# 문자열 색인 tuple 정보 : (0, 9)
#
# ===== search 함수의 반환 결과 역시 Match 객체입니다. =====
# <class 're.Match'>
# 슬라이싱 : 4800
# 조건에 맞는 문자열 : 4800
# 문자열 시작 인덱스 : 9
# 문자열 끝 인덱스 : 13
# 문자열 색인 tuple 정보 : (9, 13)


