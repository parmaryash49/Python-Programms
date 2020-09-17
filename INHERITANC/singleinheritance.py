class Bank(object):
	cash=1000
	@classmethod
	def availabe_cash(cls):
		print(cls.cash)

class Andhra(Bank):
	cash=800
	@classmethod
	def availabe_cash(cls):
		print(cls.cash)

class State(Bank):
	cash=500
	@classmethod
	def availabe_cash(cls):
		print(cls.cash+Bank.cash)

a=Andhra()
a.availabe_cash()

s=State()
s.availabe_cash()

b=Bank()
b.availabe_cash()