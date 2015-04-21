#For Python 3.x

def Chaos34():
        print ("This program illustrates a chaotic function")
        x = eval(input("Enter a number between 0 and 1: "))
        y = eval(input("Enter a second number between 0 and 1: "))
        for i in range(10):
                x = 3.9 * (x - x * x)
                y = 3.3 * (y - y * y)
                print (x,'\t',y)

Chaos34()
