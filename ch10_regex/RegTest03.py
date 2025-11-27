import re
# ########################################################################
# # RegTest03.py
# ########################################################################
print('findall 함수는 정규식과 매치되는 모든 문자열을 list 형식으로 반환해 줍니다.')
order_info = '오늘 커피가격은 아메리카노 3500원, 라테 4200원, 모카 4800원입니다.'


# 날짜처럼 예시를 맞추기 위해 0000/00/00 형태로 출력하는 형식 유지
# 이번에는 가격을 "3500/4200/4800" 형태로 출력


print('\n총 주문 수량 구하기')
order_qty = '아메리카노 2잔, 카페라테 3잔, 바닐라라테 1잔 주세요.'
regEx = '\d+'
pattern = re.compile(regEx)
result = pattern.finditer(order_qty)

total = 0
for match in result:
    total += int(match.group())

print('총 주문 수량 : %d' % total)


print('\nb로 시작하는 커피 메뉴만 추출하여 정렬하기')
menu_list = '브루잉 brew 블랙 black 바닐라 vanilla 바닐라라테 latte 블루 blue'
regEx = 'b[a-z]*'
pattern = re.compile(regEx)
result = pattern.findall(menu_list)
result.sort()
print(result)

print('\nfinditer 함수는 결과물을 반복 가능한 객체 형식으로 반환해 줍니다.')
print('일반적으로 for 구문과 같이 사용됩니다.')
result = pattern.finditer(menu_list)
for fill in result:
    print('\n객체정보 : ', fill)
    print('문자열 정보 : ', fill.group())
    print('색인 위치 tuple : ', fill.span())
    start, end = fill.start(), fill.end()
    print('슬라이싱을 이용한 문자열 추출 : ', menu_list[start:end])

print('\n커피 주문 수량 계산(finditer)')
mycoffee = '에스프레소 1잔, 아메리카노 2잔, 카푸치노 3잔'
regEx = '\d+'
pattern = re.compile(regEx)
result = pattern.finditer(mycoffee)
total = 0
for fill in result:
    total += int(fill.group())


print('음료 총 주문 수량 : %d' % total)



# 실행 결과
#
# findall 함수는 정규식과 매치되는 모든 문자열을 list 형식으로 반환해 줍니다.
# <class 'list'>
# ['3500', '4200', '4800']
# 3500/4200/4800
#
# 총 주문 수량 구하기
# 총 주문 수량 : 6
#
# b로 시작하는 커피 메뉴만 추출하여 정렬하기
# ['black', 'blue', 'brew']
#
# finditer 함수는 결과물을 반복 가능한 객체 형식으로 반환해 줍니다.
# 일반적으로 for 구문과 같이 사용됩니다.
# 객체 정보 : <re.Match object; span=(4, 8), match='brew'>
# 문자열 : brew
# 색인 위치 tuple : (4, 8)
# 슬라이싱을 사용한 문자열 추출 : brew
# 객체 정보 : <re.Match object; span=(12, 17), match='black'>
# 문자열 : black
# 색인 위치 tuple : (12, 17)
# 슬라이싱을 사용한 문자열 추출 : black
# 객체 정보 : <re.Match object; span=(45, 49), match='blue'>
# 문자열 : blue
# 색인 위치 tuple : (45, 49)
# 슬라이싱을 사용한 문자열 추출 : blue
#
# 커피 주문 수량 계산(finditer)
# 음료 총 주문 수량 : 6


