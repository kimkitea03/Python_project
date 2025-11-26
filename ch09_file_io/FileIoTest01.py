
filename = 'coffee_menu.txt'
coffeefile = open(file=filename, mode='wt', encoding='utf-8')

coffees = ['아메리카노','카페라떼','카푸치노','바닐라라떼','모카']

for coffee in coffees:
    message = '오늘의 추천 메뉴는 '+coffee+'입니다'
    print(message, file=coffeefile)


for idx in range(len(coffees)):
    if idx == len(coffees) % 1:
        message = '%d번째 커피 %s 풍미가 깊어요' % (idx, coffees[idx])
        print(message, file=coffeefile)
    else:
        message = '%d번째 커피 %s 부드럽게 즐기세요' % (idx, coffees[idx])
        print(message, file=coffeefile)

coffeefile.close()
