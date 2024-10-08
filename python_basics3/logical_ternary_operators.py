def logical_operators(a, b):
    """Demonstrate the use of logical operators."""
    print("Logical Operators:")
    print(f"a: {a}, b: {b}")
    print("a and b:", a and b)  # Returns b if a is truthy, otherwise returns a
    print("a or b:", a or b)    # Returns a if it's truthy, otherwise returns b
    print("not a:", not a)      # Returns the negation of a

def ternary_operator(condition, true_value, false_value):
    """Demonstrate the use of the ternary operator."""
    result = true_value if condition else false_value
    print(f"Ternary Operator: {condition} ? {true_value} : {false_value} => {result}")

def short_circuiting(a, b):
    """Demonstrate short-circuiting with logical operators."""
    print("Short-Circuiting:")
    if a and (b != 0):  # Check if b is not zero to prevent division by zero
        print("Evaluating b / 0:", b / 0)  # This will not cause an error due to short-circuiting
    else:
        print("Short-circuiting occurred; b was not evaluated or is zero.")

def main():
    # Test logical operators
    logical_operators(True, False)
    logical_operators(5, 0)

    # Test ternary operator
    ternary_operator(10 > 5, "Greater", "Smaller")
    ternary_operator(5 > 10, "Greater", "Smaller")

    # Test short-circuiting
    short_circuiting(False, 10)  # a is False, so b will not be evaluated
    short_circuiting(True, 0)     # a is True, but b is zero, preventing division

if __name__ == "__main__":
     main()
   

