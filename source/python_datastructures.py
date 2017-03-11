#!/usr/bin/python

########
# List #
########

l = ['abc', 34, 4.34, 23]
l.append(50)

print l # l will now contain 50 as the fifth item
print l[4] # outputs 50

#########
# Tuple #
#########

t = (1, 2, 3, 'John')

"""
Append does NOT work because you cannot mutate tuples
and t will always contain 4 items with those values.
t.append(5)
"""

# But you can create new tuples with 5 as the fifth item.
t2 = t + (5,)

print t2 # t2 will result in (1, 2, 3, 'a', 5)
print t2[4] # outputs 5

##############
# Dictionary #
##############

d = {'first_name': 'John', 'age': 5}

# Add more key values to dictionary
d['last_name'] = 'Doe'

print d # outputs {'first_name': 'John', 'age': 5, 'last_name': 'Doe'}
print d['first_name'] # outputs 'John'
print d['last_name'] # outputs 'Doe'
