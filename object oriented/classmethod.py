class Bird:
    n=0
    wings=2
    def __init__ (self,name):
        Bird.n=Bird.n+1
        self.name=name

    def display(self):
    	print(self.name)
    
    @staticmethod
    def objects():
        print("no of instances created",Bird.n)

    @classmethod
    def fly(cls,name):
        print(f"{name} is fly with 2 wings..")

Bird.fly("sparrow")
Bird.fly("parrot")
b1=Bird("yash")
b2=Bird("kamesh")
b1.display()
b2.display()
Bird.objects()