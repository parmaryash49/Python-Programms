from array import *
n=int(input("how many elments you want to store.."))
Myarray=array('i',[])
for i in range(n):
    num=int(input("enter element:"))
    Myarray.append(num)
flag=False
for i in range(n-1):
    for j in range(n-1-i):
        if Myarray[j]>Myarray[j+1]:
            Myarray[j],Myarray[j+1]=Myarray[j+1], Myarray[j]
        flag=True
    
    if flag==False:
        print("Array is already sorted...")
        break
    else:
        flag=False


for i in Myarray:
    print(i)

