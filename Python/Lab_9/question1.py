__author__ = 'ilya_rubinshteyn'
# global constants

X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


def display_instruct():
    # display instructions for the Tic-Tac-Toe game
    print("\t\tTic-Tac-Toe")
    print("\n\t ",0,"  |  ",1,"  |  ",2," ")
    print("\t------+-------+-------")
    print("\t ",3,"  |  ",4,"  |  ",5," ")
    print("\t------+-------+-------")
    print("\t ",6,"  |  ",7,"  |  ",8," ")
    print("\nHow to play:")
    print("1. Each number on the board represents a possible position that a player can use to make their move.")
    print("2. When it is your turn, please enter a digit \'0 - 8' to make your move to that position.")
    print("3. To win, get 3 marks in a straight vertical, horizontal or diagonal line!")


def ask_yes_no(question):
    # take user input, return True if 'Y' or 'y', otherwise False
    while True:
        question = input("\nWould you like to go first? (Y/N) \n")
        if question.isalpha():
            answer = str(question)
            if answer == 'Y' or answer == 'y':
                print("You chose to go first.")
                answer = True
                return answer
            elif answer == 'N' or answer == 'n':
                print("You chose to go second.")
                answer = False
                return answer
            else:
                print("Invalid input. Try again.")
        else:
            print("Invalid input. Try again.")


def new_board():
    # create a new board here...
    print("\nCurrent Board:")
    board = [EMPTY, EMPTY, EMPTY,
             EMPTY, EMPTY, EMPTY,
             EMPTY, EMPTY, EMPTY]
    return board


def display_board(board):
    print("display the current board")
    print("\n\t ",board[0],"  |  ",board[1],"  |  ",board[2]," ")
    print("\t------+-------+-------")
    print("\t ",board[3],"  |  ",board[4],"  |  ",board[5]," ")
    print("\t------+-------+-------")
    print("\t ",board[6],"  |  ",board[7],"  |  ",board[8]," ")


def winner(board):
    # check if there is a winner or it is a tie
    ways_to_win = \
               ((0, 1, 2),
                (3, 4, 5),
                (6, 7, 8),
                (0, 3, 6),
                (1, 4, 7),
                (2, 5, 8),
                (0, 4, 8),
                (2, 4, 6))
    for row in ways_to_win:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None


def human_move(board, human):
    # human move
    m = eval(input("\nPlease enter a human move...\n"))
    # ...
    return m

def computer_move(board, computer, human):
    # computer move
    # ...
    print("\nComputer move...")
    return 1

def next_turn(turn):
    # change the turn to next player
    if turn == X:
        turn = O
    else:
        turn = X
    print("\nSwapped the player!")
    return turn


def congrat_winner(the_winner, computer, human):
    # congratulate the winner or declare a tie
    if the_winner == human:
        print("You win! Congrats!")
    elif the_winner == computer:
        print("You lose! Computer is the winner!")
    else:
        print("It's a tie! Try again!")


if __name__ == '__main__':
    # variables
    human = X
    computer = O
    turn = human
    the_winner = TIE

    # display the game instructions
    display_instruct()

    # determine who goes first
    if ask_yes_no("Would human like to go first? (Y/N) ")==True:
        turn = human
    else:
        turn = computer

    # create an empty tic-tac-toe board
    board = new_board()
    # display the board
    display_board(board)

    # while nobody's won and it's not a tie
    while not winner(board):
        # if it's the human's turn
        if turn == human:
            # get the human's move
            move = human_move(board, human)
            # update the board with the move
            board[move] = human
        # otherwise
        else:
            # calculate the computer's move
            move = computer_move(board, computer, human)
            # update the board with the move
            board[move] = computer
        # display the board
        display_board(board)
        # switch the turn
        turn = next_turn(turn)

    # congratulate the winner or declare a tie
    the_winner = winner(board)
    #congrat_winner(the_winner, computer, human)
    congrat_winner('Tie', 'X', 'O')
    congrat_winner('X',  'X', 'O')
    congrat_winner('O',  'X', 'O')
