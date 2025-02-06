# number = 23
# print(type(number),number,id(number))
# number = number + 1
# print(number, id(number))

# a = 10
# b = a
# print(a,b)
# a = a+1
# print(a,b)
# a = [4,5]
# b = a
# b[0] = 1
# print(a)

# weather = [65,"light rain",8,"SSW",26.87]
# new_weather = weather # donot create a new list. copy the reference only.
# new_weather[1] = "Cloudy"
# print(weather,id(weather))
# print(new_weather,id(new_weather))

# alist = ["ab","bc","cd","de","ef"]
# aslice = alist[2:5] # creates a new list object
# print(alist,id(alist))
# print(aslice,id(aslice))

# a = [4,5]
# b = a[:]
# b[0] =1
# print(a,id(a))
# print(b,id(b))

# l1 = [1,2,3]
# l2 = l1
# l3 = [l1,l1,l1]
# l1[0] =5
# print(l3[0])

# l1 = [1,2,3]
# l2 = l1
# l3 = [l1[:],l1[:],l1[:]]
# l1[0] = 5
# print(l3[0])

# l1 = [1,2,3]
# l2 = l1
# l3 = l1+[4]
# l1.append(5)
# print("L1= ",l1)
# print("L2= ",l2)
# print("L3= ",l3)

A = [1,2]
B = list(A)
C = A
D = A[:]
B[1]=7
print(A,id(A))
print(B,id(B))
print(C,id(C))
print(D,id(D))
