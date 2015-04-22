
turnedOn = True

def Addition():

        a=float(input("Input: "))
        b=float(input("Input: "))
        equals = a + b
        #opertation = print(a,'+',b)

        for i in range(1):
                print("Opertation: ",a,'+',b)
                print("Output",equals)

def Subtraction():

        a=float(input("Input: "))
        b=float(input("Input: "))
        equals = a - b

        for i in range(1):
                print("Opertation: ",a,'-',b)
                print("Output",equals)

def Muliplication():

        a=float(input("Input: "))
        b=float(input("Input: "))
        equals = a * b

        for i in range(1):
                print("Opertation: ",a,'*',b)
                print("Output",equals)

def Division():

        a=float(input("Input: "))
        b=float(input("Input: "))
        equals = a / b

        for i in range(1):
                print("Opertation: ",a,'/',b)
                print("Output",equals)



while turnedOn:
    print("Welcome to Simple Calculator!"
          "")

    print("1 = addition")
    print("2 = subtraction")
    print("3 = multiplication")
    print("4 = subtraction")
    print("5 = quit")

    prompt = int(input("What would you like to do? "))

    if prompt == 1:
        Addition()
        print("")

    elif prompt == 2:
        Subtraction()
        print("")

    elif prompt == 3:
        Muliplication()
        print("")

    elif prompt == 4:
        Division()
        print("")

    elif prompt == 5:
        print("Exiting Calculator...")
        turnedOn = False




