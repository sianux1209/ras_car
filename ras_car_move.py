import RPi.GPIO as gpio
import time

class Ras_car_move:

	def __init__(self):
		self.setup()

	def __del__(self):
		gpio.cleanup()

	def stop(self):
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)

	def setup(self):
		gpio.setmode(gpio.BOARD)
		gpio.setup(7, gpio.OUT)
		gpio.setup(11, gpio.OUT)
		gpio.setup(13, gpio.OUT)
		gpio.setup(15, gpio.OUT)
		gpio.setup(16, gpio.OUT)
		gpio.setup(18, gpio.OUT)
		gpio.output(7, True)
		gpio.output(11, True)

	def turn_right(self):
		gpio.output(13, False)
		gpio.output(15, True)
		gpio.output(16, True)
		gpio.output(18, False)

	def turn_left(self):
		gpio.output(13, True)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, True) 

	def forward(self):
		gpio.output(13, True)
		gpio.output(15, False)
		gpio.output(16, True)
		gpio.output(18, False)

	def backward(self):
		gpio.output(13, False)
		gpio.output(15, True)
		gpio.output(16, False)
		gpio.output(18, True)

if __name__ == "__main__":

	car = Ras_car_move()

	print 'turn left'
	car.turn_left()
	time.sleep(1)
	car.stop()

	print 'turn right'
	car.turn_right()
	time.sleep(1)
	car.stop()

	print 'forward'	
	car.forward()
	time.sleep(1)
	car.stop()

	print 'backward'
	car.backward()
	time.sleep(1)
	car.stop()