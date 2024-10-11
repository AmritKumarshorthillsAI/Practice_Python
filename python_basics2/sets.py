# Basics of Sets

# Creating a Set
fruits = {"apple", "banana", "cherry", "date"}
print("Set of fruits:", fruits)  # Output: {'apple', 'banana', 'cherry', 'date'}

# Adding Elements
fruits.add("elderberry")           # Add a single element
print("After adding elderberry:", fruits)

# Adding Multiple Elements
fruits.update(["fig", "grape"])    # Add multiple elements
print("After adding fig and grape:", fruits)

# Removing Elements
fruits.remove("banana")            # Remove an element (raises KeyError if not found)
print("After removing banana:", fruits)

# Discarding Elements
fruits.discard("date")             # Remove an element (doesn't raise an error if not found)
print("After discarding date:", fruits)

# Set Length
print("Number of fruits in set:", len(fruits))  # Output: Number of unique fruits

# Set Membership
is_cherry_present = "cherry" in fruits
print("Is cherry present?", is_cherry_present)  # Output: True

# Set Operations

# 1. Union
tropical_fruits = {"pineapple", "mango"}
all_fruits = fruits.union(tropical_fruits)
print("Union of fruits:", all_fruits)  # Output: All unique fruits

# 2. Intersection
citrus_fruits = {"orange", "lemon", "banana"}
common_fruits = fruits.intersection(citrus_fruits)
print("Common fruits:", common_fruits)  # Output: Common fruits (if any)

# 3. Difference
difference_fruits = fruits.difference(citrus_fruits)
print("Fruits not in citrus fruits:", difference_fruits)  # Fruits in 'fruits' not in 'citrus_fruits'

# 4. Symmetric Difference
symmetric_difference = fruits.symmetric_difference(citrus_fruits)
print("Fruits in either set but not in both:", symmetric_difference)

# Set Methods

# 1. copy() - Returns a shallow copy of the set
fruits_copy = fruits.copy()
print("Copied set:", fruits_copy)

# 2. clear() - Removes all elements from the set
fruits.clear()
print("Set after clear():", fruits)  # Output: set()

# Re-adding elements for demonstration
fruits = {"apple", "banana", "cherry", "date"}

# 3. pop() - Removes and returns an arbitrary element from the set
popped_fruit = fruits.pop()
print("Popped fruit:", popped_fruit)  # Output: An arbitrary fruit
print("Set after pop():", fruits)

# 4. set() - Convert a list to a set (removes duplicates)
duplicate_list = ["apple", "banana", "apple", "cherry"]
unique_fruits = set(duplicate_list)
print("Unique fruits from list:", unique_fruits)

# 5. isdisjoint() - Returns True if two sets have no elements in common
another_set = {"orange", "lemon"}
is_disjoint = fruits.isdisjoint(another_set)
print("Are the sets disjoint?", is_disjoint)  # Output: Depends on the current fruits set

# 6. issubset() - Checks if a set is a subset of another set
subset_set = {"apple"}
is_subset = subset_set.issubset(fruits)
print("Is subset_set a subset of fruits?", is_subset)  # Output: True or False

# 7. issuperset() - Checks if a set is a superset of another set
is_superset = fruits.issuperset(subset_set)
print("Is fruits a superset of subset_set?", is_superset)  # Output: True or False
