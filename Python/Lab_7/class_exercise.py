__author__ = 'ilya_rubinshteyn'


# for i in (1,2,3,4,5):
#     print(i)

def common(a,b):
    for i in a:
        if i in b:
            print(i)
common("oranges","apples")