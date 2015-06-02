#__author__ = 'ilya_rubinshteyn'
import sys
import re

file = open('Lorem.txt')

strToSearch = ""

for line in file:
    strToSearch += line

#print(strToSearch)

patFinder1 = re.compile('Lorem')

findPat1 = re.search(patFinder1, strToSearch)

print(findPat1.group())
print(findPat1.start())
print(findPat1.end())
print(findPat1.span())

findPat1 = re.findall(patFinder1,strToSearch)

for i in findPat1:
    print(i)


splitFound = patFinder1.split(strToSearch)
print(splitFound)

subFound = patFinder1.sub('Ilya',strToSearch)
print(subFound)