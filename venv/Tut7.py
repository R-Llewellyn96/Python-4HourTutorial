# Welcome to Python Tutorial 7!

# Python Functions

# Standard definition of a function, : is used for indentation and shows the entry point of a function
def sayHi(arg1, arg2):

    print(arg1, arg2)

# Standard method for calling a function
sayHi("Hello There!", "Ryan")

# Return statements

# Function to calculate the cube of a number
def calculateCube(arg1):

    return arg1 * arg1 * arg1

cubedVal = calculateCube(3)

print(cubedVal)

# If statements if python

def ifStatementsFunc():

    is_male = False
    is_tall = True

# Standard structure of an if statement in python
    if is_male and is_tall:
        print("You are male and tall")
    elif is_male and not(is_tall):
        print("You are male but not tall")
    elif is_tall and not(is_male):
        print("You are not male but you are tall")
    else:
        print("You are not male and you are not tall")

# Call function
ifStatementsFunc()

# If statements and comparison operators

def ifStatementsAndComparisons(arg1, arg2, arg3):

    if arg1 == "dog" and arg2 == "cat":
        print("You entered animals", arg1, "and", arg2)
    elif arg1 != arg2 and arg1 >= arg3:
        print("The greatest value is ", arg1)
    elif arg2 >= arg1 and arg2 >= arg3:
        print("The greatest value is ", arg2)
    else:
        print("The greatest value is ", arg3)




ifStatementsAndComparisons(6, "cat", 3)