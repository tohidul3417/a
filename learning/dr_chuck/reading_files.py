# Counting lines in a file
fhand = open('./mbox.txt')
count = 0
for word in fhand:
    count = count + 1
print('Line Count:', count)

# Reading the whole file
the_file = open('mbox-short.txt')
readable_file = the_file.read()
print(len(readable_file))
print(readable_file[0:30])

# Searching through a file
file = open('mbox-short.txt')
for line in file:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
print('\nSecond\n')

file2 = open ('mbox-short.txt')
for line in file2:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)


print('\nThird\n')

# Using 'in' to select line
file3 = open('./mbox-short.txt')
for line in file3:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)


print('\nPrompt for File Nameh\n')

# Prompt for file name
file = input('Enter the file name: ')
file = open(file)
count = 0
for line in file:
    line = line.rstrip()
    if line.startswith('Subject'):
        count = count + 1
print('There were', count, 'subject lines in', file)

print('\nFifth\n')

# Handling bad file names
file_name = input('Enter the file name: ')
try:
    prepared_file = open(file_name)
except:
    print('File cannot be found', file_name)
    quit()
count = 0
for line in prepared_file:
    if line.startswith('Subject'):
        count = count + 1
print('Total subject lines:', count)