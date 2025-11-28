from xml.etree.ElementTree import Element, ElementTree,SubElement

# xml 파일에 추가할 사전 정보

humanDict = {'kim':('김철수',30,'남자','마포구 공덕동'),'park':('박영희',20,'여자','동대문구 휘경동') }

#xml 파일의 속성에 추가할 사전 정보
anotherDict = {'kim':('01011112222','hello@naver.com'),'park':('01033334444','world@daum.net') }

xmldata = Element('members')

for key, myTuple in humanDict.items():
    mem = SubElement(xmldata, 'member')
    mem.attrib['id'] = key

    SubElement(mem, 'name').text = str(myTuple[0])
    SubElement(mem, 'age').text = str(myTuple[1])
    SubElement(mem, 'gender').text = str(myTuple[2])
    SubElement(mem, 'address').text = str(myTuple[3])

    anotherInfo = anotherDict[key]
    mem.attrib['phon'] = anotherInfo[0]
    mem.attrib['email'] = anotherInfo[1]

#end for

# xmldata.attrib['birth'] = '19951223'
#
# SubElement(xmldata, 'name').text = '홍길동'
# SubElement(xmldata, 'age').text = '30'
# SubElement(xmldata, 'address').text = '마포구 공덕동'


def indent(elem, level=0):
    mytab = '\t'
    i = '\n' + level * mytab

    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + mytab

        if not elem.tail or not elem.tail.strip():
            elem.tail = i

        for elem in elem:
            indent(elem, level + 1)

        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
# end def

indent(xmldata)

xmlFile = 'XmlExam02.xml'

ElementTree(xmldata).write(xmlFile, encoding='utf-8')
print(xmlFile + '파일생성')