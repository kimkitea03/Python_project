# 필수 매개변수는 앞쪽으로 오기에 first에 기본값을 입력할 수 없다.
def add(first, second = 5):
    return 2 * first + 3 * second

su01 = 3
su02 = 5
result = add(su01, su02)
print('2 * %d + 3* %d = %d' %(su01, su02, result))

print('2 * %d + 3 * %d = %d' %(4, 7, add(4,7)))

print('%d' % add(10))