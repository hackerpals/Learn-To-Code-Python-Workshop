#!/usr/bin/python

"""Display a simple greeting."""
def hello_user():
    print("Hello Human!")


hello_user() # Returns "Hello Human"

#Display a simple greeting
def greet_user(human):
    print("Hello, " + human.title() + "!")


greet_user('Jack')# Returns "Hello, Jack"
