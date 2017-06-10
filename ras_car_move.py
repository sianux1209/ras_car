import RPi.GPIO as gpio
import time
import sys

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

	def testMove(self):
		print 'turn left'
		self.turn_left()
		time.sleep(1)
		self.stop()

		print 'turn right'
		self.turn_right()
		time.sleep(1)
		self.stop()

		print 'forward'	
		self.forward()
		time.sleep(1)
		self.stop()

		print 'backward'
		self.backward()
		time.sleep(1)
		self.stop()


def action(command):

	if command == "forward":
		car.forward()

	elif command == "right":
		car.turn_right()
		
	elif command == "backward":
		car.backward()

	elif command == "left":
		car.turn_left()

	elif command == "stop":
		car.stop()

def readState():
	# readline.py
	f = open("./actionFlag", 'r')
	lines = f.read().splitlines()

	mode = lines[0]
	action = lines[1]
	flag = lines[2]

	return mode, action, flag


	f.close()



if __name__ == "__main__":

	car = Ras_car_move()
	command = sys.argv[1]

	while True:
		mode, command, flag = readState()

		if(bool(flag) == True && mode == 'manual'):
			action(command)

		time.sleep(0.1)