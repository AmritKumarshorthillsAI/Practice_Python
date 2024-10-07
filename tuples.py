# Basics of Tuples

# Creating a Tuple
fruits = ("apple", "banana", "cherry", "date")
print("Tuple of fruits:", fruits)  # Output: ('apple', 'banana', 'cherry', 'date')

# Accessing Elements
print("First fruit:", fruits[0])    # Output: apple
print("Last fruit:", fruits[-1])     # Output: date

# Slicing Tuples
print("First two fruits:", fruits[0:2])  # Output: ('apple', 'banana')
print("Last two fruits:", fruits[-2:])   # Output: ('cherry', 'date')

# Concatenating Tuples
tropical_fruits = ("pineapple", "mango")
all_fruits = fruits + tropical_fruits
print("All fruits:", all_fruits)  # Output: ('apple', 'banana', 'cherry', 'date', 'pineapple', 'mango')

# Repeating Tuples
repeated_fruits = fruits * 2
print("Repeated fruits:", repeated_fruits)  # Output: ('apple', 'banana', 'cherry', 'date', 'apple', 'banana', 'cherry', 'date')

# Tuple Length
print("Number of fruits:", len(fruits))  # Output: 4

# Checking for Existence
is_banana_present = "banana" in fruits
print("Is banana present?", is_banana_present)  # Output: True

# Unpacking Tuples
a, b, c, d = fruits
print("Unpacked fruits:", a, b, c, d)  # Output: apple banana cherry date

# Nested Tuples
nested_tuple = (("apple", "banana"), ("cherry", "date"))
print("Nested Tuple:", nested_tuple)  # Output: (('apple', 'banana'), ('cherry', 'date'))

# Accessing Nested Tuples
print("First fruit in nested tuple:", nested_tuple[0][0])  # Output: apple

# Tuple Methods
# 1. count() - Counts the occurrences of a value
fruits_with_duplicates = ("apple", "banana", "apple", "cherry")
apple_count = fruits_with_duplicates.count("apple")
print("Count of 'apple':", apple_count)  # Output: 2
