from abs import Car
class Maruti(Car):
	def steering(self):
		print("Maruti uses manual streeing")
	def braking(self):
		print("maruti using hydrulic brakes")
		print("apply brakes ands stop it")

m = Maruti("yash")
m.opentank()
m.steering()
m.braking()