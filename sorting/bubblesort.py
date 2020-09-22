def bubblesort(list1):
    for j in range(len(list1)-1):
        for i in range(len(list1)-1):
            if(list1[i]>list1[i+1]):
                list1[i],list1[i+1]=list1[i+1],list1[i]

num=int(input("enter howmany element you want to store."))
list1=[int(input())for i in range(num)]
bubblesort(list1)
print(list1)