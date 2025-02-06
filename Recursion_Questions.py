#1
# def mystery(n):
#     if n<10:
#         return n
#     else:
#         a = n//10
#         b = n%10
#         return mystery(a+b)
# print(mystery(678))
#2
# def f(l,v):
#     if not l:
#         return 0
#     count = 1 if l[0]>v else 0
#     return count + f(l[1:],v)
# l =[3,7,1,9,5]
# v = 4
# print(f(l,v))

# def f(lst,i=0):
#     if i ==len(lst):
#         return
#     f(lst,i+1)
#     if(lst[i]%2!=0):
#         print(lst[i]," ")
# lst = [1,2,3,4,5]
# f(lst)

# def f(t):
#     if not t:
#         return 0
#     return t[0][0]+f(t[1:])
# t = [[1,2],[0,4],[5,6]]
# print(f(t))

