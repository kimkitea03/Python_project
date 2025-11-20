breadString = "바게트,크로와상,스콘,치아바타,나쵸,식빵,스콘,호밀빵,베이글"
breadList = breadString.split(',')

breadTuple = tuple(breadList)
print(breadTuple)

breadcount = breadTuple.count('스콘')
print('스콘 개수 : %d'%breadcount)
breadindex = breadTuple.index('스콘')
print('스콘 첫 번째 인덱스 : %d'%breadindex)
newtuple = breadTuple[:3]+breadTuple[-3:]
print('새로운 튜플 : ',newtuple)

newList = list(newtuple)
# print(type(newList))
newList.sort()
print("오름차순 정렬")
print(newList)