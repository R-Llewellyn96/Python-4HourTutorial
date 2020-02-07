#Welcome to the 4 hour Python Tutorial 1!

#Comments are created using the hash key

#Printing a statement is really simple
print("Hello World")

#Variables dont need to be declared before being used
sentence = "This is my message"
print(sentence)

#Want to print a the result of a math equation? Simple as
print(42 * 4)

#What about combining statements?
print("My message is: ", sentence, "\nThe result of 42 x 4 is: ", 42 * 4)

#Drawing a shape in Python
print("\nTriangle: \n")
print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")

#Variables and data types in Python
name = "Ryan Llewellyn"
print("My name is: " + name)

#Functions
print(name.lower())
print(name.upper())

#Check if a value is all uppercase
print(name.isupper())

#Combination of string functions
print(name.upper().isupper())

#length of string
print("Length of name is: " ,len(name))

#get individual characters in a string
print("First character of name is: ",name[0])

#Find the index of a character in a string
print("L is the: ",name.index("L"), "th Letter of my name")

#Concatenate a string
name = name + " BSc"

#replace a value in a string
print("My title is: ",name.replace("Ryan", "Mr"))


#Dealing with data types

#Modulus operator, gives remainder after division
print(10 % 3)

#Storing numbers in variables
myNum1 = 3
myNum2 = -12

#convert number to a string
print(str(myNum1) + " is my favourite number")

#Absolute value
print(abs(myNum2))

#power value, calculate a value to the power of
print("3 squared = ", pow(3,2))

#Max function, returns larger of 2 values passed to it
print(max(5,2))

#Min function, returns the smaller of 2 values passed to it
print(min(5,2))

#Round function, rounds a float number to nearest full integer
print(round(3.7))

#importing external code to file, in this case math
from math import *

#Now we can access more math functions!

#Floor function, take floating point value to lowest integer
print(floor(3.7))

#Ceil function, take floating point value to highest integer
print(ceil(3.7))

#Square root function, find square root of passed value
print(sqrt(36))

#End of Python Tutorial 1




