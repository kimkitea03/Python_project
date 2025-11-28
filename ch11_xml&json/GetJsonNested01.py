import json

filename = 'HumanData01.json'

with open(filename, 'rt', encoding='UTF-8') as myfile:
    mystring = myfile.read()
    jsondata = json.loads(mystring)
# end wiht

print(f'원본 json 타입 : {type(jsondata)}')
print(f'요소 갯수 : {len(jsondata)}')
print()
print(jsondata)

for key in jsondata:
    # 기본정보
    name = jsondata[key]['name']
    age = jsondata[key]['age']
    # 집주소 정보
    street = jsondata[key]['location']['address']['street']
    city = jsondata[key]['location']['address']['city']
    gu = jsondata[key]['location']['address']['gu']
    # 연락처 정보
    contact = jsondata[key]['contact'] # 결과는 사전
    mobile = contact['mobile']
    email = contact['email']
    # 직업 정보
    job_title = jsondata[key]['job']['title']
    company_name = jsondata[key]['job']['company']['name']
    company_location = jsondata[key]['job']['company']['location']
    # skill 정보
    skills = jsondata[key]['skills']
    myskil = '%'.join(skills)

    print(f'{name},{age},{street},{city},{gu},{mobile},{email},{job_title},{company_name},{company_location},{myskil}')
