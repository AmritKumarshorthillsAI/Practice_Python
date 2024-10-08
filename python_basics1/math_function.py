import math

class Math:
    # constructor
    def __init__(self):
        """
        Initialize the Math class.
        """
        pass

    def add(self, a, b):
        """Return the sum of two numbers."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of two numbers."""
        return a - b

    def multiply(self, a, b):
        """Return the product of two numbers."""
        return a * b

    def divide(self, a, b):
        """Return the quotient of two numbers. Raises an error if dividing by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def power(self, base, exponent):
        """Return the result of base raised to the power of exponent."""
        return base ** exponent

    def factorial(self, n):
        """Return the factorial of a number."""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def maximum(self, *args):
        """Return the maximum value among the given numbers."""
        return max(args)

    def minimum(self, *args):
        """Return the minimum value among the given numbers."""
        return min(args)

    def absolute(self, x):
        """Return the absolute value of a number."""
        return abs(x)

    def power_func(self, base, exponent):
        """Return the result of base raised to the power of exponent."""
        return pow(base, exponent)

    def ceil(self, x):
        """Return the smallest integer greater than or equal to x."""
        return math.ceil(x)

    def floor(self, x):
        """Return the largest integer less than or equal to x."""
        return math.floor(x)

# Create an object of the Math class
math_operations = Math()

# Using the methods of the Math class
print("Addition (5 + 3):", math_operations.add(5, 3))                    # Output: 8
print("Subtraction (5 - 3):", math_operations.subtract(5, 3))            # Output: 2
print("Multiplication (5 * 3):", math_operations.multiply(5, 3))         # Output: 15
print("Division (5 / 3):", math_operations.divide(5, 3))                 # Output: 1.666...
print("Power (2 ^ 3):", math_operations.power(2, 3))                     # Output: 8
print("Factorial (5!):", math_operations.factorial(5))                   # Output: 120
print("Maximum (5, 3, 9, 1):", math_operations.maximum(5, 3, 9, 1))      # Output: 9
print("Minimum (5, 3, 9, 1):", math_operations.minimum(5, 3, 9, 1))      # Output: 1
print("Absolute (-10):", math_operations.absolute(-10))                  # Output: 10
print("Power Function (2, 3):", math_operations.power_func(2, 3))        # Output: 8
print("Ceil (4.3):", math_operations.ceil(4.3))                          # Output: 5
print("Floor (4.7):", math_operations.floor(4.7))                        # Output: 4


