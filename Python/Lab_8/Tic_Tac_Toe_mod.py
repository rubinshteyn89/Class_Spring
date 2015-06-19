__author__ = 'ilya_rubinshteyn'
# global constants

# def Mark_Choice():
#     user_choice = input("Which would you Like to be '\X' or '\O'? ")
#     if user_choice == X:
#         human = X
#         computer = O
#         return human == X
#     else:
#         human = O
#         computer = X


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


def trap(board):
    possible_traps = \
       ((0,7,6),
        (0,2,8),
        (2,7,8),
        (2,0,6))
    for row in possible_traps:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            trap = board[row[0]]
            return trap
    return None

def legal_moves(board):
    # collect all board EMPTY positions and put them into the positions list,
    # so a player (either human or computer) can only move to these places
    positions = []
    for i in range(NUM_SQUARES):
        if board[i] == EMPTY:
            positions.append(i)
    return positions


def human_move(board, human):
    # human move
    # get a list of all legal moves
    legal = legal_moves(board)
    # initialize it the return move to None
    move = None
    # if current legal list has nothing in it
    if legal == []:
        # No legal moves at all and just return None
        return move
    # now let us find a legal move
    # keep trying as long as the move is not in the legal list
    while move not in legal:
        # init user input
        user_input = "None"
        # make sure a user's input is a digit number
        while not user_input.isdigit():
            # take a user_input with the prompt " Please enter your move (0 - 8) "
            user_input = input("Please enter your move (0 - 8): ")
            if not user_input.isdigit():
                print("The move has to be a position number.")
            # print a msg "The move has to be a position number" if it is not digit
        # now we can convert it to an integer safely
        move = int(user_input)
        if move < 0 or move > 8:
            print("The position of your move has to be between 0 - 8")
        elif move not in legal:
            print("Sorry, that position has already been taken!")
    # now return the legal next move
    return move


def computer_move(board, computer, human):
    print("Computer move...")
    # make a copy of board as a working board
    board_copy = board
    # computer will take the best moves in this order
    best_moves = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    # generate a list of legal moves with the current board
    legal = legal_moves(board)
    # init move to None
    move = None
    # if no any possible legal moves
    if legal == []:
        # just return computer move as None
        return move
    # now loop all the possible moves in the legal list
    for move in legal:
        # test this move as a computer move
        board_copy[move] = computer
        # if this generates a computer win, return that move
        if winner(board_copy) == computer:
            return move
        # if not, undo the test
        board_copy[move] = EMPTY
    # then the computer will check if human can win from the current legal moves
    # the following code will be almost the same as the previous code for computer
    # loop again all the possible moves in the legal list
    for move in legal:
        # test this move as a human move
        board_copy[move] = human
        # if this generates a human win, return that move to block it
        if winner(board_copy) == human:
            return move
        # if not, undo the test
        board_copy[move] = EMPTY
    # if no one can win through previous tests, take the best from the BEST_MOVES
    for move in best_moves:
        if move in legal:
            return move
    return move


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
    # Mark_Choice()

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
    congrat_winner(the_winner, computer, human)
    # congrat_winner('Tie', 'X', 'O')
    # congrat_winner('X',  'X', 'O')
    # congrat_winner('O',  'X', 'O')
