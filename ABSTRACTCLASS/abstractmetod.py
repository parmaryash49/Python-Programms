# class Myclass:
# 	def calculate(self,x):
# 		print("square value=",x*x)

# obj1=Myclass()
# obj1.calculate(2)

# obj2=Myclass()
# obj2.calculate(3)

# obj3=Myclass()
# obj3.calculate(4)

from abc import ABC,abstractmethod
class Myclass(ABC):
	@abstractmethod
	def calculate(self,x):
		pass

class sub1(Myclass):
	def calculate(self,x):
		print("square value=",x*x)
import math
class sub2(Myclass):
	def calculate(self,x):
		print("square root=",math.sqrt(x))

class sub3(Myclass):
	def calculate(self,x):
		print("cube is",x**3)

obj1=sub1()
obj1.calculate(2)

obj1=sub2()
obj1.calculate(16)

obj1=sub3()
obj1.calculate(2)