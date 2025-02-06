# a = 23
# b = 34
# def f1():
#     global a
#     a = 22
#     global c
#     c = 199
#     return a
# def f2(a):
#     return a
# print(f1())
# print(f2(100))
# def mystery(t,x):
#     for v in t:
#         if v==x:
#             return True
#     return False

# print(mystery(['a','b','c'],'d'))
# print(mystery(['a','b','c'],'c'))
# def mystery(a):
#     print(a)
#     for i in range(1,len(a)):
#         a[i]= a[i]+a[i-1]
#         print(a)
# mystery([8,5,0,-7,4])

# def silly(x):
#     print("start silly")#1
#     print(x)#5
#     funny(x+2)
#     print('End silly')#6
# def funny(y):
#     print("Start funny")#3
#     print(y*3)#21
#     print("End funny")#5
# silly(5)

# def silly(x):
#     print("Start silly")
#     print(x)
#     goofy(x-1)
#     funny(x+2)
#     print("End silly")
# def funny(y):
#     print("Start funny")
#     print(y)
#     goofy(y*2)
#     print("End funny")

# def goofy(x):
#     print("Start goofy")
#     print(x)
#     print('End goofy')

# silly(3)

# dogs = ["Fido","ruff"]
# foo=[]
# k = 1
# for dog in dogs :
#     foo.append(k)
#     foo.append(dog)
#     k+=1
# print(foo)
# print(k)

# def hofun(fun,seq):
#     return [fun(seq,s) for s in seq]

# def f (seq,i):
#     return seq[0]+i

# result = hofun(f,[1,3,2])
# print(result)

# l = ['a','b']
# def func(p,q):
#     p.append(q)
# func(l,'c')
# print(l)

# d = "HELLO"
# print(d,id(d))
# def func(p):
#     p = p + " World" 
#     return p
# print(func(d),id(d))
# print(d,id(d))

# l = ['a','b']
# def func(p,q):
#     p.append(q)
# func(l[:],'c')
# print(l)

# def f(L):
#     L = [1,2,3]
#     L[0]=5
#     print(L[0])
# L1 = [4,5,6]
# f(L1)
# print(L1[0])

# def h(L):
#     L[1]=[7,8]
#     L[0]=[5,6]
#     L[0][0]=9
#     print(L)
# L=[[1,2],[3,4]]
# h(L)
# print(L)

# def greet(name = "Chandrika"):
#     print("Hi", name)
# greet('Sayan')
# greet()

# def foo(x,y=0):
#     return x,y

# result = foo(5)
# print(result)

def fun(x,y,z=2):
    print(x,y,z)
fun(1,2)

def append_to(element,to=[]):
    to.append(element)
    return to
print(append_to(42))
print(append_to(15))


