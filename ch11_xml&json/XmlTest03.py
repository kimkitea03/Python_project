from xml.etree.ElementTree import parse

tree = parse(source='Car_info.xml')

myroot = tree.getroot()
print(type(myroot))

mycars = myroot.findall('car')
print(type(mycars))
print(f'차 종류 : {len(mycars)}')

for mycar in mycars: # family : 1 가족을 의미
    print('차종 정보')

    brand = mycar[0].text
    brandName = mycar[0].attrib['name']
    name = mycar[1].text
    year = mycar[2].text
    coler = mycar[3].text

    print('브랜드 : %d' % brand)
    print('브랜드명 : %d' % brandName)
    print('이름 : %d' % name)
    print('연도 : %d' % year)
    print('색상 : %d' % coler)
