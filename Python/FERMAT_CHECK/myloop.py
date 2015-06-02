__author__ = 'ilya_rubinshteyn'
# def myloop():
#     b = int(input())
#     for i in range(100):
#         b = b-1
#         print(b)
#
# myloop()
#
# x = "test1"
# if x:
#     print("true")
# else:
#     print("false")

import time
def ilyas_drinking():
    drinks = int(input("How many drinks do you think Ilya will have?"))
    if drinks:
        while True:
            drinks = drinks+1
            print("At the current rate based on time, this is how many drink he will actually have:",drinks)
            time.sleep(2)
    else:
        print("Ilya quit drinking.")
ilyas_drinking()
