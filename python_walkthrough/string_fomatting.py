# numbers need to be converted into strings to concatenate strings with float numbers

# using str() function

print('The value of pie is ' + str(3.14))

# string formatting with .format()

string1 = 'Need'
string2 = 'Love'
string3 = 'The Beatles'

print('All you {} is {}, sung by {}'.format(string1, string2, string3))

# or use the f-string formatting, which i prefer

print(f'All you {string1} is {string2}, sung by {string3}')