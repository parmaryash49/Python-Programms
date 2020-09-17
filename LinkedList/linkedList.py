linkedlist=[]
linkedlist.append("India")
linkedlist.append("Australia")
linkedlist.append("Japan")
choice=0
print("The Existing List=",linkedlist)
while choice<5:
    print("Linked List operations..")
    print("1:Add element")
    print("2:Remove elment")
    print("3:Replace element")
    print("4:Search for element")
    print("5:Exit")
    choice=int(input("Enter Your choice"))
    if choice==1:
        element=input("enter country name")
        pos=int(input("At what position?"))
        linkedlist.insert(pos,element)
    elif choice==2:
        try:
            element=input("Enter element:")
            linkedlist.remove(element)
        except ValueError:
            print("Element not found..")
    elif choice==3:
        element=input("Enter a new element")
        pos=int(input("At what position"))
        linkedlist.pop(pos)
        linkedlist.insert(pos,element)
    elif choice==4:
        element=input('Enter element')
        try:
            pos=linkedlist.index(element)
            print('Element found at position:',pos)
        except ValueError:
            print("Elment not found")
    else:
        break
    print('List=',linkedlist)




