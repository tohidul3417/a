# slicing strings
word = "Monty Python"
print(word[1:4]) #Starts from '1' index, including index upto 4 (not including 4);

# Using 'in' as a logical operator
print('k' in word)
print('t' in word)

# String library. Python has a number of string functions which are in string library
greet = "Hello World"
zap = greet.lower()
print(zap)
print('Hello Friend'.lower())
nnn = greet.upper()
print(nnn)

message = 'This is our village. We should take care of it. A village should be a place for all'
nstr = message.replace('village', 'district')
print(nstr)
print(message)
nstr = message.replace(" ", "-")
print(nstr)

greeting2 = ' Hello friend, what are you doing? '
stripped_left = greeting2.lstrip()
stripped_right = greeting2.rstrip()
stripped = greeting2.strip()
print(greeting2)
print(stripped_left)


# Prefixes
line = 'Hello there'
print(line.startswith('H'))
