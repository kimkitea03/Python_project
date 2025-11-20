# coffees = [] # empty list

coffees = list() # 함수를 이용한 빈 리스트 생성

coffees.append('아메리카노')
coffees.append('콜드부르')
coffees.append('카푸치노')
coffees.append('바닐라라떼')
coffees.append('디카페인커피')
coffees.append('카페라떼')

count = len(coffees)
print('요소 개수 : %d' % count)

# 1번째 요소를 고구마라떼로 변경
coffees[1] = '고구마라떼'

# 인덱싱
print('앞에서 2번째 요소 : %s' % coffees[2])
print('뒤에서 1번째 요소 : %s' % coffees[-1])

# 슬라이싱
# coffees [start : end : step] start부터 시작하여 end직전까지 step 단계씩 슬라이싱하세요.
print('1번째 요소부터 3번째 요소까지 : %s' % coffees[1:4]) # 1부터 4직전까지라는 뜻
print('3번째 이후의 요소 : %s' % coffees[3:])
print('2번째 이전의 요소 : %s' % coffees[:3])

print('0부터 짝수 요소만 : %s' % coffees[0::2])
print('1부터 홀수 요소만 : %s' % coffees[1::2])
print('전부 출력 : %s' % coffees[::])

print('오름차순 정렬')
coffees.sort()
print(coffees)

print('내림차순 정렬')
coffees.sort(reverse=True)
print(coffees)

