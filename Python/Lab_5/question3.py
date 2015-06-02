__author__ = 'ilya_rubinshteyn'
rate = 2.5

def invest(rate):
    money = 100
    years = 0

    rate = rate +1
    while money< 200:

        money = money * rate
        years = years + 1
    return print(float(years))


if __name__ == '__main__':
    invest(rate)