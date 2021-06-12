import re
fhandle = open('../mbox-short.txt')

nums = list()
for line in fhandle:
    line = line.rstrip()
    result = re.findall(r'^X\S*?: ([0-9.]+)', line)
    if len(result) != 1: continue
    num = float(result[0])
    nums.append(num)


print('Maximum:', max(nums))