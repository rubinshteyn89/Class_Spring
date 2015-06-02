__author__ = 'ilya_rubinshteyn'
import math
def sqr_root():
    x = eval(input("Square root of "))
    n = eval(input("How many times would you like to calculate? "))

    actual = math.sqrt(x)
    guess = x/2
    new_guess = (guess+x/guess)/2

    for i in range(n):
            guess = new_guess
            new_guess = (guess+x/guess)/2
            print("Guess is ",new_guess," vs ","Actual is ",actual)
    print("Difference of final guess and actual is",actual-new_guess)
sqr_root()

