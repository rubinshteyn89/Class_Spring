__author__ = 'ilya_rubinshteyn'

def C2F():
        print("This program converts Celsius to Fahrenheit")
        C = eval(input("Enter your Celsius value here: "))
        for i in range(1):
                F = C*(9.0/5)+32
                return print (C,"Celsius is equal to ",F,"Fahrenheit"), print("")

def F2C():
        print("This program converts Fahrenheit to Celsius")
        F = eval(input("Enter your Fahrenheit value here: "))
        for i in range(1):
                C = (F-32.0)*5/9

                return print (F,"Fahrenheit is equal to ",C,"Celsius"), print("")

def main():
    On = True
    while On:
        print("Options:")
        print("1 = Celsius -> Fahrenheit")
        print("2 = Fahrentheit -> Celsius")
        print("3 = Quit")
        prompt = eval(input("Which conversion would you like to do?"))
        if prompt == 1:
            for i in range(10):
                C2F()
        elif prompt == 2:
            for i in range(10):
                F2C()
        elif prompt == 3:
            print("Exiting program...")
            On = False

main()
