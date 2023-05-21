#!/bin/python3

name = input("Enter your name: ")
drink =input("What's your favorite drink?: ")
print ("Hello "+name+"! Why don't you have some "+drink+".")

x = float(input("Lets do some math.  Give me a number: "))
o = input("Give me an operator: ")
y = float(input("Give me yet another number: "))

if o=="+":
    print (x + y)
elif o == "-":
    print (x-y)
elif o== "/":
    print (x/y)
elif o == "*" or o=="x":
    print (x*y)
elif o == "**" or o== "^":
    print (x**y)
else:
    print("Unknown operator.")
