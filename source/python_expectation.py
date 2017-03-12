#!/usr/bin/python

while True:
    try:
        x = int(raw_input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

"""

Zero divison example

"""
def input_numbers():
    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))
    return a, b


x, y = input_numbers()

while True:
    try:
        print("%d / %d is %f" % (x, y, x/y))
        break
    except ZeroDivisionError:
       print("Cannot divide by zero")
       x, y = input_numbers()
