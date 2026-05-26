# Purpose: A program combining two integer rays into a third, larger array without duplicate values.
# Sorted in ascending numerical order

# import random to use random integer generator for arrays
import random

# prompt user for integer input, prompt for the input value
N = int(input("Enter a positive integer greater than 1: "))
# open for whatever data is used
arr1 = []
# user input determining size of range of numbers generated randomly
for i in range(N):
    # allows any random number 0 through 500
    arr1.append(random.randint(0, 500))
# open for whatever data is used
arr2 = []
# user input determining size of range of numbers generated randomly
for i in range(N):
    # allows any random number 0 through 500
    arr2.append(random.randint(0, 500))

# combined array 1 and array 2 using + operations.
# Converted to set to remove duplicate values, then to list to order them
arr3 = list(set(arr1 + arr2))
# iterates over the range of the object starting from 0 to length of the object
for i in range(len(arr3)):
    for j in range(i + 1, len(arr3)):
        # if array 3 [i] is greater than array 3 [j]
        if arr3[i] > arr3[j]:
            # place array 3 [j] before array 3 [i], this sorts everything numerically, ascending
            arr3[i], arr3[j] = arr3[j], arr3[i]
# iterates over array 3 using a for loop
for i in arr3:
    # prints results
    print(i)
