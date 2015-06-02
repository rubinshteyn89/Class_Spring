__author__ = 'ilya_rubinshteyn'




def user_promp():

    if n > 2:
        check_fermat()
    else:
        print("n must be greater than 2")

def check_fermat():

    formula = (a**n)+(b**n)==(c**n)
    if formula == False:
        print("No, that doesn’t work")
    else:
        print("Holy smokes, Fermat was wrong!")


if __name__ == '__main__':
    a =eval(input("a = "))
    b =eval(input("b = "))
    c =eval(input("c = "))
    n = eval(input("n = "))
    user_promp()
    check_fermat()