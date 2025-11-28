from xml.etree.ElementTree import Element, ElementTree, SubElement

xmldata = Element('human', gender = '남자')


xmldata.attrib['birth'] = '19951223'

SubElement(xmldata, 'name').text = '홍길동'
SubElement(xmldata, 'age').text = '30'
SubElement(xmldata, 'address').text = '마포구 공덕동'


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


xmlFile = 'XmlExam01.xml'

ElementTree(xmldata).write(xmlFile, encoding='utf-8')
print(xmlFile + '파일생성')

