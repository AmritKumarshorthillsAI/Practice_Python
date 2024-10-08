name = "Alice"
age = 30
result = "My name is %s and I'm %d years old" % (name, age)
print(result)

# concatenation using join
words = ["Python", "is", "awesome"]
res = " ".join(words)  # "Python is awesome"
print(res)


# String Creation
string1 = "Hello"
string2 = "World"

# String Concatenation
concatenated_string = string1 + " " + string2
print("Concatenated String:", concatenated_string)  # Output: Hello World

# String Indexing
first_char = concatenated_string[0]
last_char = concatenated_string[-1]
print("First Character:", first_char)  # Output: H
print("Last Character:", last_char)     # Output: d

# Slicing Strings
substring = concatenated_string[0:5]  # Get substring from index 0 to 4
print("Substring (0 to 4):", substring)  # Output: Hello

# Formatted Strings (f-strings)
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print("Formatted String:", formatted_string)  # Output: My name is Alice and I am 30 years old.

# Using str.format() Method
formatted_string2 = "My name is {} and I am {} years old.".format(name, age)
print("Formatted String using format():", formatted_string2)  # Output: My name is Alice and I am 30 years old.

# Using % Formatting
formatted_string3 = "My name is %s and I am %d years old." % (name, age)
print("Formatted String using %:", formatted_string3)  # Output: My name is Alice and I am 30 years old.

# String Methods
# 1. Uppercase
uppercase_string = concatenated_string.upper()
print("Uppercase String:", uppercase_string)  # Output: HELLO WORLD

# 2. Lowercase
lowercase_string = concatenated_string.lower()
print("Lowercase String:", lowercase_string)  # Output: hello world

# 3. Title Case
title_case_string = concatenated_string.title()
print("Title Case String:", title_case_string)  # Output: Hello World

# 4. Strip Whitespace
whitespace_string = "   Hello World   "
stripped_string = whitespace_string.strip()
print("Stripped String:", stripped_string)  # Output: Hello World

# 5. Replace Substring
replaced_string = concatenated_string.replace("World", "Python")
print("Replaced String:", replaced_string)  # Output: Hello Python

# 6. Split String
split_string = concatenated_string.split(" ")
print("Split String:", split_string)  # Output: ['Hello', 'World']

# 7. Join String
joined_string = ", ".join(split_string)
print("Joined String:", joined_string)  # Output: Hello, World

# 8. Check if String Contains a Substring
contains_hello = "Hello" in concatenated_string
print("Contains 'Hello':", contains_hello)  # Output: True

# 9. Count Occurrences of a Substring
count_hello = concatenated_string.count("l")
print("Count of 'l':", count_hello)  # Output: 3

# 10. String Length
string_length = len(concatenated_string)
print("Length of Concatenated String:", string_length)  # Output: 11

# 11. Find Index of a Substring
index_of_world = concatenated_string.find("World")
print("Index of 'World':", index_of_world)  # Output: 6

# 12. Check if String Starts/Ends with a Substring
starts_with_hello = concatenated_string.startswith("Hello")
ends_with_world = concatenated_string.endswith("World")
print("Starts with 'Hello':", starts_with_hello)  # Output: True
print("Ends with 'World':", ends_with_world)      # Output: True
 # type: ignore