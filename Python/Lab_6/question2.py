__author__ = 'ilya_rubinshteyn'


def question2():
    n = 1
    while n != 0:
        n = eval(input("What range of numbers would you like to add? "))

        if n < 0 or type(n) == float:
            print("Invalid input")
            continue
        elif n > 0:
            sum_of_n = n*(n+1)/2
            print("The sum of the number range you selected is ",sum_of_n)
            continue
        elif n == 0:
            break

if __name__ == '__main__':
    question2()