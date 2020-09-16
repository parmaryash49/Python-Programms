# lists=[12,34,56,2,89,78,0]
# max1=lists[0]
# # lists.sort()
# print(max(lists))
# print(max1)
# for i in lists:
#     if i > max1:i
#         max=i
# print("max is",max1)


# num=int(input("enter the number"))
# if num%2==0:
#     print("this is even number")
# else:
#     print("this is odd")
numbers=[12,45,20,40,11,99,77,22]
print(numbers[4])
numbers[4]=100
print(numbers)
even_numbers=[]
odd_numbers=[]
for i in numbers:
    if i % 2==0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print(even_numbers)
print(odd_numbers)
