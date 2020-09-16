class Student():
    def __init__(self):
        self.name="milan"
        self.age=34
        self.date='27/12/97'
    
    def display(self):
        print(f"my name is {self.name}")
        print(f"my age is {self.age}")
        print(f"my date is {self.date}")
    
s=Student()
print(s.display())