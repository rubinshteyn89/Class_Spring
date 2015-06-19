__author__ = 'ilya_rubinshteyn'
def read_global():
      print("Inside read_global(), the value is:", value)

def shadow_global():
      value = -8
      print("Inside shadow_global(), the value is:", value)

def change_global():
      global value
      value = -6
      print("Inside change_global(), the value is:", value)


# main
# value is a global variable
value = 10
print("Inside main(), the value is:", value)
read_global()
print("Back inside main(), the value is still:", value)
shadow_global()
print("Back inside main(), the value is still:", value)
change_global()
print("Back inside main(), the value has now changed to:", value)


