__author__ = 'ilya_rubinshteyn'

def formatting():

    specials_text = "Good {}! Today's special is {} and the price is ${}."

    time = "afternoon"

    food = "Spam with eggs"

    price =  3.95

    output_text = specials_text.format(time, food, price)

    print(output_text)
#use these:
    print("Good %s! Today's special is %s and the price is $%g." % (time, food, price))

#no these:
    print("Good {}! Today's special is {} and the price is ${}.".format(time, food, price))
    print("Good ",  time, "! Today's special is ", food, " and the price is $",  price, ".", sep="")



#notes
#sep= " "  is way of adding spaces


def example2():
    x = int(input("Enter an integer: "))

    y = int(input("Enter another integer: "))

    output_str = "{0} + {1} = {2}; {0} * {1} = {3}."   # {number} indicates position of argument

    output = output_str.format(x, y, x+y, x*y)

    print(output)


example2()