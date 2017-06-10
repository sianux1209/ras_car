

def readFlag():
	# readline.py
	f = open("./actionFlag", 'r')
	lines = f.read().splitlines()

	mode = lines[0]
	action = lines[1]
	flag = lines[2]

	return mode, action, flag


	f.close()

mode, action, flag = readFlag()

print mode
print action
print flag