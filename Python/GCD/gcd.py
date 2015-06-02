__author__ = 'ilya_rubinshteyn'
def my_gcd():

    a = eval(input("a = "))
    b = eval(input("b = "))

    while b:
        r = a%b
        (a,b) = (b,r)
        print("calculating...")
    return print(a)

if __name__ == '__main__':
    my_gcd()