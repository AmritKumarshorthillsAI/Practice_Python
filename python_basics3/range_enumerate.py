def print_list_items(items):
    """Print each item in a list using an iterable."""
    print("Items in the list:")
    for item in items:
        print(item)

def generate_numbers(start, end):
    """Generate numbers from start to end using range and return as a list."""
    return list(range(start, end + 1))

def print_enumerated_list(items):
    """Print items in a list along with their indices using enumerate."""
    print("Enumerated items:")
    for index, item in enumerate(items):
        print(f"Index {index}: {item}")

def main():
    # Create a list of fruits
    fruits = ["apple", "banana", "cherry", "date"]

    # Print items in the list
    print_list_items(fruits)

    # Generate a list of numbers from 1 to 10
    numbers = generate_numbers(1, 10)
    print("Generated numbers:", numbers)

    # Print enumerated items from the list
    print_enumerated_list(fruits)

if __name__ == "__main__":
    main()
