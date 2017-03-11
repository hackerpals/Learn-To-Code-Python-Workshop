#########
# BREAK #
#########

s = '''first line
second line
'''
s2 = ''

# Get only first  line in multi-line string
# By breaking on newline character.
for c in s:
    if c == '\n':
        break
    s2 += c
print("s2 is '{}'".format(s2))

############
# CONTINUE #
############

# Remove lines that are 'commented' with either # or //

s3 = '''first line
#second line
third line
#fourth line
// fifth line
sixth line
'''

new_lines = ''

for line in s3.split('\n'):
    if line.startswith('#'): 
        continue
    if line.startswith('//'): 
        continue
    new_lines += line+'\n'
print('non-commented lines')
print(new_lines)
