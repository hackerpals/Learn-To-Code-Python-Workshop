#!/usr/bin/python

s1 = 'abc'
s2 = "123"

# Join 2 strings together
print s1 + s2
print 'abc' + '123'

# But you cannot join a string and a non-string
print 'abc' + 123



s0="supercalifragilisticexpialidocious"
s1 = 'Hello World \n'
s2 = "Anothe String"
s3 = """
A multi line
string!
"""

print(type(s1))
print("%s, %s, %s" % (s1,s2,s3))


#Length
print(len(s0))
print('{0}:{1}'.format(s[0],s[-2]))
