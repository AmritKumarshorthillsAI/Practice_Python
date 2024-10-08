# Explicit type conversion

# Convert float to integer
float_number = 7.9
int_number = int(float_number)
print("Float to Integer:", int_number)  # Output: 7

# Convert integer to float
int_value = 10
float_value = float(int_value)
print("Integer to Float:", float_value)  # Output: 10.0

# Convert integer to string
int_value = 123
str_value = str(int_value)
print("Integer to String:", str_value)   # Output: '123'

# Convert string to integer
str_number = "456"
int_number = int(str_number)
print("String to Integer:", int_number)   # Output: 456

# Convert string to float
str_float = "3.14"
float_number = float(str_float)
print("String to Float:", float_number)    # Output: 3.14

# Convert list to string
list_value = [1, 2, 3]
str_list = str(list_value)
print("List to String:", str_list)         # Output: '[1, 2, 3]'



# Convert list to tuple
list_data = [1, 2, 3]
tuple_data = tuple(list_data)
print("List to Tuple:", tuple_data)        # Output: (1, 2, 3)

# Convert tuple to list
tuple_data = (4, 5, 6)
list_data = list(tuple_data)
print("Tuple to List:", list_data)         # Output: [4, 5, 6]
