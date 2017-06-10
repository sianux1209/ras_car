import Tkinter as tk
import os

def forward(event):
	print "forward"
	os.system('python ras_car_move forward')

def backward(event):
	print "backward"
	os.system('python ras_car_move backward')

def left(event):
	print "left"
	os.system('python ras_car_move left')

def right(event):
	print "right"
	os.system('python ras_car_move right')

def release(event):
	print "release"
	os.system('python ras_car_move release')

root = tk.Tk()
print( "Press a key (Escape key to exit):" )
root.bind('<Up>', forward)
root.bind('<Down>', backward)
root.bind('<Left>', left)
root.bind('<Right>', right)
root.bind("<KeyRelease>", release)

# don't show the tk window
root.withdraw()
root.mainloop()