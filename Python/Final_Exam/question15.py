__author__ = 'ilya_rubinshteyn'



while True:

    userInput = input ("Please type a real number: ")

    try:
        float(userInput)
        print("Thank you for following instructions.")
    except Exception:
        print("You typed a char that isn't appropriate in a real number.")
    finally:
        print("I hope you play again.")