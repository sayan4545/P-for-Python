class Fraction:
    def __init__(self,x,y):
        if y ==0:
            raise ValueError("Denominator cannot be zero")
        self.num =x
        self.din = y
        #self.convertFraction()
    def __str__(self):
        return '{}/{}'.format(self.num,self.din)
    def __add__(self,other):
        new_num = self.num*other.din+other.num*self.din
        new_din = self.din*other.din
        return '{}/{}'.format(new_num,new_din)
    def __sub__(self,other):
        new_num = self.num*other.din-other.num*self.din
        new_din = self.din*other.din
        return '{}/{}'.format(new_num,new_din)
    def __mul__(self,other):
        return '{}/{}'.format(self.num*other.num,self.din*other.din)
    def convertFraction(self):
        fraction = self.num/self.din
        return fraction



fr1 = Fraction(2,5)
fr2 = Fraction(4,5)
print(fr1)
print(fr2)
print(fr1+fr2)
print(fr1-fr2)
print(fr1*fr2)