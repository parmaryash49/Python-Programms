class Square:
	def __init__(self,x):
		self.x=x
	def area(self):
		print("Area of Square",self.x*self.x)

class Rectangle(Square):
	def __init__(self,x,y):
		super().__init__(x)
		self.y=y
	def area(self):
		super().area()
		print("Area of Rectangle:",self.x*self.y)

a,b=[float(x) for x in input("Enter two number").split()]
r=Rectangle(a,b)
r.area()

s=Square(10)
s.area()