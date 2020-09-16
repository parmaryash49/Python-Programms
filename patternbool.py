boolvar=int(input("enter 1 or 0"))
boolvar=bool(boolvar)
number=int(input("how many rows you want to print..."))
if boolvar ==False:
    for i in range(0,number):
        for j in range(i+1):
            print("*",end="  ")
        print()
else:
    for i in range(0,number):
        for j in range(0,number-i):
            print("*",end="  ")
        print()