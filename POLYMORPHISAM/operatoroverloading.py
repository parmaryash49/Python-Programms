# print(10+15)
# s1="red"
# s2="fort"
# print(s1+s2)

# a=[10,20,30]
# b=[5,15,-10]
# print(a+b)

# class BookX:
# 	def __init__(self,pages):
# 		self.pages=pages

# class BookY:
# 	def __init__(self,pages):
# 		self.pages=pages
# 	def __add__(self,other):
# 		return other.pages+self.pages
	


# b2=BookY(150)
# b1=BookX(100)
# print("Total pages",b2+b1)

class Ramayan:
	def __init__(self,pages):
		self.pages=pages
	def __gt__(self,other):
		return self.pages>other.pages

class Mahabharat:
	def __init__(self,pages):
		self.pages=pages

r=Ramayan(3000)
m=Mahabharat(300)
if(r>m):
	print("ramayan has more pages",r.pages)
else:
	print("Mahabharat has more pages")

