# Sorting dictionary using tuple
data = {
    'kiwi': 12,
    'apple': 4,
    'mango': 9,
    'banana': 1,
    'grape': 7,
    'orange': 3
}

tmp = list()

for key, val in data.items():
    tmp.append((val, key))

print(tmp)
tmp = sorted(tmp)

newTmp = []
for val, key in tmp[:5]:
    newTmp.append((key, val))
print(newTmp)

# Shorter version
data = {
    'kiwi': 12,
    'apple': 4,
    'mango': 9,
    'banana': 1,
    'grape': 7,
    'orange': 3
}

print(sorted([(v, k) for k, v in data.items()]))