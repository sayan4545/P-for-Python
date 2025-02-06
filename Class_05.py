# # for i in range(1,5,2):
# #     print("Hello!")

# # for i in range(1,11):
# #     print("when i = ",i,"i^2=", i*i)

# for i in range(1,11):
#     print(str(i),". ",i*5)

# for i in range(10,5,-1):
#     print(i)

#Nested loops
# for x in range(5):
#     for y in range(x):
#         print("x: ",x," y: ",y)

# for x in range(5):
#     for y in range(4):
#         print("x: ",x," y: ",y)

# for i in [1,2,3,4,5,6,7,8,8]:
#     print(i)
#     if(i>=4):
#         break
# print("Out of loop")
# numbers = [2,3,11,7,5]
# for i in numbers:
#     print("Current number is : ",i) # 2,4,3,9,11,7,49,5,25
#     if(i>10):
#         continue
#     square = i*i
#     print("Square of the current number is : ",square)

# li = [2,4,6,8]
# dli = [2*x for x in li]
# print(dli)

# # nos = [1,2,3,4,0,-2]
# # squares = [i*i for i in nos if i!=0]
# # print(squares)

# nums = [1,2,3,4,5,6,7]
# numss = [num for num in  nums if num %2==0]
# print(numss)

# print([str(x)+str(x) for x in range(10) if x %2==0])

# row = int(input("Enter the number of rows: "))
# for i in range(row):
#     str = ""
#     for j in range(row):
#         str = str + "* "
#     print(str)

# for row in range(4):
#     print_str = ""
#     for col in range(row+1):
#         print_str = print_str +"* "
#     print(print_str)
# row = 4
# for i in range(row):
#     pstr = ""
# #     for j in range(row):
# #         if i==0 or i == row-1:
# #             pstr = pstr+"* "
# #         if j == 0 or j==row-1:
# #             pstr = pstr +"* "
# #         pstr = pstr+ " "
# #     print(pstr)

# row = 4
# for i in range(row):
#     pstr = ""
#     for j in range(row-i-1):
#         pstr = pstr+" "
#     #print(pstr)
#     for j in range(i+1):
#         pstr = pstr+"* "
#     print(pstr)

row = int(input("Enter the number of rows: "))
for i in range(row):
    st = ""
    for j in range(row-i-1):
        st = st + " "
    for j in range(i+1):
        st = st + str(i+1) +" "
    print(st)

row = int(input("Enter the number of rows: "))
ctr = 1
for i in range(row):
    st = ""
    for j in range(row-i-1):
        st = st + " "
    for j in range(i+1):
        st = st + str(ctr) +" "
        ctr = ctr+1
    print(st)

