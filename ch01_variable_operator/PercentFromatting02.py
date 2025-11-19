from pyexpat.errors import messages

name = '김철수'
fruit = '사과'
gaesu = 8
su01 = 4
su02 = 9
su03 = -5
a = 2.0
b = 3.0
rate = 0.4567

messages ="%s가 %s를 %d개 먹었습니다."
messages2 = "%d 곱하기 %d는 %d입니다."
messages3 = "%0.6f의 %0.6f 제곱은 %0.6f입니다."
messages4 ="비율 : %0.6f%%"
message5 = "%를 표시할려면 %%를 표시해야합니다."
message6 = "원본 : %d , 절대 값 : %d"

print(messages%(name,fruit,gaesu))
print(messages2%(su01,su02,(su01*su02)))
print(messages3%(a,b,pow(a,b)))
print(message5)
print(messages4%(100*rate))
print(message6%(su03 ,abs(su03)))