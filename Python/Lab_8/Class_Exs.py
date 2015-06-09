__author__ = 'ilya_rubinshteyn'

# Pseudocode
#
# display the game instructions
#
# determine who goes first
#
# create an empty tic-tac-toe board
#
# display the board
#
# while nobody's won and it's not a tie
#
#          if it's the human's turn
#
#                  get the human's move
#
#                  update the board with the move
#
#          otherwise
#
#                  calculate the computer's move
#
#                  update the board with the move
#
#           display the board
#
#           switch the turn
#
# congratulate the winner or declare a tie


###GLOBALS###
X = 'X'
O = 'O'
EMPTY = ' '
NUM_SQUARES = 9


def welcome():
    print("Welcome to Tic-Tac-Toe!")
    print("This is the GRID:")

def grid():
    print("\n ",0,"  |  ",1,"  |  ",2," ")
    print("------+-------+-------")
    print(" ",3,"  |  ",4,"  |  ",5," ")
    print("------+-------+-------")
    print(" ",6,"  |  ",7,"  |  ",8," ")

def instructions():
    print("\nThe digits \'0 - 9' are grid positions.")
    print("\'X' or \'O' can be placed into any of the GRID positions if they are empty.")

def new_game_choice():
    print("\nPlease type \'1' to be Player One, or \'2' to be Player Two.")
    while True:
        player = input("Input: ")
        if player.isdigit():
            player = int(player)
            if player == 1:
                print("You chose to be Player One.")
                return player
            elif player == 2:
                print("You chose to Player Two.")
                return player
            else:
                print("Invalid input. Try again.")
        else:
            print("Invalid input. Try again.")
def winning_logic():
    print()

def next_turn(turn):
    print("Change turn...")
    if turn == X:
        turn = 0
    else:
        turn = X
    return turn

def grid_dictionary():
    empty_grid = { 0:EMPTY, 1:EMPTY, 2:EMPTY,
                   3:EMPTY, 4:EMPTY, 5:EMPTY,
                   6:EMPTY, 7:EMPTY, 8:EMPTY}
    move = int(input("\nWhich position? "))
    print(empty_grid[move])


if __name__ == '__main__':

    welcome()
    grid()
    instructions()
    new_game_choice()
    grid_dictionary()

