# #Lists
# # l1 = [1,2,3,4,5,6]
# # print(l1,type(l1),id(l1))
# # l1[3] = 88
# # print(l1,type(l1),id(l1))

# # l2= ["Sayan",88,True,2,""]
# # print(l2,type(l2),id(l2))
# # print(l2[0][::2])
# # print(l2[-2])

# # str = "abc"
# # print(type(str),str,id(str))
# # l3 = list(str) #list() converts string to list
# # print(l3,type(l3),id(l3))

# # l4 = ['a','b','c']
# # str1 = " Gate 2025 ".join(l4)
# # print(str1,id(str1))

# # l5 = ["Every","day","is","a","new","beginning"]
# # str2 = " ".join(l5)
# # print(l5,type(l5),id(l5))
# # print(str2,type(str2),id(str2))
# # str3 = "*".join(l5)
# # print(str3)

# # l1 = [23,"banana",True,0,87]
# # print(l1[0::2])

# # ll = l1.append([1,2,3])
# # print(ll)
# # l2 = [1,2,3,4]
# # l3 = [6,7,8,9]
# # l4 = l2.extend(l3)
# # print(l4)

# # l1 = [1,2,3,"sayan"]
# # l2 = l1 + [67,78]
# # print(l2)
# # a = 5
# # a+2
# # print(a)

# # l1 = [1,2,3]
# # print(l1,id(l1))
# # ll =l1+[9,10]
# # print(ll,id(ll))

# # l2 = [1,2,3]
# # print(l2,id(l2))
# # l2.append(9)
# # l2.append(10)
# # print(l2,id(l2))

# # l3 = l2*2
# # print(l3,id(l3))

# # list = ["arya","Sayan","Rimi"]
# # print("Rimi" in list + ["John"][2:])

# #2D list
# from operator import __add__


# list2D = [[1,2,3],[4,5,6],[7,8,9]]
# print(list2D)

# a = 10
# b = 13
# print(a.__add__(b))
def count(child_dict,i):
    if i not in child_dict.keys():
        return 1
    ans = 1
    for j in child_dict[i]:
        ans += count(child_dict,j)
    return ans
child_dict = dict()
child_dict[0] = [1,2]
child_dict[1]=[3,4,5]
child_dict[2]=[6,7,8]
print(count(child_dict,0))


