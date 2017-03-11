
invalid = 'cow' == 'pig'

# You can check for successful validation as such. 

if not invalid:
    print('Validation is successful')

# OR as such, to avoid double negatives:

if invalid:
    pass
else:
    print('Validation is successful')

# Because you get syntax error if you have an if block containing nothing.
# 'pass' basically does nothing.
