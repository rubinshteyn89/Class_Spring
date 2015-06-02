__author__ = 'ilya_rubinshteyn'
import random
def Rando():

    Y = (int(random.random()*100))
    return Y

def guess():

    y = Rando()
    print("The computer generated a random number between 0 to 100.")
    #print("for testing purposes:",y," is the random number")
    tries = 0
    while True:
        print("")
        x = eval(input("Please enter your guess: "))
        tries += 1

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
            print("")
            print("It took you ",tries," tries to guess ",y)
            quit()


if __name__ == '__main__':
    guess()



