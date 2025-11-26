filename = 'coffee_list.txt'

test = open(file=filename, mode='rt', encoding='utf-8')


while True:
    line = test.readline().strip()
    print(type(line))
    if not line:
        print(line)
        break

    print('['+line+']')

test.close()


test2 = open(file=filename, mode='rt', encoding='utf-8')

data = [item.split() for item in test2.readlines()]
print(type(data))
print(data)

test2.close()

test3 = open(file=filename, mode='rt', encoding='utf-8')
data2 = test3.read()
print(type(data2))
print(data2)
test3.close()