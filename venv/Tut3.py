#Welcome to Python Tutorial 3!

#import math functions
from math import*

#Building a basic calculator

usrVal1 = input("Enter first integer  : ")
usrVal2 = input("Enter second integer : ")

#Inputs from users are always strings, must convert them to integers or floats for math operations
result = round(float(usrVal1)) + round(float(usrVal2))

print("sum of " + str(usrVal1) + " + " + str(usrVal2) + " = " , int(result))

#End of Python Tutorial 3

