# ExceptionTest03.py

# MinJumsuException : 과락(과목이 40미만), FailedException : 평균 60미만

class MinJumsuException(Exception):
    def __init__(self, name, score):
        print()
        message = f"{name}님 과락입니다. ({score}점)\n조금만 더 공부하세요."
        super().__init__(message)


# end class MinJumsuException

class FailedException(Exception):
    def __init__(self, name, average):
        # 평균 기준으로 합격/불합격 메시지를 자동으로 생성
        if average >= 60:
            message = f"{name}님 합격입니다!\n평균: {average}점\n시험 잘 보셨습니다!"
        else:
            print()
            message = f"{name}님 불합격입니다.\n평균: {average}점\n다음에 더 좋은 결과를 기대합니다."

        super().__init__(message)
# end class FailedException

try:
    name = input('이름 입력 : ')

    kor = int(input("국어 점수 입력 : "))
    if kor < 0 or kor > 100:
        raise ValueError("점수는 0~100 사이여야 합니다.")

    eng = int(input("영어 점수 입력 : "))
    if eng < 0 or eng > 100:
        raise ValueError("점수는 0~100 사이여야 합니다.")

    math = int(input("수학 점수 입력 : "))
    if math < 0 or math > 100:
        raise ValueError("점수는 0~100 사이여야 합니다.")

    jumsu = [int(kor), int(eng), int(math)]


    for score in jumsu:
        if score <= 40:
            raise MinJumsuException(name, score)

        average = sum(jumsu) / len(jumsu)
        raise FailedException(name, average)


except ValueError as err:
    print('올바른 숫자 형식을 입력해 주셔야 합니다.')
    print(err)


except MinJumsuException as e:
    print('에러가 발생하였습니다.',e)

except FailedException as e:
    print('에러가 발생하였습니다.', e)

except Exception as err:
    print('에러가 발생하였습니다.',err)

