# Escape character
import re
x = 'We just received $15.00 for cookies'
result = re.findall(r'\$[0-9.]+', x)
print(result[0])