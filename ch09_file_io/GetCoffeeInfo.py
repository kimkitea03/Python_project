import math

filename = 'coffee.txt'
filename01 = 'coffee_result.txt'
myencoding = 'utf-8'

coffees = open(file=filename,mode= 'rt',encoding=myencoding)
coffees_result = open(file=filename01,mode= 'wt',encoding=myencoding)

discounts = {
    '아메리카노' : 0.10,
    '라떼': 0.05,
    '카푸치노': 0.07,
    '바닐라라떼':0.08,
    '모카' : 0.06
}

result = []

for line in coffees:
    bean = line.strip().split(",")

    name = bean[0]
    price = int(bean[1])
    sale = int(bean[2])

    discounted_price = price * (1 - discounts[name])
    acount = discounted_price * sale
    acount = math.ceil(acount)

    result.append([name, price, sale, acount])
    print(name, price, sale, acount)

    # 결과 파일 저장
    coffees_result.write(f'{name},{price},{sale},{acount:.2f}\n')

coffees.close()
coffees_result.close()






