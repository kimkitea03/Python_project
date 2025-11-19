'''
    멀티라인 주석입니다.
    작성자 : 홍길동
    작성 일자 : 2025/11/19
    목적: 처음 작성해 보는 python 프로그래밍
'''
# from collections.abc import async_generator

# 내 이름 출력하기
print('홍')
print()
print("길")
print("동")

# 특수문자 사용
print('이름\t국어\t영어 \t수학')
print('김철수\t50\t60\t70')
print('\n\n')
print('박영희\t30\t40\t50')
print("오늘은 \'날씨\'가 엄청 추워요")

# sep매개변수: 구분자를 의미하는데, 기본 값은 공백, 사용자가 변경할 수 있음
# sep='/' 이런식으로하면 구분자는 /가 된다

name = '김철수'
age = 30
address = '마포'
print('이름 :'+name)
print('나이 :'+str(age))# 형변환 : 변경할 타입 (변수)
print('주소 :'+address)

name = "홍길동"
age = 27
height = 175.23
weight = 55.4
bool = False
print("제 이름은 "+name+"이고, 키는 "+str(height)+"이며, 몸무게는 "+str(weight)+"입니다.")