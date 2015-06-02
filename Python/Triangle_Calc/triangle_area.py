__author__ = 'ilya_rubinshteyn'

from math import sqrt
def triangle_area():


        try:
            a = eval(input("Side a = "))
            b = eval(input("Side b = "))
            c = eval(input("Side c = "))
            s = ( a + b + c ) / 2
            A = print("Area of triangle with sides 'a','b','c' =",sqrt( s * (s - a) * (s - b) * (s - c) ))
            return A

        except ValueError:

            print("Invalid input: make sure: a + b > c")

triangle_area()

