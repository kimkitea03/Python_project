import math

class Circle:
    type = '원'

    def __init__(self, xpos, ypox, radius):
        self.xpos = xpos
        self.ypox = ypox
        self.radius = radius

    def showinfo(self):
        print('원 중심 : {},{}'.format(self.xpos, self.ypox))
        print('반지름 : {}'.format(self.radius))

        # preimeter = 2*

        print('면적 : %.1f'%(self.radius*self.radius*3.14))
# end class


print('도형의 타입 : %s' % Circle.type)
print('-'*20)

circle1 = Circle(3, 5, 10)
circle1.showinfo()
print( '-' * 20 )
circle2 = Circle(8, 6, 20)
circle2.showinfo()


