__author__ = 'ilya_rubinshteyn'

import re

file = open('Lorem.txt')

stringToSearch = ''

for line in file:
    stringToSearch += line

#print(stringToSearch)

patternFinder2 = re.compile('Lorem',re.IGNORECASE)
findPattern2 = re.findall(patternFinder2,stringToSearch)

if(findPattern2):
    print(findPattern2.group())
else:
    print("nothing found")
