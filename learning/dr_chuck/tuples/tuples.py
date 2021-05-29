x = ('John', 'Ran', 35, 33, 'Lain')
print(x[0])
nums = (34, 5, 13, 53, 124)
print(sum(nums) / len(nums))
print(type(x))
# tuples and assignment
(x, y) = ('john', 34)
print(y)
print(type(y))

# Tuples are comparable
tuple_a = (34, 55, 24)
tupble_b = (33, 2, 5)
print(tupble_b > tuple_a)
tuple_c = ('Elo', 'Lenin')
tupble_d = ('Elias', 'Elo')
print(tupble_d > tuple_c)