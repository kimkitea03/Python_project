import json

filename = 'humans.json'
humansfile = open(file=filename, mode='rt', encoding='utf-8')
myhumans = humansfile.read()
print(type(myhumans))
humansfile.close()

jsonData = json.loads(myhumans)
print(type(jsonData))
print(jsonData)

humanList = list()

for human in jsonData:
    name = human['name']
    hobby = human['hobby']
    address = human['address']
    blood = human['blood']
    ssn = human['ssn']

    gender = '남자' if ssn[7] in ['1', '3'] else '여자'

    if ssn[7] in ['3','4'] :
        year = '2000년대생'
    else:
        year = '1900년대생'

    # end if

    humantuple = (name, hobby, address, blood, ssn, gender, year)
    humanList.append(humantuple)
# end for

print(humanList)