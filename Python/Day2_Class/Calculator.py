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
            print("Output: ",Operation)
        except(ValueError,SyntaxError) :
            print("Output: Invalid operation, try again.")
        except(NameError,TypeError):
            print("Exiting Calculator...")
            turnedOn = False

Calculator()
