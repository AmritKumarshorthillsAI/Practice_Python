def break_example(n):
    """Demonstrate the use of break in a loop."""
    print("Break example:")
    for i in range(n):
        if i == 5:
            print("Breaking the loop at i =", i)
            break  # Exit the loop when i equals 5
        print(i)

def continue_example(n):
    """Demonstrate the use of continue in a loop."""
    print("\nContinue example:")
    for i in range(n):
        if i % 2 == 0:
            print("Skipping even number:", i)
            continue  # Skip the rest of the loop for even numbers
        print("Odd number:", i)

def pass_example(n):
    """Demonstrate the use of pass in a loop."""
    print("\nPass example:")
    for i in range(n):
        if i < 3:
            pass  # Do nothing for i < 3
        else:
            print("Processing number:", i)

def main():
    n = 10  # Define the range limit

    break_example(n)    # Demonstrate break
    continue_example(n) # Demonstrate continue
    pass_example(n)     # Demonstrate pass

if __name__ == "__main__":
    main()
