import re

data = 'From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008'

# Extracting the email address
result = re.findall(r'From (\S+@\S+)', data)

# Printing the email
print(result[0])  # Output: louis@media.berkeley.edu


result2 = re.findall('@([^ ]*)', data)
print(result2[0])

# Even cooler regex version!
result3 = re.findall('From .*@([^ ]*)', data)
print(result3[0])