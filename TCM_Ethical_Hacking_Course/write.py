#!/bin/python3

days = open('days.txt', "a") # "w" places into write mode, "a" for append.  "w" will over right existing file.  "a" will add to it

print(days.mode)
days.write("Monday") #adds to file
days.write("\nTuesday")


days.close()
