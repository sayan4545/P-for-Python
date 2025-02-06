# Local scope
# def myFunc(x):
#     y = 23
#     return x+y

# res = myFunc(23)
# print(res)
# #print(x) -- This will throw error
# Global scope
# x = 90 # Global scope of variable x
# def f2(x): # local scope of variable x
#     return x
# print(f2(45)) # prints 45
# print(x) # prints 90
# x = 90
# def f1():
    
#     global x
#     x = 89
#     return x
# print(f1())
# print(x)

# a = 3
# b = 2
# def foo(x):
#     return a+x
# def bar(x):
#     b =1
#     return b+x
# print(foo(3),bar(3))

# a = 1
# b = 2
# def foo():
#     global a
#     a = 2
#     b = 3
#     print("In foo: ","a = ",a,"b =",b)
# print("Outside foo: ","a = ",a,"b= ",b)
# foo()
# print("Outside foo: ","a = ",a,"b= ",b)

# a = 100
# def bar1():
#     print(a)
#     print(a+a)
# def bar2():
#     print(a)
# bar1()
# bar2()

a = 100
def bar():
    global a
    a = a+1
bar()
print(a)




