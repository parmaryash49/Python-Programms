class Student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    
    def display(self):
        print(f"your  name is {self.name}")
        print(f"your marks is {self.marks}")
    
    def calculate(self):
        if (self.marks >70):
            print("you  got a grade..")
        elif(self.marks >=50 and self.marks<=70):
            print("you got b grade..")
        else:
            print('you are fail..')

n=int(input("how many students..."))
i=1
# marks=[]
while(i<=n):
    sum=0
    name=input("enter your name")
    marks=[int(num) for num in input().split(' ')]
    print(marks)
    for i in range(len(marks)):
        sum=sum+marks[i]
    print(sum)
    s=Student(name,sum)
    s.display()
    s.calculate()
    i+=1