myencoding = 'utf-8'

source = open(file='jumsu.txt', mode='rt', encoding=myencoding) # 읽어올 파일
destination = open(file='result.txt', mode='wt', encoding=myencoding) # 신규 생성할 파일

data = [item.strip() for item in source.readlines()]
print(data)

for bean in data:
    # print(type(bean))
    # human = bean.strip() : bean을 str형식으로 만들어줌
    human = bean.split(',') # bean을 ','으로 쪼갠뒤 list형식으로 만들어줌

    # split(), strip() 차이 공부 split은 list, strip은 str

    # print(type(human))
    name = human[0]
    kor = float(human[1])
    eng= float(human[2])
    math = float(human[3])
    _gender = human[4].upper()

    total = kor + eng + math
    average = total/3

    if _gender == 'M':
        gender = '남자'
    else:
        gender = '여자'
    # end if

    # 표시형식 : '이름/성별/총점/평균'
    sentences = '%s/%s/%.1f/%.2f\n' % (name, gender, total, average)
    print (sentences, file=destination)

# end for

source.close()
destination.close()

print('처리 작업이 완료되었습니다.')
