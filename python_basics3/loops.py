def print_numbers_for_loop(n):
    """Print numbers from 1 to n using a for loop."""
    print("Using for loop:")
    for i in range(1, n + 1):
        print(i)
        
def print_numbers_while_loop(n):
    """Print numbers from 1 to n using a while loop."""
    print("Using while loop:")
    i = 1
    while i <= n:
        print(i)
        i += 1

def factorial_using_for(n):
    """Calculate factorial of n using a for loop."""
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def factorial_using_while(n):
    """Calculate factorial of n using a while loop."""
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    return factorial

def main():
    # Get user input
    n = int(input("Enter a positive integer: "))
    
    # Print numbers using for loop
    print_numbers_for_loop(n)

    # Print numbers using while loop
    print_numbers_while_loop(n)

    # Calculate factorial using for loop
    fact_for = factorial_using_for(n)
    print(f"Factorial of {n} using for loop is: {fact_for}")

    # Calculate factorial using while loop
    fact_while = factorial_using_while(n)
    print(f"Factorial of {n} using while loop is: {fact_while}")

if __name__ == "__main__":
    main()
