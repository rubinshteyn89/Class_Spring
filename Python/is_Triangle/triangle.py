__author__ = 'ilya_rubinshteyn'

from math import sqrt
def is_Triangle(a,b,c):

        if a > b + c or b > a + c or c > a + b:
            return False,print("False")
        else:
            return True,print("True")

def stick_input():
    a = int(input("Stick A = "))
    b = int(input("Stick B = "))
    c = int(input("Stick C = "))
    if is_Triangle(a,b,c):

        try:
            s = ( a + b + c ) / 2
            A = print("Area of triangle with sides 'a','b','c' =",sqrt( s * (s - a) * (s - b) * (s - c) ))
            return A

        except ValueError:
             print("Invalid input")



if __name__ == '__main__':
    stick_input()
