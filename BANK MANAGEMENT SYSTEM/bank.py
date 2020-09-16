import sys,random,time
import MySQLdb
class Bank():
    #add account...
    def __init__(self,name,account_no,password,balance):
        self.name=name
        self.account_no=account_no
        self.password=password
        self.balance=balance

    def disply(self):
    	print(self.name)
    	print(self.balance)
    #deposit money into account...
    def deposit(self):
        no=int(input("Enter Your account no.."))
        password=input("Enter Your password..")
        if (no==self.account_no and password==self.password):
            print(f"Welcome to Trusty bank..,{self.name} ")
        else:
            print("your account no or passoword is wrong....")



while(True):
    print("1:Add a account \n 2:Deposit money  \n 3:Withdraw money \n 4:Exit")
    choice=int(input("enter your choice"))
    if choice==1:
        name=input("Enter your name")
        print("pls wait your account no is generated..")
        account_no=random.randint(1000,5000)
        time.sleep(5)
        print(f"Your accout no is {account_no}")
        password=input("pls enter your password make sure you remeber for login")
        while(True):
            balance=int(input("how much money you want to add"))
            if balance<3000:
                print("pls put atleast 3000 rupess into account...")
            else:
                break
        b=Bank(name,account_no,password,balance)
        b.disply()
    
    elif choice==4:
        sys.exit()

   
        



    