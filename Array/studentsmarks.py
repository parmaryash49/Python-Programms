from array import *
def sumandavg(marks):
    sum=0
    for i in range(len(marks)):
        sum+=marks[i]
    print("total sum is ",sum)
    avg=sum/(len(marks))
    print("avg is ",avg)

# marks=input("enter marks").split('\n')
n=int(input("how many records you want insert..."))
marks=[]
for i in range(0,n):
    # num=(int(input("enter the number..")))
    # marks.append(num)
    marks.append(int(input("enter the number")))
    print(marks)

# marks=[int(num) for num in marks]
# for i in range(len(marks)):
#     print(marks[i])
sumandavg(marks)
for i in marks:
    print(i)