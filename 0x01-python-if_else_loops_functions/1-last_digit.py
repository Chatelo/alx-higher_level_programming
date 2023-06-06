#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = number % 10 if number >= 0 else number % -10
string = "Last digit of " + str(number) + " is " + str(last_digit) + " and is "

if last_digit == 0:
    string += "0"
elif last_digit > 5:
    string += "greater than 5"
else:
    string += "less than 6 and not 0"

print(string)
