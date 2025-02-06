print(set(map(lambda x: x**2,range(1,5))))

def  f1(x,y):
    return x+y
print(list(map(f1,[1,2,3,4],[4,5,6,7])))

def f2(x):
    return x%2==0
print(list(filter(f2,[1,2,3,4,5,6,7,8,9,10])))

def f3(x):
    y = 10
    return (x+y)%2==0

print(list(filter(f3,[1,2,3,4])))
