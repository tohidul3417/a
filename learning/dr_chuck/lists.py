friends = ['Sakib', 'Elisa', 'Rakib', 'Jog']
for i in range(len(friends)):
    friend = friends[i]
    print('Happy new year', friend)

# Concatenating lists using +
a = [34, 53, 55]
b = [25, 52, 22, 55]
c = a + b
print(c)

# Building a list from scratch
stuff = list()
stuff.append('book')
stuff.append(34)
print(stuff)

# Lists are in order
friends = ['Wasim', 'Raju', 'Elvis', 'Rahi', 'Ceny']
friends.sort()
print(friends)
numbers = [34, 5, 24, 52, 14, 54, 92, 24]
numbers.sort()
print(numbers)
print(sum(numbers) / len(numbers))

# Calculating the average
total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    inp = float(inp)
    total = total + inp
    count = count + 1
print(total / count)

# Another way
numbers = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    numbers.append(float(inp))
print('Average:', sum(numbers) / len(numbers))