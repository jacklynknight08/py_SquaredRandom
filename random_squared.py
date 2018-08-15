# Using the random module and the range method, generate a list of 20 
# random numbers between 0 and 49.

# With the resulting list, use a list comprehension to build a new list 
# that contains each number squared. 
# For example, if the original list is [2, 5], the final list will be [4, 25].

import random

random_numbers = [random.randrange(0, 50, 1) for num in range(20)]
print(random_numbers)

squared = [x**2 for x in random_numbers]
print(squared)
