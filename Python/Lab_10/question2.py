__author__ = 'ilya_rubinshteyn'

import sys
#globals


def Welcome():
    print("Welcome!")

def open_file():
    """Open a file."""

    try:
        the_file = open("trivia.txt", "r")
    except FileNotFoundError as e:
        print("Unable to open the file", the_file, "\nEnding program...",e)
        quit()
    else:
        print("returning file")
        return the_file

def read_line(the_file):
    next_line = the_file.readline()
    print("read next line")
    return next_line

def round1():
    print("starting round 1")



def check_answer():
    print("check answer")

def calculate_total_score():
    print("Score is ...")

if __name__ == '__main__':
    Welcome()
    open_file()
    round1()
    read_line()
    check_answer()
    calculate_total_score()