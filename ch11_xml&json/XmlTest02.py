from xml.etree.ElementTree import Element, ElementTree, SubElement

mydict = {'hong': ('홍길동', 60, 80, 70), 'park': ('박영희', 50, 70, 95)}

xmldata = Element('students')

jum = {'hong':(),'park':()}

for key, myTuple in mydict.items():
    mem = SubElement(xmldata, 'student')
    mem.attrib['id'] = key

    SubElement(mem, 'name').text = str(myTuple[0])
    SubElement(mem, 'kor').text = str(myTuple[1])
    SubElement(mem, 'eng').text = str(myTuple[2])
    SubElement(mem, 'math').text = str(myTuple[3])

    total = myTuple[1]+myTuple[2]+myTuple[3]
    average = total/3

    mem.attrib['총점'] = str(total)
    mem.attrib['평균'] = '%.3f' % average

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

xmlFile = 'XmText02.xml'

ElementTree(xmldata).write(xmlFile, encoding='utf-8')
print(xmlFile + '파일생성')
