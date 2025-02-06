# # def func(a,b=5,c=10,d=20):
# #     print("a :",a)
# #     print("b :",b)
# #     print("c :",c)
# #     print("d :",d)
# # func(1)
# # func(1,2)
# # func(1,2,3)
# # func(1,2,3,4)

# # def myFunc(a,b,c,d):
# #     print(a,b,c,d)

# # myFunc(a=2,b="Sayan",c = True,d = "Chandrika")
# #Tuples
# # t = ()
# # t1 = (1,2,"Sayan Chatterjee",True)
# # print(t1,type(t1),id(t1))
# # l1 = [1,2]
# # print(l1,type(l1),id(l1))
# # l2 = tuple(l1)
# # print(l2,type(l2),id(l2))
# # a = (10,)
# # print(a,type(a),id(a))

# val = (10,20,30)
# a,b,c = val
# print(a,b,c)
# print(type(a))

# x = 1
# y = 2
# print(x,y) # 1,2
# x = y
# y = x
# print(x,y) # 2,2
# x = 1
# y = 2
# print(x,y)
# x,y = (y,x)
# print(x,y)
# a = (1,2,3,4,5)
# x,y, *rest = a
# print(x,y,rest) 

# def f1(t1,t2):
#     return t1+t2,t1-t2

# a,b = f1(3,4)
# print(a,b,type(f1),type(a))

# def myFunc(*numbers):
#     total =0
#     for num in numbers:
#         total = total + num
#     return total
# print(myFunc(1,2,3,4,*[5,6,7]))

def linearSearch(list,target):
    for i in range(len(list)):
        if list[i] is target:
            return i
    return -1
print(linearSearch([1,2,"STT",True],True))    
    