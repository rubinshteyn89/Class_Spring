__author__ = 'ilya_rubinshteyn'

def type_convert():

    while True:

        usr_in = input("What would you like to know the type of? ")
        original_input = type(usr_in)
        conversion_method = eval(usr_in)
        final_result = type(conversion_method)
        output_string = "Before conversion, your input({}) was {}, after conversion, your input is {}"
        output_text =  output_string.format(usr_in,original_input,final_result)
        print(output_text)

if __name__ == '__main__':
    try:
        type_convert()
    except (KeyboardInterrupt):
        print("quit via stop or keyboard")
    except (NameError):
        print("NameError")