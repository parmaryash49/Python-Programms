def binarysearch(list1, key):
    print("function is calling")
    low = 0
    high = len(list1)-1
    while low <= high:
        mid = (low+high)//2
        if key == list1[mid]:
            return mid
        elif key > list1[mid]:
            low = mid+1
        else:
            high = mid-1
    return -1
    # if found==True:
    #     print("key is found",list1[mid])
    # else:
    #     print("key is not found",list1[mid])


numbers = [12, 34, 56, 78, 90, 100]
print("helo")
ans=binarysearch(numbers,100)
if ans==-1:
    print("element is not found...")
else:
    print("the element found at",ans)


