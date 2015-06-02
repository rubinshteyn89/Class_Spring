__author__ = 'ilya_rubinshteyn'

def string_comparison():

    string_a = "\nThey'll hibernate during the winter."
    string_b = "\n\"Absolutely not,\" he said."
    string_c = "\n\"He said, 'Absolutely not,'\" recalled Mel."
    string_d = "\nhydrogen sulfide"
    string_e = "\nleft\\right"

    print(string_a)
    print("{}{}".format("The length of this string is ",len(string_a)))

    print(string_b)
    print("{}{}".format("The length of this string is ",len(string_b)))

    print(string_c)
    print("{}{}".format("The length of this string is ",len(string_c)))

    print(string_d)
    print("{}{}".format("The length of this string is ",len(string_d)))

    print(string_e)
    print("{}{}".format("The length of this string is ",len(string_e)))

if __name__ == '__main__':
    string_comparison()