# Parsing and extracting
data = 'From david.brown@university.edu Wed Sep 8 11:20:55 2021'
atpos = data.find('@')
sppos = data.find(' ',atpos)
host = data[atpos+1:sppos]
print(host)