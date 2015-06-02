__author__ = 'ilya_rubinshteyn'

import datetime
t_hour = datetime.datetime.now().time().hour
#print(t_hour)
def time_greet():
    if t_hour >= 0 and t_hour < 12:
        tod = "Morning"
    elif t_hour >= 12 and t_hour < 18:
        tod = "Afternoon"
    elif t_hour >= 18 and t_hour < 21:
        tod = "Afternoon"
    elif t_hour >= 21 and t_hour < 24:
        tod = "Afternoon"

    username = input("Username: ")
    greeting = "Good {}, {}"

    print(greeting.format(tod,username))

if __name__ == '__main__':
    time_greet()