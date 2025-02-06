# # str = "STELLA"
# # print(str[0])
# # print(str[1])
# # print(str[2])
# # print(str[3])
# # print(str[4])
# # print(str[5])
# # print(str[-1])
# # print(str[-2])
# # print(str[-3])
# # print(str[-4])
# # print(str[-5])
# # print(str[-6])

# s1 = "WILLIAMSON"
# s2 = "SON"
# s3 = "WILLSON"
# # print(s2 in s1)
# # print(s3 in s1)
# # print(s3 not in s1)

# print(s1[0:])
# print(s1[-10:])
# print(s1[2:8])
# print(s1[:])

# month = "January"
# day =10
# output_string = ""

# if day<=10:
#     output_string += "Early"

# if day>10:
#     output_string += "late"
# else:
#     output_string += "Mid"
# output_string += month
# print(output_string)

# a = [6,5,4,3,2,1,0]
# b = "success"
# c = b[a[-3]] + b[::4]
# print (c,type(c))
# d = a[1]*a[2]*a[-3]*a[4//2]
# print(d,type(d)) # 160

x = "HelloWorld"
print(x[5::-1])
print(x[5:0:-1])
y = "HELLO"
print(y[-1::-1])

z = "WILLIAMSON"
print(z[::-2])

aphbt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(len(aphbt))
print(aphbt[7:9]) #HI
print(aphbt[-3:-1])#XY

#Strintg methods 
# str = "hello"
# print (str.upper(),id(str.upper())) #Doesnot modify the string. 
# print(str,id(str))

# s = "hello"
# s = s.upper()
# print(s,id(s),id(s.upper()))
# short circuit evaluation
p = (1>1) or (2<=3)
print(int (p))



