#!/usr/bin/python3
""" 
Identifes as python file
"""

# Print String
print("Hello World")
print('Hello World')
print("""This string runs
multiple lines!""") #triple quote for multiple lines
print("This string "+"is awesome!!!") #We can also concatenate
print('\n') # new line
print ('Test that new line out')
print('\n')

#MATH
print(50+50) #add
print(50-50) #subtract
print(50*50) #multiply
print(50/50) #divide
print(50+50-50*50/50) #PEDMAS - order of operations
print(50**2) #exponets
print(50%6) #modulo - takes only what is left over
print(50/6) #division with remainder (or a float)
print(50//6) #no remainder
print('\n')

#VARIABLES AND METHODS
QUOTE="All is fair in love and war."
print(QUOTE)
print(QUOTE.upper()) #uppercase
print(QUOTE.lower()) #lowercase
print(QUOTE.title()) #title case
print(len(QUOTE)) #counts characters (spaces included)
print('\n')

NAME= "Moo" #string
AGE= 147 #integer
GPA= 0.1 #float - has decemial

print(int(AGE))
print(int(30.1))
print(int(30.9)) #Will not round
print("My name is "+ NAME +" and I am " + str(AGE) +" years old.")

AGE +=1 #adds 1 to age variable
print(AGE)

BIRTHDAY = 1
AGE += BIRTHDAY #adding variables together
print(AGE)
print('\n')

#FUNCTIONS
def who_am_i():
    """
    A simple function with out parameters
    """
    name = "Moo" #local variable
    age = 10000
    print ("My name is "+ name +" and I am " + str(age) +" years old.")

who_am_i()

def add_one (num):
    """
    one parameter function
    """
    print (num+100)

add_one(100)

def add(x,y):
    """
    function with multiple parameters
    """
    print(x+y)

add(7,7)

def multi(x,y):
    """
    shows how "return" command works
    """
    return x*y #stores for later

multi(7,7)
print(multi(7,7))

def square_root(x):
    """
    How to do square roots
    """
    print(x**.5)

square_root(64)

def nl(): #new line
    """
    function for creating new lines
    """
    print("\n")

nl()

#BOOLEAN EXPRESSIONS (True/False)
bool1 = True
bool2 = 3*3 == 9 #is equal too
bool3 = False
bool4 = 3*3 != 9 #is NOT equal

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True" #"" make it a string
print (type(bool5))
nl()

#RELATIONAL AND BOOLEAN OPERATORS
#Google Python Truth Table for table
greater_than = 7>5
less_than = 5>7
greter_than_equal_to = 7>=7
less_than_equal_to = 7<=7

test_and = (7>5) and (5<7) #True
test_and2 = (7>5) and (5>7) #False - all conditions must be True
test_or = (7>5) and (5<7) #True
test_or2 = (7>5) and (5>7) #also True - either condition can be True

test_not = not True #False
