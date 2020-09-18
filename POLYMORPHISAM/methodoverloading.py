class Myclass:
	def sum(self,a=None,b=None,c=None,*d):
		if(a!=None and b!=None and c!=None):
			print("sum of three numbers",a+b+c)
		elif (a!=None and b!=None):
			print("sum of two numbers",a+b)
		else:
			print("pls enter two or three arguments")
m=Myclass()
m.sum(10,20,30)
m.sum(10,20)
m.sum(1)