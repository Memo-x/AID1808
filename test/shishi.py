# # 输入X升水和Y升水，输入Z，最后得到Z升水
# L = []
# def suanfa(x,y,a):
#     try:    
#         qy = y%x
#         if qy == z:
#             print("已经实现完毕")
#         else:               
#             b = a-(x-qy)
#             if b == z:
#                 L.append([x,b])
#                 print("已经实现完毕")
#             else:
#                 L.append([x,b])
#                 return suanfa(x,b,a)       
#         print(L)
#     except RecursionError:
#         print("数据有误，无法实现")
     
# x = int(input("请输入一个整数："))
# y = int(input("请输入一个整数："))
# a = y
# z = int(input("请输入一个整数为想得到的结果"))
# suanfa(x,y,a)


# def s(x):
#     if x>1:
#         return x*s(x-1)
#     else:
#         return x

# print(s(5))

# def s(x):
#     if x == 1:
#         return 1
#     else:
#         a = x*s(x-1)
#         return a
        

# print(s(5))

def print_list(lst):
    sum = 0 
    for x in lst:
        if type(x) is int:
            sum += x
        if type(x) is list:
            sum += print_list(x) 
    return sum

L = [[3,5,8],10,[[13,14],15,18],20]
print(print_list(L))













