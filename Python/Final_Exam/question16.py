__author__ = 'ilya_rubinshteyn'



if __name__ == '__main__':
    file_name = input("\nPlease type a file name that you want to create: ")
    open_file = open(file_name,"w")
    written_file = open_file.write(input("\nPlease type something to be saved into this file: "))
    open_file.close()
    print("\nOK, the file",file_name, "has been saved.")
    read_file = open(file_name,"r")
    content = read_file.read()
    print("\nRead back what you have saved in the file",file_name,":",content)
    print("\nNow read back the second time from the file",file_name,":",content)
    print("\nBye!")
    read_file.close()
