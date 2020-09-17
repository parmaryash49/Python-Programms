class Father:
	def __init__(self,property):
		self.property=8000
	def display(self):
		print("father property,",self.property)

class Son(Father):
	# pass
	def __init__(self):
		super().__init__(property)
		self.property1=2000
	def display(self):
		print("total property is",self.property+self.property1)

s=Son()
s.display()