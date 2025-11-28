import json

filename = 'HumanData02 (1).json'

with open(filename, 'rt', encoding='UTF-8') as myfile:
    mystring = myfile.read()
    jsondata = json.loads(mystring)
# end wiht

print(f'원본 json 타입 : {type(jsondata)}')
print(f'요소 갯수 : {len(jsondata)}')
print()
print(jsondata)

for key in jsondata:
    print('-'*30)
    # 커피 기본정보
    name = jsondata[key]['basic']['name']
    origin = jsondata[key]['basic']['origin']
    roast = jsondata[key]['basic']['roast']
    # 커피 레시피
    recipe = jsondata[key]['recipe']

    if 'water' in recipe:
        water_mlike = recipe['water']
        wmname= '물'
    else:
        water_mlike = recipe['milk']
        wmname = '우유'

    espresso_shot = recipe['espresso_shot']

    # 브랜드 정보
    brand = jsondata[key]['store']['brand']
    branch = jsondata[key]['store']['branch']
    last_brewed = jsondata[key]['store']['last_brewed']
    status = jsondata[key]['store']['status']

    print(name, origin, roast, water_mlike, espresso_shot, brand, branch, last_brewed, status)

    message = f'메뉴명 : {name}, 원두 : {origin}, 로스트 정도 : {roast}'
    print(message)

    if 'chocolate' in recipe: # 초콜릿이 있는지 없는지 확인
        chocolate = recipe['chocolate']
        message = f'{wmname}의 용량 : {water_mlike}, 에스프레소 샷 : {espresso_shot}, 초코릿 양 : {chocolate}'
    else :
        message = f'{wmname}의 용량 : {water_mlike}, 에스프레소 샷 : {espresso_shot}'
    print(message)
    message = f'카페 브렌드 : {brand}, 지점 : {branch}, 마지막 제조 : {last_brewed}, 판매 상태 : {status}'
    print(message)
