__author__ = 'ilya_rubinshteyn'

#qustion #2
def sum_all():
    n = eval(input("What range of numbers would you like to add? "))
    x = 0

    while True:
        x = x + 1
        print(x)
        formula = n*(n+1)/2
        if x == n:
            print("The sum of the number range you selected is ",formula)
            break
        else:
            continue


def sum_odd():
    n = eval(input("What number would you like to start with? "))
    s = eval(input("What number would you like to end with? "))
    x = 0
    while True:
        x = x + 1
        sum = 0
        for i in range(n,s,2):
            print(i)
            sum += i
        if x == n:
            print("The sum of the number range you selected is ",sum)
            break
        else:
            continue


def sum_input():
    total = 0

    while True:
        n = eval(input("How much would you like to add to that? "))

        if n == 999:
            print("Breaking loop.")
            break

        elif n != 999:
            total = total + n
            print("Total is now ",total)
            continue

if __name__ == '__main__':
    sum_all()
    sum_odd()
    sum_input()