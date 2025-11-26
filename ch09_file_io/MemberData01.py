from enum import member

filename = 'memdata01.txt'
myencoding = 'utf-8'

memsfile = open(file=filename,mode= 'r', encoding=myencoding)
members =[mem.split() for mem in memsfile.readlines()]
print(type(members))
print(members)


memsfile.close()

memfile = open(file=filename,mode= 'r', encoding=myencoding)
department = {}

totallist=[]


print('사전정보')
for line in memfile:
    bean = line.strip().split(",")

    name = bean[0]
    dept = bean[1]
    position = bean[2]
    jum01=float(bean[3])*80/1000
    jum02=float(bean[4])*10/100
    jum03=float(bean[5])*10/100

    department[dept] = department.get(dept, 0) + 1

    total=jum01+jum02+jum03
    average=total/3.0

    avg = float('%10.2f'%average)

    sublist = (name,total,avg)
    totallist.append(sublist)

print(totallist)

print(department)
memfile.close()
