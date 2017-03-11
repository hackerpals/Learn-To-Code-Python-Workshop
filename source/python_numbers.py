#!/usr/bin/python
# This file is named python_numbers.py instead of numbers.py
# in order to avoid collision with an existing library also called numbers.

# Integer
a = 1
b = 0x10
print(type(a))

# Complex
e = 1+2j
c = 3.14j
f = complex(1,2)
print(type(e))
print(f == e)

# Float
# https://docs.python.org/3/tutorial/floatingpoint.html
c = 1.2
d = .5
g = .314e1
print(type(g))

f = 14.55
(0.1 + 0.1 + 0.1) == 0.3

# Decimal

from decimal import Decimal
(Decimal('0.1') + Decimal('0.1') + Decimal('0.1')) == Decimal('0.3')
