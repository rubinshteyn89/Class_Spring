#For Python 2.x

def Chaos26():
	print "This program illustrates a chaotic function"
	x = input("Enter a number between 0 and 1: ")
	y = input("Enter a second number between 0 and 1: ")
	for i in range(10):
		x = 3.9 * x * (1 - x)
		y = 3.3 * y * (1 - y)
		print x, '\t',  y
Chaos26()
