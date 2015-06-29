__author__ = 'ilya_rubinshteyn'
# def last_element(p):
#     return p[len(p)-1]
#
# # main function
# def main():
#     last = last_element(user_entry)
#     print(last)
#
# user_entry = ('I', 'love', 'Python')
# main()

# a = '1'
# b = '2'
# c = '3'
# d = 4   # 4 without single quotes
# s = ''   # empty string
# for k in [a, b, c, d]:
#     if isinstance(k, str):
#         s = s + k
#     elif isinstance(k, int):
#         k = str(k)
#         s = s + k
# print(s)

income = int(input("Please type your income: "))
taxRate = 0
if 20000 < income < 30000:
   taxRate = .15
elif 30000 <= income < 45000:
   taxRate = .20
elif 45000 <= income <75000:
   taxRate = .30
else:
   taxRate = .40
print("Your income tax rate is: ", taxRate)

