"""
Creating a dictionary of squares for numbers from 1 to 5
using for loop
"""
numbers = [1, 2, 3, 4, 5]
# O/P: {1:1,2:4,3:9,4:16,5:25}
square_dict = {}
for n in numbers:
    square_dict.setdefault(n, n*n)
print(square_dict)
