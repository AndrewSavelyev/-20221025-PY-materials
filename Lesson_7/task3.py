# List comprehension exercise
#
# Use a list comprehension to make a list containing tuples (i, j) where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.
# sevens = [i for i in range(0, 71, 7) if i % 5 != 0]

# dict = {}
# for i in range(1, 10):
#     dict[i] = i*i
# print(dict)

dict = {i: i*i for i in range(1, 10)}
print(dict)
