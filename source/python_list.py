#Start a list
l = ['python', 12, 'Hacker', 'pals', 'seven']
print(type(l))

#print the length of list
print(len(l))


#Slicing
print(l[0])
print(l[-1])
print(l[1:-1])


#Edit your list
l.append('hey')

l.insert(2, '.4.1')

l.extend(['!','!'])


print(l.pop())

print(l.pop(2))

l.remove("in")

del l[2]


#index
print(l.index('pic'))
