# list1=[1,2,4,5,9]
# # s=list(filter(lambda x:x*x,list1))
# # print(s)
# def square(list1):
#     for i in range(1,list1):
#         list1[i]= list1[i]* list1[i]
#     return list1
    
# s=list(filter(square,list1))
# print(s)

def square(x):
    return x*x

l=[3,2,4]
lst1=list(filter(square,l))
print(lst1)
