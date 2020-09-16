from array import *
n=int(input("how many elments you want to store.."))
Myarray=array('i',[])
for i in range(n):
    num=int(input("enter element:"))
    Myarray.append(num)

searchelement=int(input("enter element that you want to search..."))
flag=False
# for i in range(len(Myarray)):
#     if searchelement==Myarray[i]:
#         print(f"{searchelement} is found at position {i+1}")
#         flag=True
# if flag==False:
#     print("element not found in the array..")

#using index method..

try:
    pos=Myarray.index(searchelement)
    print("found at postion ",pos+1)
except ValueError:
    print("not found in the array...")

for i in Myarray:
    print(i)

