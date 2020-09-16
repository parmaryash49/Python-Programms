while(True):
    string=input("enter the string")
    # for i in range(len(string)):
    #     for j in range(len(string)-i):
    #         print(string[j],end=" ")
    #     print()
    for i in range(len(string)):
        for j in range(i+1):
            print(string[j],end=" ")
            # print("*",end=" ")
        print()
