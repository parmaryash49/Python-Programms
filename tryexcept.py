try:
    num1=int(input("enter the number"))
    num2=int(input("enter the number2"))
    print("the sum is ",num1+num2)
except Exception as e:
    print("you need to enter only numbes..")
    print(e)
finally:
    print("finally successful..")