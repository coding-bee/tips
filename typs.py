# Swap Variables
a = 10
b = 20
a, b = b, a
print(a, b)  # Output: 20 10

# List Comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]

# Dictionary Comprehension
numbers = [1, 2, 3, 4, 5]
squares_dict = {x: x**2 for x in numbers}
print(squares_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Check if All Elements in a List Satisfy a Condition
numbers = [10, 20, 30, 40, 50]
all_greater_than_zero = all(x > 0 for x in numbers)
print(all_greater_than_zero)  # Output: True

# Merge Two Dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Unpack Elements from a List
numbers = [1, 2, 3]
a, b, c = numbers
print(a, b, c)  # Output: 1 2 3

# Find the Most Common Element in a List
numbers = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5]
most_common = max(set(numbers), key=numbers.count)
print(most_common)  # Output: 5

# Iterate Over Multiple Lists Simultaneously
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, age)
# Output:
# Alice 25
# Bob 30
# Charlie 35

# Remove Duplicates from a List while Preserving Order (Python 3.7+)
numbers = [1, 2, 3, 3, 4, 4, 5, 5]
unique_numbers = list(dict.fromkeys(numbers))
print(unique_numbers)  # Output: [1, 2, 3, 4, 5]

# Create a Timer using timeit module
import timeit

def my_function():
    # Code to measure the execution time

# Measure the execution time of my_function
execution_time = timeit.timeit(my_function, number=1)
print(execution_time)
