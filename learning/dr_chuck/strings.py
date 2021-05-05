# Looping through strings
word = 'elephant'
index = 0
while index < len(word):
    print(index, word[index])
    index = index + 1

# Preferred way here to loop through strins is using for loop, because it is taking less amout of code
fruit = "apple"
for letter in fruit:
    print(letter)

# Looping and counting
name = "remember"
count = 0
for letter in name:
    if letter == 'm':
        count = count + 1
print(count)