__author__ = 'ilya_rubinshteyn'

from math import exp
def is_Power():
    a = eval(input("first number: "))
    b = eval(input("second number: "))
    if a % b == 0  and (a/b)%b == 0:

        print("true")
        return True

    else:
        print("false")
        return False

is_Power()