__author__ = 'ilya_rubinshteyn'

# Notes:
# \n = new line

# \t = tab

# \\ = single backslash

# \" = double quote

# \' = single quote

# ''' = triple quote used to print multi-line strings

# len() = length of string or variable (also includes spaces into count)

# .isdigit() = returns True if all characters in the string are digits

# .isalpha() = returns True if all characters in the string are letters

# .find() = returns index of argument

# print("Hello World"[0]) = will print 'H' or first position of string.

# string[x:y] = will return characters from position x through y in the string.

# .count(x) = counts how many times argument x repeats in the string or variable.

# .split('') = splits string into substrings by argument( spaces or characters)-- Example:
# ("hello world").split(" ")
#output: ['hello', 'world']

# .replace(x,y) = replaces x with y
# print("+") = will print + 80 times in same line

#lists: mutable or change-able

# list1 = [1, 'two', 3.1, '2.e']
# <class 'list'>
# [1, 'two', 3.1, '2.e']

#list1[len(list1)-2]
# 1

#list1[0]=2
#[2, 'two', 3.1, '2.e']

#tuples: immutable or not change-able
#tuple1 = (1, 'two', 3.1, '2.e')
#<class 'tuple'>
#(1, 'two', 3.1, '2.e')



def something():
    a = True

    while a:
        letter = input("enter a letter: ")
        if letter > "cat":
            print(letter+" is larger")
        else:
            print(letter+" is less")

if __name__ == '__main__':
    something()



