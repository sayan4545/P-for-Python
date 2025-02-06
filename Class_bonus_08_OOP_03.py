class geometry:
    def __init__(self,type,length,breadth):
        self.type = type
        self.length = length
        self.breadth = breadth
    def area(self,length,breadth):
        return length *breadth
    
class Square(geometry):
    def area(self,side):
        return side*side
class Rectangle(geometry):
    pass
s1 = Square('Quadrilateral',3,3)
print(s1.area(3))
s2 = Rectangle('Quad',3,4)
print(s2.area(3,4))