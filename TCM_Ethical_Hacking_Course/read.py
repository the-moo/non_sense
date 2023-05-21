#!/bin/python3

months = open('months.txt', encoding="utf8") #encoding may need to be added ot function correctly

print(months) #gives file info
print(months.mode) #gives mode of file
print(months.readable()) #gives boolean answer (is this readable?)
print(months.read()) #whole file
months.seek(0) #resets to line in file
print(months.readline()) # line by line
print(months.readline())
months.seek(0) 
print(months.readlines()) #prints as list
months.seek(0) 
print(months.readlines()) 
months.seek(0) 
for month in months:
    print(month) # another way to print
months.seek(0) 
for month in months:
    print(month.strip()) #.strip removes excess lines


months.close

