intro = 'My name is Jeff!'

print(intro[0]) #prints M

print(intro[0:2]) #prints My

print(intro[-5:-1]) #prints Jeff

# len() measure the length of a string (with the spaces)

intro1 = 'My name is Jeff!'
intro2 = 'Hello all!'
intro3 = 'Hi there.'

print(len(intro1)) # evaluates 16
print(len(intro2)) # evaluates 10
print(len(intro3)) # evaluates 9

# str.lower(), str.upper(), str.title() = .lower() converts all letters to lowercase, .upper() converts all letters to uppercase, .title() converts all first letters in uppercase

print(intro.lower()) # prints 'my name is jeff!'
print(intro.upper()) # prints 'MY NAME IS JEFF!'
print(intro.title()) # prints 'My Name Is Jeff!'

# str.split() takes a string and splits into a list of strings.

print(intro.split()) # prints ['My', 'name', 'is', 'Jeff!']
print(intro.split('name')) # prints ['My', ' is Jeff!']
print(intro.split('!')) # prints ['My name is Jeff', '']