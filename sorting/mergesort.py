def mergesort(list1):
    if len(list1)>1:
        mid=len(list1)//2
        left_list=list1[:mid]
        right_list=list1[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i=0
        j=0
        k=0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                list1[k]=left_list[i]
                i=i+1
                k=k+1
                print(list1)
            else:
                list1[k]=right_list[j]
                j=j+1
                k=k+1
                print(list1)
        # print("hello")
        # print(i ,j)
        while len(left_list)>i:
            list1[k]=left_list[i]
            i=i+1
            k=k+1
        while len(left_list)<j:
            list1[k]=left_list[j]
            j=j+1
            k=k+1
        
num=int(input("enter number for total elments"))
list1=[int(input())for x in range(num)]
mergesort(list1)
print("sorted list is",list1)
