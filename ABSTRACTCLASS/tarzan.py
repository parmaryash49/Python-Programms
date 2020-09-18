from abs import Car
class Tarzan(Car):
	def steering(self):
		print("tarza use power steering")

	def braking(self):
		print("apply brakes now...")


t=Tarzan(5678)
t.opentank()
t.steering()
t.braking()