__author__ = 'ilya_rubinshteyn'


def q15():

    turnedOn = True
    while turnedOn:
        user_input = eval(input("Please enter a positive integer to show all its factors (enter 0 to quit):"))

        if user_input < 0:
            print("Your input is invalid")

        elif user_input == 0:
            print("Well done and goodbye!")
            turnedOn = False

        elif type(user_input) != int:
            print("Your input is invalid")
            continue

        for i in range(1,user_input+1):

            if user_input%i == 0:
                    print(i)

if __name__ == '__main__':
    q15()
