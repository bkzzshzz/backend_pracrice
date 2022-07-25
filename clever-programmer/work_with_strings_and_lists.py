# name from email

email = 'lovely@love.com'
name = email[:email.index('@')]
print(f"Hello {name}!")

print(f"The email you use is {email[email.index('@'):-4]}")

print(email[0:-1:2])
print(email[::-1])

#using find
print(email.find('@'))

# using split
# This splits the data and gives a list
raw_data = "XBOX 360 | 150 | New"
separated_data = raw_data.split('|')
print(separated_data)
print(f"The price of {separated_data[0]} is {separated_data[1]} and is {separated_data[2]} condition")

# Better way
# the split data is directly mapped to the variables
# strip() function removes the leading and the trailing white spaces
raw_data = "XBOX 360 | 150 | New"
product, price, status = raw_data.split('|')
print(f"The price of {product.strip()} is {price.strip()} and is {status.strip()} condition")

# use append() to append data onto a list
separated_data.append('Trending')
print(separated_data)
