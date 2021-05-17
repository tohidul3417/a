# Using split method
sentence = 'We were having fun all the time'
words = sentence.split()
print(words)


# 
fhand = open('mbox-short.txt')
for line in fhand:
    line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])

# The double split pattern
fhand = open('mbox-short.txt')
for line in fhand:
    line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]
    pieces = email.split('@')
    name = pieces[0]
    print(name)