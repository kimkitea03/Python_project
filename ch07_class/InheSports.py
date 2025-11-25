class Sports:
    def __init__(self,name,entry):
        self.name = name
        self.entry = entry
    # end def __init__
    def showData(self):
        print('종목 : %s ' % self.name)
        print('엔트리 : %d명' % self.entry)
# end class Sports

class BaseBall (Sports):
    def __init__(self,name,entry,average):
        super().__init__(name,entry)
        self.average = average
    # end def __init__

    def showPlay(self):
        super().showData()
        print('타율 : %.3f'%self.average)
        print('-'*20)
    # end def showPlay
# end class BaseBall

class FootBall(Sports):
    def __init__(self,name,entry,score):
        super().__init__(name,entry)
        self.score = score
    # end def __init__

    def showPlay(self):
        super().showData()
        print('골수 : %d' %self.score)
        print('-'*20)
    # end def showPlay
# end class FootBall

base = BaseBall('야구',9,0.235)
base.showPlay()

foot = FootBall('축구',11,5)
foot.showPlay()