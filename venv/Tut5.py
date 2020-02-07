#Welcome to Python Tutorial 5!

#Lists in Python (Arrays)

#You can mix data types in an array in python if you want!
friendsList = ["Alice", "Bob", "Caitlin"]

#You can access array elements based on their index
print(friendsList[0])

#you can also access array elements from reverse by using negative values
print(friendsList[-1])

#Another way to access array elements is, 1: gets all elements from position 1 and after
print(friendsList[1:])

#We can also access a range of array elements
print(friendsList[0:2])

#We can modify array values by assigning values to their element index
friendsList[1] = "Bethany"

#List functions

#List / Array 1
lucky_numbers = [4, 8, 15, 16, 23, 42]

#append allows for adding another array element
friendsList.append("Dave")

#Extend allows for concatenating one array to another

#Insert allows for insering an element into an array
friendsList.insert(1,"Kelly")

print(friendsList)

#Remove allows for the removal of array elements
friendsList.remove("Kelly")

print(friendsList)

#Pop removes the last element from the array
friendsList.pop()

print(friendsList)

#Index returns the element index of a value in the array
print(friendsList.index("Caitlin"))

#Count returns the number of occurances in an array of a value
print(friendsList.count("Bethany"))

#Add a new element to the end of our array
friendsList.append("Anna")

print(friendsList)

#Sort, sorts our array, either alphabetically for strings or ascending order for integer arrays
friendsList.sort()

#Reverse, reverses the order of our array
friendsList.reverse()

#Copy allows for copying one array to antoher
friends2 = friendsList.copy()
print(friends2)

friendsList.reverse()

print(friendsList)

#End of Python Tutorial 5
