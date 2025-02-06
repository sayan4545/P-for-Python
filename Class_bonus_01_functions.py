# def is__even(x):
#     """
#     The function, accepts a positive integer , 
#     returns true,if it is even, otherwise false

#     """
#     if type(x) != int:
#         return 'Invalid entry'
#     if x%2==0:
#         return True
#     return False
# # print(is__even(3))
# # print(is__even(4))

# for i in range(1,11):
#     even_odd = is__even(i) 
#     if even_odd is True:
#         print('i: ',i," ", 'even')
#     else:
#         print('i: ',i," ",'odd')

# print(is__even("Hello"))

# def power(a=2,b=2):
#     """
#     Takes two integers as input oparameters and gives the 
#     power of second input to the first as result, if no 
#     input provided, takes 2 as input in both the parameters.

#     """
    
#     return a**b

# print(power(3,1.6))
# def add(a,b):
#     """
#     Adds two numbers a and b provided as input to the function
#     """
#     if isinstance(a,(int,float,complex)) and isinstance(b,(int,float,complex)) :
#         return  a+b
#     return 'invalid'
# sum = add(a=8,b=5)
# print(add(sum,add(3,add(4,add(sum,add(1,2))))))
# def multiply(a,*b):
#     result = a
#     for num in b:
#         result *=num
#     return result

# print(multiply(2,3,4))
# def display(**kwargs):
#     for(key,value) in kwargs.items():
#         print(key,'->',value)

# display(India ="Kolkata",Australia= 'Melbourne')

# def demo(a,b,*args,**kwargs):
#     i =0
#     for (key,value) in kwargs.items():
#         if i<len(args):
#             print(a+1,b+1,args[i],key,'->',value)
#             i=i+1
        
        
# demo(3,4,1,2,3,4,Sayan="Q",Chandrika ="R")
# def g(y):
#     print(x)
#     print(x+1)
# x =5
# g(x)
# print(x)
# def f(y):
#     x =1 # a local variable x initialized to 1
#     x +=1 # x =2
#     print(x) # prints 2
# x =5 # global scope x =5
# f(x) # function called, and in the function scope, y =5
# print(x) # prints 5 
# def h(y):
#     global x
#     x +=1
# x =5
# h(x)
# print(x) # 6
# def f(x):
#     x = x+1
#     print('in f(x) : x = ',x)
#     return x
# x = 3
# z = f(x)
# print('in main prg scope: z = ',z)
# print('inj main prg scope: x = ',x)

# def f():
#     def g():
#         print('Inside function g')
#     print('Inside function f')
#     g()
# f()

# def f():
#     def g():
#         print('Inside function g')
#     f()
#     print('Inside function f')
# f() # stack over flow. infinite recursion

# def g(x):
#     def h():
#         x ='abc'
#     x = x+1
#     print('In g(x): x = ',x)
#     h()
#     return x
# x = 3
# z = g(x)

# def square(x):
#     return x**2
# print(square(2)+square(3))

# y = square
# print(y(3),id(y),id(square),type(y))
# del(square)
# #square(3)
# print(y(3))

# def f():
#     def x(a,b):
#         return a+b
#     return x
# val = f()(3,4)
# print(val)

# def func_a():
#     print('Inside func_a')
# def func_b(z):
#     print('Inside func_b')
#     return z()
# print(func_b(func_a))
# isPresent = lambda str : 's' in str
# print(isPresent('sayan'),isPresent('chandrika'))

# def square(num):
#     return num**2
# def transform(f,lst):
#     output =[]
#     for l in lst:
#         output.append(f(l))
#     print(output)

# transform(square,[1,2,3,4,5])

# print(list(map(lambda x : x**2,[1,2,3,4,5])))
# print(list(map(lambda x : 'even' if x%2==0 else 'odd',[1,2,3,4,5,6])))
#print(list(filter(lambda x : x%2,[1,2,3,4,5,6,7,8])))
print(list(filter(lambda x :x%2,[1,2,3,4,5,6,7,8,9,10])))






    



