# ExcepTest01.py

try :
    su1 = 10
    su2 = 20

    result = su1 + su2
    print(result)

    mydict = {'hong': 10, 'kim': 20}
    findKey = 'a'
    print(mydict[findKey])

except IndexError as err:
    print('index값에 초과 에러가 발생하였습니다.',err)

except TypeError as err:
    print('타입에 관한 에러가 발생했습니다. %s'%err)

except KeyError as err:
    print('키 입력에 관하여 에러',err)

except Exception as e:
    print('오류가 발생했습니다. %s'%e)

else :
    print('문제 없이 작동합니다.')

finally:
    print('예외처리 공부')
