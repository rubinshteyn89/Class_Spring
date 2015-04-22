def F2C():
	print("This program converts Fahrenheit to Celsius")
	F = eval(raw_input("Enter your Fahrenheit value here: "))
	for i in range(1):	
		C = (F-32.0)*5/9
		print (C,"Celsius")
F2C()
