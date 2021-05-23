counts = dict()
line = '''The deep sea remains one of the most mysterious and least explored places on Earth.
With depths reaching over 36,000 feet, it harbors creatures that have adapted to 
extreme pressure, complete darkness, and frigid temperatures. Bioluminescent organisms,
like the anglerfish and jellyfish, create their own light to navigate and hunt in the abyss. 
Scientists believe that studying these deep-sea ecosystems could provide insights into medicine,
 climate change, and even extraterrestrial life, as extreme environments on other planets may share
similarities with Earth's deep oceans. Despite technological advancements, more than 80% of the ocean
 remains unexplored, leaving vast opportunities for future discoveries.'''
words = line.split()
print('words:', words)
print('Printing counts....')
for word in words:
    word = word.rstrip('.')
    if (not word in counts):
        counts[word] = 1
    else:
        counts[word] = counts[word] + 1
print(counts)

# Simplified
counts = dict()
line = input('Enter a line: ')
words = line.split()
for word in words:
    word = word.rstrip()
    counts[word] = counts.get(word, 0) + 1
print(counts)