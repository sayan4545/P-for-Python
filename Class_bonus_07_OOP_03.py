# # # class User:
# # #     def __init__(self):
# # #        self.name = 'Sayan'
# # #     def login(self):
# # #         print('login')

# # # class Student(User):
# # #     def __init__(self):
# # #         super().__init__()
# # #         self.id = 10000000
# # #     def enroll(self):
# # #         print('Enrolled into the course')

# # # s1 = Student()
# # # s1.login()
# # # print(s1.name)
# # class Phone:
# #     def __init__(self,price,brand,color):
# #         print('Inside the phone constructor')
# #         self.__price = price
# #         self.brand = brand
# #         self.color = color
# #     def buy(self):
# #         print('Buying a phone')
# #     def show(self,__price):
# #         print(self.__price)
# # class SmartPhone(Phone):
# #     #pass
# #     # def __init__(self,os,ram):
# #     #     print('Inside smartphone constructor')
# #     #     self.os = os
# #     #     self.ram = ram
# #     def check(self):
# #         print(self.__price)
       

# # s1 = SmartPhone(1200,'MI','Black')
# # # print(s1.brand,s1.color,s1.price)
# # # s1.buy()

# # class parent:
# #   def __init__(self,num):
# #     self.__num = num
# #   def get_num(self):
# #     return self.__num
# # class Child(parent):
# #   def __init__(self,val,num):
# #     self.__val = val
# #   def getVal(self):
# #     return self.__val
# #   def show(self):
# #     print('Child class')
# # son = Child(100,10)
# # print('Parent : num',son.get_num())
# # print('Child: val',son.getVal())

# class A :
#   def __init__(self):
#     self.var1 = 100
#   def display1(self,var1):
#     print("Class A: ",self.var1)
# class B(A):
  
#   def display2(self,var1):
#     print("Class B: ",self.var1)
# obj = B()
# obj.display1(200)
def override(method):
   def wrapper(*args, **kwargs):
     return method(*args, **kwargs) 
   return wrapper
def override2(method):
   def wrapper(*args, **kwargs):
     return method(*args, **kwargs) 
   return wrapper
class Phone:
    def __init__(self,brand,price,camera):
        self.brand = brand
        self.price = price
        self.camera = camera
    def buy(self):
        print("Buy a phone")
class SmartPhone(Phone):
    def __init__(self,price,brand,camera,color,ram):
      #  super().__init__(price,brand,camera,brand,price,camera)
       self.color = color
       self.ram = ram
       super().__init__(price,brand,camera)
    @override
    def buy(self):
        print('Buy a SP')
        super().buy()
S1 = SmartPhone('Nokia',76888,108,'Black',8)
S1.buy()
class parent:
   def __init__(self):
      self.num =100
class child(parent):
   def __init__(self):
      super().__init__()
      self.var =200
   def show(self):
      print(self.num)
      print(self.var)
c1 = child()
c1.show()