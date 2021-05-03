# finding the largest value
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [24, 25, 65, 24, 52, 51, 58]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far)

# Counting in a loop
count = 0
print('Before', count)
for item in [24, 52, 51, 14, 62, 24]:
    count = count + 1
    print(count, item)
print('After', count)

# Summing in a loop
sum = 0
print('Before', sum)
for num in [34, 1, 534, 13, 1, 152, 243, 2]:
    sum = sum + num
    print(sum, num)
print('After', sum)

def findAverage(numbers):
    count = 0
    sum = 0
    for num in numbers:
        count += 1
        sum += num
    average = sum / count
    return average

average = findAverage([34, 52, 22, 53, 90, 66, 89, 25, 99])
print(average)

# find lowest nuumber
lowest = None
for num in [34, 52, 2, 52, 2, 53, 24, 52]:
    if lowest is None:
        lowest = num
    elif num < lowest:
        lowest = num
print(lowest)