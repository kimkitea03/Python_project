from fileinput import close

print('파일에 기록합니다.')

filename = 'mem.txt'
myfile01 = open(file=filename, mode='wt', encoding='utf-8')
print(type(myfile01))

members = ['홍영식','김민수','박진철','강호숙']

for mem in members:
    message = f'{mem}님 안녕하세요.\n'
    myfile01.write(message)

myfile01.close()

print(f'{filename}파일이 생성됨')

print('기존 파일에 내용을 더 추가합니다.')

# append: 제일 뒷쪽에 집어넣기
myfile02 = open(file=filename, mode='at', encoding='utf-8')

for idx in range(len(members)):
    if idx % 2 -- 0 :
        message = f'{idx}번째 고객 {members[idx]}님 방가워요. \n'
    else:
        memsage = f'{idx}번째 고객 {members[idx]}님 어서 오세요.\n'

    myfile02.write(message)

myfile02.close()


print('반복문을 사용하여 파일 여러개를 생성합니다.')
print('파일 이름 : somefile01.txt~somefile10.txt')




# for idx in range(1,10):
#     filename = 'somefile' + '.txt'
#     myfile = open(file=filename, mode='wt', encodin='utf-8')
#     myfile.write(mem+'고객을 위한 텍스트 파일입니다.\n')
#     myfile.close()
#






for mem in members:
    filename = mem + '.txt'
    myfile = open(file=filename, mode='wt', encoding='utf-8')
    myfile.write(mem + '고객을 위한 텍스트 파일입니다. \n')
    myfile.close()




print('with 구문을 사용하면, 일시적으로 close() 함수가 호출이 됩니다.')
with open(file='test.txt', mode='wt', encoding='utf-8') as testfile:
    testfile.write('가나다\n')
    testfile.write('abc\n')
    testfile.write('123\n')

    print('hello world', file=testfile)
# end with
















