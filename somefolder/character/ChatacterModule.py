def namePrint ():
    name = input("이름 입력 :")
    age = int(input("나이 입력 : "))
    print('이름 : %s, 나이 : %d' % (name,age))
# end def

def sayHello(hello, n):
    for i in range(n):
        print(hello)
        # end for
    #end def