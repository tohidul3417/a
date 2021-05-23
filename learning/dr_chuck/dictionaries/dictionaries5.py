fname = input('Enter the file name: ')
if len(fname) < 1: fname = '../clown.txt'
fhandle = open(fname)

counts = dict()

for line in fhandle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigWord = None
bigCount = None
for word, count in counts.items():
    if bigWord is None or count > bigCount:
        bigWord = word
        bigCount = count
print('#' + bigWord + '#' + str(bigCount))