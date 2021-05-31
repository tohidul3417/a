# Sorting dictionary using tuple
data = {
    'kiwi': 12,
    'apple': 4,
    'mango': 9,
    'banana': 1,
    'grape': 7,
    'orange': 3
}
print(data)

sortedItems = sorted(data.items())
print('Sorted Items', sortedItems)
sortedDic = dict(sortedItems)
print('Sorted dictionary', sortedDic)

sortedByValue = sorted(data.items(), key=lambda item : item[1])
print(dict(sortedByValue))