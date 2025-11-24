import random

# 0.0 <= 값 < 1.0
print(random.random())

# random.seed(1234) # 시드 배정하면 항상 동일한 값이 나옴
print(random.random())

print(random.randint(1, 10)) # a부터 b까지 아무거나 뽑아와

coffees = ['아메리카노','카페라떼','아이스커피','디카페인커피','바닐라라떼']
print(random.choice(coffees))

random.shuffle(coffees) # list 셔플 (list 순서를 섞어줌)
print(coffees)

# 로또 번호 생성
lottoNumber = [su for su in range(1,46)] # 1부터 46전까지 수를 list에 등록
random.shuffle(lottoNumber)
print(lottoNumber)

lotto = lottoNumber[0:6]
lotto2 = lottoNumber[6:7]

print('당첨 번호 : ',lotto)
print('2등 번호 : ',lotto2)
print('-'*30)

def extractLottoNo():
    random.shuffle(lottoNumber)
    lotto = sorted(lottoNumber[0:6])
    lotto2 = lottoNumber[6:7]
    return lotto, lotto2
# end def extractLottoNo

# 5게임 출력하기
for idx in range(1, 6):
    print(f'\n{idx} 번째 게임')

    lotto, lotto2 = extractLottoNo()
    print('당첨 번호 : ', lotto)
    print('2등 번호 : ', lotto2)

# 다음 명단을 이용하여, 1조당 2명씩 조 배정을 해보세요.
MEMBER_SU = 2 # 조원 멤버 수

members = ['이민정', '최현미', '강유식', '김정식', '안미주', '심현철', '오지훈', '이한나']

# def jo():
#     random.shuffle(members)
#     tim = members[:MEMBER_SU]
#     return tim
# # end def jo
#
# for idx in range(0, 5):
#     print(f'\n{idx} 조')
#     tim = jo()
#     print('조원 : ',tim)
# # end for

for idx in range(0, len(members),MEMBER_SU):
    print(f'\n{idx} 조')
    print('조원 : ',members[idx:idx+MEMBER_SU])

n=3
sampling = random.sample(members,n)
print(sampling)