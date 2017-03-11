<<<<<<< HEAD
#!/usr/bin/python

for i in range(0, 4):
    print i
=======
# Loop a list

print('Loop List')
for i in [11, 12, 13]:
    print(i)

# Loop a dictionary

d = {
    'a': 1,
    'b': 2,
}

# d.items() returns a lazy list of tuples looking
# like the following, which makes it loopable:
"""
[('a', 1), ('b', 2)]
"""
print('Loop Dictionary')
for key, value in d.items():
    print(key, value)
>>>>>>> origin/master
