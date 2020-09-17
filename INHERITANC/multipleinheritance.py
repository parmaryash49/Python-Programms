class Father:
	def height(self):
		print("height is 6.00 foot")
class Mother:
	def color(self):
		print("color is white")

class son(Father,Mother):
	pass

s=son()
s.height()
s.color()