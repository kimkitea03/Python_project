# Exception02.py

# 품목을 주문하되, 존재하지 않으면 예외 발생 시키기
def studentsCheck(findItem):
    students = ['철수','영희','민수','지영']
    if findItem in students:
        print(f'학생 \'{findItem}\'은(는) 출석했습니다.')

    else: # 예외 발생 시키기
        message = f'\'{findItem}\' 학생의 정보를 찾을 수 없습니다.'
        raise Exception(message)
    # end if
#  end def coffeeCheck

try:
    CheckList = ['철수','훈식']
    for item in CheckList:
        studentsCheck(item)
    # end for

except Exception as e:
    print('예외 발생 : {}'.format(e))
# end try

