class Account: # 클래스 정의
    bankname = 'KB' # 클래스 변수 (자바에 스테틱 변수와 유사)

    def __init__(self, name, no, deposit): # 약간 self가 this같은 느낌인거 같음
        # 인스턴스 변수 : self 키워드를 사용하여 선언한 변수
        self.name = name
        self.no = no
        self.deposit = deposit
    # end def __init__
    def printData(self):
        print('예금주 : %s' % self.name)
        print('계좌 번호 : %s' % self.no)
        print('예치금 : %s' % self.deposit)
#end class Account

print('주거래 은행 : %s' %Account.bankname)
print('-'*30)

soo = Account('김철수', 1234, 1000) # 객체 생성
soo.printData()
print('-'*30)


hee = Account('박영희', 5678, 2000)
hee.printData()

