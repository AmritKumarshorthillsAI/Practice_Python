# List Operations, Methods, Slicing, and Unpacking

# Creating a List
fruits = ["apple", "banana", "cherry", "date"]

# Accessing Elements
print("First fruit:", fruits[0])         # Output: apple
print("Last fruit:", fruits[-1])          # Output: date

# Slicing
print("First two fruits:", fruits[0:2])   # Output: ['apple', 'banana']
print("Last two fruits:", fruits[-2:])    # Output: ['cherry', 'date']

# Adding Elements
fruits.append("elderberry")                # Adding to the end
print("After append:", fruits)             # Output: ['apple', 'banana', 'cherry', 'date', 'elderberry']

fruits.insert(1, "blueberry")              # Adding at a specific position
print("After insert:", fruits)              # Output: ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry']

# Removing Elements
fruits.remove("banana")                    # Remove by value
print("After remove:", fruits)             # Output: ['apple', 'blueberry', 'cherry', 'date', 'elderberry']

popped_fruit = fruits.pop()                # Remove and return the last item
print("Popped fruit:", popped_fruit)       # Output: elderberry
print("After pop:", fruits)                 # Output: ['apple', 'blueberry', 'cherry', 'date']

# List Length
print("Number of fruits:", len(fruits))    # Output: 4

# Sorting
fruits.sort()
print("Sorted fruits:", fruits)             # Output: ['apple', 'blueberry', 'cherry', 'date']

# Reversing
fruits.reverse()
print("Reversed fruits:", fruits)           # Output: ['date', 'cherry', 'blueberry', 'apple']

# List Comprehensions
squared_numbers = [x**2 for x in range(5)]
print("Squared Numbers:", squared_numbers)  # Output: [0, 1, 4, 9, 16]

# Unpacking
a, b, c, d = fruits  # Unpacking values into variables
print("Unpacked values:", a, b, c, d)       # Output depends on the current order of fruits

# Nested Lists
nested_list = [["apple", "banana"], ["cherry", "date"]]
print("Nested List:", nested_list)           # Output: [['apple', 'banana'], ['cherry', 'date']]

# Accessing Nested Lists
print("First fruit in nested list:", nested_list[0][0])  # Output: apple
print("Second fruit in nested list:", nested_list[1][1]) # Output: date
