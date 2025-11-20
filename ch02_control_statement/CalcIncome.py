salary = int(input('월급 입력 : '))
annual_salary = 0 # 연봉

tax = 0.0 # 세금

# 여기에 코딩
if salary >= 500:
    annual_salary = salary * 12
else:
    annual_salary = salary * 13

if annual_salary < 1000:
    tax = 0 * annual_salary
elif annual_salary < 5000:
    tax = annual_salary * 0.10
elif annual_salary < 7000:
    tax = annual_salary*0.12
elif annual_salary < 10000:
    tax = annual_salary*0.15
else:
    tax = annual_salary*0.20

print('급여 : %d' %salary)
print('연봉 : %.2f' % annual_salary)
print('세금 : %.2f' % tax)