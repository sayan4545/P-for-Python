# class Point:
#     def __init__(self,x,y):
#         self.x_cord = x
#         self.y_cord = y
#     def __str__(self):
#         return '<{},{}>'.format(self.x_cord,self.y_cord)
#     def euclidian_dist(self,other):
#         return ((other.x_cord-self.x_cord)**2+(other.y_cord-self.y_cord)**2)**0.5
#     def distanceFromOrigin(self):
#         if self.x_cord == 0 and self.y_cord==0 :
#             return 0
#         return (self.x_cord**2+self.y_cord**2)**0.5
# class Line:
#     def __init__(self,A,B,C):
#         self.A = A
#         self.B = B
#         self.C = C
#     def __str__(self):
#         return '{}x +{}y +{} = 0'.format(self.A,self.B,self.C)
#     def point_on_line(self,point):
#         if self.A*point.x_cord +self.B*point.y_cord + self.C ==0:
#             return 'Point on line'
#         else:
#             return 'Point not on line'

# p1 = Point(0,0)
# p2 = Point(2,2)
# print(p1,p2)
# print(p1.euclidian_dist(p2))
# print(p2.distanceFromOrigin())
# l1 = Line(2,3,4)
# print(l1)
# l2 = Line(1,2,3)
# print(l1.B)
# p = Point(1,1)
# l = Line(1,1,-2)
# print(l.point_on_line(p))
# class Person:
#     def __init__(self,name_input,country_input):
#         self.name = name_input
#         self.country = country_input
#     def greet(self):
#         if self.country == 'India':
#             return 'Namaste', self.name
#         else:
#             return 'hello',self.name

# p = Person('Sayan','Rnp')
# print(id(p))
# q = p
# #def greet(person):
#     #print('My name is ',person.name ,' and I live in ',person.country)
# #greet(p)
# def greet_01(person):
#     person.name = 'xxxx'
#     return person
# p2 = greet_01(p)
# print(id(p2))

class Human :
    population = 1
    def __init__(self,name,religion,sex):
        self.name = name
        self.religion = religion
        self.sex = sex
        self.pop = Human.population
        Human.population +=1
    def __str__(self):
        return '{}->{}->{}-->{}'.format(self.name,self.religion,self.sex,self.pop)
            
Chandrika = Human('Chandrika','Hindu','F')
Sayan = Human('Sayan','Hindu','M')

print(Chandrika)
print(Sayan)
print(Human.population)