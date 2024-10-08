# Creating a Dictionary
fruits = {
    "apple": 3,
    "banana": 5,
    "cherry": 10,
    "date": 7
}

# Accessing Values by Key
print("Number of apples:", fruits["apple"])  # Output: 3

# Using the get() Method
print("Number of bananas:", fruits.get("banana"))  # Output: 5
print("Number of oranges (not in dict):", fruits.get("orange", 0))  # Output: 0 (default value)

# Adding or Updating Key-Value Pairs
fruits["elderberry"] = 4  # Adding a new key-value pair
fruits["banana"] = 6      # Updating an existing key
print("Updated dictionary:", fruits)

# Removing Key-Value Pairs
removed_value = fruits.pop("cherry")  # Removes 'cherry' and returns its value
print("Removed cherries:", removed_value)  # Output: 10
print("After removing cherries:", fruits)

# Checking for Keys
is_apple_present = "apple" in fruits
print("Is apple present?", is_apple_present)  # Output: True

# Dictionary Length
print("Number of unique fruits:", len(fruits))  # Output: 4

# Iterating Over a Dictionary
print("\nFruits and their quantities:")
for fruit, quantity in fruits.items():
    print(f"{fruit}: {quantity}")

# Dictionary Methods

# 1. keys() - Returns a view of the dictionary's keys
print("\nKeys in the dictionary:", fruits.keys())  # Output: dict_keys(['apple', 'banana', 'date', 'elderberry'])

# 2. values() - Returns a view of the dictionary's values
print("Values in the dictionary:", fruits.values())  # Output: dict_values([3, 6, 7, 4])

# 3. items() - Returns a view of the dictionary's key-value pairs
print("Items in the dictionary:", fruits.items())  # Output: dict_items([('apple', 3), ('banana', 6), ('date', 7), ('elderberry', 4)])

# 4. clear() - Removes all items from the dictionary
fruits.clear()
print("Dictionary after clear():", fruits)  # Output: {}

# Re-adding elements for demonstration
fruits = {
    "apple": 3,
    "banana": 5,
    "cherry": 10,
    "date": 7
}

# 5. copy() - Returns a shallow copy of the dictionary
fruits_copy = fruits.copy()
print("Copied dictionary:", fruits_copy)

# 6. update() - Updates the dictionary with key-value pairs from another dictionary
fruits.update({"banana": 6, "fig": 2})  # Updates banana and adds fig
print("After update:", fruits)

# 7. setdefault() - Returns the value of a key if it exists, otherwise sets it to a default value
date_quantity = fruits.setdefault("date", 0)  # date already exists
print("Quantity of dates (setdefault):", date_quantity)  # Output: 7
new_fruit_quantity = fruits.setdefault("grape", 5)  # grape doesn't exist, sets it to 5
print("Quantity of grapes (setdefault):", new_fruit_quantity)  # Output: 5
print("After setdefault:", fruits)
