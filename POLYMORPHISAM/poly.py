# Duck typing philosophy of Python
# Operator overloading
# Method overloading
# Method overriding
class Dog:
	def talk(self):
		print("bark bark")
class Duck:
	def talk(self):
		print('Quack,quack')
class Human:
	def talk(self):
		print('hello hi')


def call_talk(obj):
	obj.talk()

x=Human()
call_talk(x)
x=Duck()
call_talk(x)
x=Dog()
call_talk(x)
