# Repeated steps
n = 8
while n > 0:
    print(n)
    n = n - 1
print('Done')
print(n)

# Breaking out of a loop
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print("Done!")

# Continue
while True:
    line = input('>')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Bye!')
