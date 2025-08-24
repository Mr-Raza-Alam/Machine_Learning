'''
This is for cal. area and perimeter of different shapes  
'''


class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class Tailor:
    def __init__(self,sk,*d):
        self.s_kind = sk.lower()
        self.dimensions = d
    def area(self):
        if self.s_kind == 'circle':
            rad, = self.dimensions
            return 3.14*rad**2
        elif self.s_kind == 'square':
              edge, = self.dimensions
              return edge**2
        elif self.s_kind == 'rectangle':
            l,b,= self.dimensions
            return l*b
        elif self.s_kind == 'triangle':
            b,h, = self.dimensions
            return 0.5*b*h
        else:
            return 'Undefined Shape'
    def perimeter(self):
        if self.s_kind == 'circle':
            rad, = self.dimensions
            return 2*3.14*rad
        elif self.s_kind == 'square':
              edge, = self.dimensions
              return 4*edge
        elif self.s_kind == 'rectangle':
            l,b,= self.dimensions
            return 2*(l+b)
        elif self.s_kind == 'triangle':
            a,b,c, = self.dimensions
            return a+b+c
        else:
            return 'Undefined Shape'