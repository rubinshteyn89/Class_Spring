__author__ = 'ilya_rubinshteyn'

def Calculator():
    turnedOn = True
    while turnedOn:
        print("")
        print("Enter a valid equation or type any Alpha Character string to Exit:")
        print("")

        try:
            Operation = float(eval(input("Input: ")))
            print("Output: ",Operation)

        except(ValueError,SyntaxError) :
            print("Output: Invalid operation, try again.")

        except(NameError,TypeError):
            print("Exiting Calculator...")
            turnedOn = False

Calculator()
