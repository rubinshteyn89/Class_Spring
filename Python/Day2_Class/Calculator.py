__author__ = 'ilya_rubinshteyn'
#Note: Only works with Python 3.X

def Calculator():
    turnedOn = True
    while turnedOn:
        print("")
        print("Enter a valid math equation or type any Text string to Exit:")
        print("")



        try:

            Operation = float(eval(input("Input: ")))
            print("Ouput: ",Operation)
        except(ValueError,SyntaxError,TypeError) :
            print("Ouput: Invalid operation, try again.")
        except(NameError):
            print("Exiting Calculator...")
            turnedOn = False

Calculator()
