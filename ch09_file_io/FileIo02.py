filename = 'test.txt'
myencoding = 'utf-8'

print('readline() 함수는 1줄을 읽어 옵니다.')
myfile01 = open(file=filename, mode='rt', encoding=myencoding)

while True:
    oneline = myfile01.readline().strip()
    # print(type(oneline))
    # .strip() : 스트링에 좌우 공백 제거

    if not oneline:
        print(oneline)
        break
    # end if
    print('['+oneline+']')
# end while

myfile01.close()

print('readlines() 함수는 모든 줄을 읽어서 list로 반환해 줍니다.')
myfile02 = open(file=filename, mode='rt', encoding=myencoding)
sentence = [text.strip() for text in myfile02.readlines()]
# print(type(sentence))
print(sentence)

myfile02.close()



print('read() 함수는 파일 내용 전체를 문자열로 반환해 줍니다.')
myfile03 = open(file=filename, mode='rt', encoding=myencoding)
sentence = myfile03.read()

print(type(sentence))
print(sentence)

myfile03.close()









