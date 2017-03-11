#!/usr/bin/python

class Dog():
    #A simple attempt to model a dog
    def __init__(self, name, age):
        #Initialize name and age attributes
        self.name = name
        self.age = age
    def sit(self):
        #Simulate a dog sitting in response to a command
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        #Simulate rolling over in response to a command
        print(self.name.title() + " rolled over!")

    def shake(self):
        #Simulate a hand shake with your dog
        print(self.name.title() + " is shaking hands with a human!")

"This would create first object of Dog class"
dog1 = Dog("Winston", 34)

"This would create second object of Dog class"
dog2 = Dog("Murphy", 24)
dog1.sit()
dog2.roll_over()

dog1.shake()
