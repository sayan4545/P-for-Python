def happy():
    print("Happy birthday!")
def greet(name):
    print("Hi ,"+ name)
happy()
greet("Sayan")
def average(a,b):
    sum = a+b
    return sum/2

ans= average(8,9)
print(ans)

def processNumber(x):
    X = 72
    return x+3

y = 54
res = processNumber(y)
print(res)

def f(a,b):
    print(a,b)

y = 4
f(12,y)
f(y,y)

def mySum(x,y):
    sum = x+y
    return sum
a = 10
b = 20
c = mySum(a,b)
print(c)

def myFood(food):
    for x in food:
        print(x)

fruits = ["apple","banana","cherry"]
myFood(fruits)

def Loopy(l):
    for item in l:
        print(item)
myList = [1,2,3]
Loopy(myList)