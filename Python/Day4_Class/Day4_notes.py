#Day 4 notes
#Boolean:
#True or False

#Numeric values 0, 0.9 and empty string and None are treated as False; all other are True

def loop1(n):
	if n <= 0:
		print("done")
	else:
		n = n + 1
		print(n)
		loop1()
loop1(1)	
