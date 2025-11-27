import re

# 회원가입, 파일 찾기 등을 할때 사용함

print('알파벳 3개 + 숫자 2개로 구성된 항목 찾기')
myList01 = ['abc12','abcd12','xy345','pq678','abcd1']
regEx = '[a-zA-Z]{3}[0-9]{2}' # 정규 표현식
pattern = re.compile(regEx)
# print(tye(pattern) <class 're.Pattern'>

result01 = [] # 결과를 저장할 리스트
for item in myList01:
    if pattern.match(item): #조건에 충족하면
        result01.append(item)
# end for
print('결과 01 : %s' %result01)

print('file + 영문자 최소 2개 이상 + .png')
print('주의 : 점은 임의의 한문자(줄바꿈 제외), 역슬래시 점 기호를 의미')
myList02 = ['filea.png','fileab.png','fileabc.png','file.png','file99.png','filexyzXpng']
regEx = '^file[a-zA-Z]{2,}\.png$'
pattern = re.compile(regEx)

result02 = []
for item in myList02:
    if pattern.match(item):
        result02.append(item)
    #end if
#end for
print('결과02 : %s' % result02)

def extract_by_regex(data, regExpr):
    # 정규식 regExpr를 사용하여 data에서 조건에 맞는 항목만 리스트로 반환해 줍니다.
    pattern = re.compile(regExpr)
    result = []

    for bean in data:
        if pattern.match(bean):
            result.append(bean)
    #end for

    return result
# end def

print('b로 시작하고, g로 끝나는데 사이에 e가 2번 이상 반복')
myList01 = ['beg','beeg','beeeg','bg']
regEx='^be{2,}g$'

result03 = extract_by_regex(myList01, regEx)
print('결과 03 : %s' % result03)


print('숫자로 시작하고(0제외), 이후에 알파벳이 1개 이상인 항목 찾기')
myList04 = ['1a','2abc','9xyz','0ab']
regEx='^[1-9][a-zA-Z]+$'

result04 = extract_by_regex(myList04, regEx)
print('결과 04 : %s' % result04)


print('\nhello 또는 hi로 시작하는 항목들 찾기')
myList05 = ['hello123','hi999','hey77','hello']
regEx='^(hello|hi).*$'

result05 = extract_by_regex(myList05, regEx)
print('결과 05 : %s' % result05)
