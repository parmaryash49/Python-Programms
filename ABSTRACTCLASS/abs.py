from abc import *
class Car(ABC):
	def __init__(self,regno):
		self.regno=regno
	def opentank(self):
		print("Fill the fuel tunk")
		print("for the car ",self.regno)

	@abstractmethod
	def steering(self):
		pass

	@abstractmethod
	def braking(self):
		pass