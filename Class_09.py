# # letters = ['a','b','c','d','e']
# # numbers = [1,2,3,4]
# # zipped = zip(letters,numbers)
# # list(zipped)
# # print(*zipped)

# # print(tuple(zip("Hello","World","Sayan","Chandrika")))
# # print(list(zip((1,2,3),range(0,5,2))))
# for tup in zip((1,2,3,4),range(10),"ABCD","EFGH","IJKL","MNOP"):
#     print(tup)

# xvec = [10,20,30]
# yvec = [1,2,3]
# print(list(x*y for x,y in zip(xvec,yvec)))

# pairs = [(1,'a'),(2,'b'),(3,'c')]
# numbers,letters = zip(*pairs)
# print(numbers)
# print(letters)

# x = [1,2,3]
# y = [3,4,5]
# new_x,new_y = zip(*zip(x,y))
# print(new_x,new_y)
# m = [[1,2,3],[5,6,7]]
# print(list(zip(*m)))

parts = [['1','2'],['3','4'],['5','6']]
print(list(zip(parts[0],parts[1],parts[2])))
