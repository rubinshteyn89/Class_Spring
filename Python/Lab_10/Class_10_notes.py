__author__ = 'ilya_rubinshteyn'

# fout = open("test_file1",'w')
# fout.write(input())
# fout.close()

# file handling:
# open("file_name", 'mode')
# mode can be 'w' 'r' 'a'
# variable.write(data)
# variable.read()
# variable.seek(0) -- seeks first character
a = 1

while a!= 0:

    a = 1
    try:
        a = eval(input("\nPlease enter an expression: "))
    except ValueError as e:
        print("That was not a valid expression!")
        print(e)
    except NameError as e:
        print("That was not a valid expression!")
        print(e)
    except ZeroDivisionError as e:
        print("That was not a valid expression!")
        print(e)
    except Exception as e:     # unspecified exception error
        print(e)
    else:
        print("Your expression is: ", a)
    finally:
        print("Thanks!")
print("Bye!")