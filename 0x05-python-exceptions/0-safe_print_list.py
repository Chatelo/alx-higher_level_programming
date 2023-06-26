#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed = 0  # Variable to keep track of the number of elements printed
    for i in range(x):  # Iterate up to the specified number of elements
        try:
            print(my_list[i], end="")  # Print the element at index i
            printed += 1  # Increment the printed count
        except IndexError:  # Handle the case when the index is out of range
            break  # Exit the loop if index is out of range
    print()  # Print a new line after printing the elements
    return printed  # Return the number of elements printed

