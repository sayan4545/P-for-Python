# # square = lambda n : n*2
# # power = lambda x,y:x**y

# # print(square(3))
# # print(power(6,3))

# # sum_add = lambda numbers: sum(2*num for num in numbers)
# # print(sum_add([3,4,5]))

# # isEven = lambda x : x%2==0
# # isOdd = lambda x : x%2!=0

# # print(isEven(4),isOdd(6))

# # lambda z : z+1

# def do_twice(n,fn):
#     return fn(fn(n))
# print(do_twice(3,lambda x : x**2))

# bear =-1
# oskin = lambda f : f(bear)
# x = oskin(abs)
# print(x)

# def inc_maker(i):
#     return lambda x : x+i
# print(inc_maker(3)(4))

# fun = (lambda x : x*3+1 if x%2 else x/2)
# print(fun(11))
# print(fun(10))

def fold(fn,list):
    res = list[0]
    for x in list[1:]:
        res = fn(res,x)
    return res
print(fold(lambda a,b : b-a,[1,3,5,7]))