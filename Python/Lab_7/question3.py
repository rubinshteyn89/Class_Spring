__author__ = 'ilya_rubinshteyn'
import os
import random
import sys
def Rando():

    Y = (int(random.random()*100))
    return Y

def guess():

    y = Rando()

    print("The computer generated a random number between 0 to 100.")
    print("For testing purposes,",y," is the random number")
    tries = 0
    turned_on = True
    while turned_on:
        print("")
        x = input("Please enter your guess: ")
        tries = tries +  1
        digit_check = x.isdigit()

        if digit_check:
            x = int(x)
            if x != y:
                print("Wrong!")
                print("")
                if x > y:
                    print(x," is greater than the random number, try again.")
                    print("")
                else:
                    print(x," is smaller than the random number, try again.")
                    print("")

            elif x == y:
                print("You are correct!")
                print("\nIt took you ",tries," tries to guess ",y)
                break

        else:
            print("\nPlease enter a valid digit.")

def new_game():

    while True:
        print("\nIf you would like to start a new game, type \'y' or \'Y'. Type \'n' or \'N' to quit.")
        answer = input(">>> ")
        ans_len = len(answer)

        if answer == 'y' or answer == 'Y':
            print("\nStarting new game...\n")
            guess()

        elif answer == 'n' or answer == 'N':
            print("Quitting application...")
            quit()

        elif answer.isalpha() == False or ans_len != 1:
            print("Invalid answer. Please Try again.")

        else:
            print("Invalid answer. Please Try again.")

if __name__ == '__main__':

    if sys.platform == 'darwin' or sys.platform == 'linux2':
        os.system('clear')
        print('')

    try:
        while True:
            guess()
            new_game()
    except(KeyboardInterrupt):
        print("\nQuit via keyboard interrupt.\n")



