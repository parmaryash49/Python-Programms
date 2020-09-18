from abc import *
class Myclass(ABC):
	@abstractmethod
	def connect(self):
		pass
	@abstractmethod
	def disconnect(self):
		pass

class Oracle(Myclass):
	def connect(self):
		print("connecting the Oracle database")
	def disconnect(self):
		print("disconnect the  from Oracle")

class Sys(Myclass):
	def connect(self):
		print("connecting the sys database")
	def disconnect(self):
		print("disconnect the  from sys")

# s=Sys()
# s.connect()

# class Database:
# 	str=input("enter database name:")
# 	classname=globals()[str]
# 	x=classname()
# 	x.connect()
# 	x.disconnect()
classname=globals()["Sys"]
x=classname()
x.connect()
x.disconnect()