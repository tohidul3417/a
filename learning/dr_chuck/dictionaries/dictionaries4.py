fname = input("Enter the file: ")
fhandle = open(fname)
counts = dict()

for line in fhandle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigWord = None
bigCount = None
for word, count in counts.items():
    if bigWord is None or count > bigCount:
        bigWord = word
        bigCount = count
print('#Big word:', bigWord, '#Big count:', bigCount)