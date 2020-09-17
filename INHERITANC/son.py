from father import Father
class Son(Father):
	# pass
	def __init__(self):
		self.property=2000
	def display(self):
		print("property is",self.property)

s=Son()
s.display()
