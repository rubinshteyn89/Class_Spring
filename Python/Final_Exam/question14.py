__author__ = 'ilya_rubinshteyn'

def factorial_function(x):

    while x == 0:
        return 1
    else:
        return x * factorial_function(x-1)

if __name__ == '__main__':
    factorial_function(5)

