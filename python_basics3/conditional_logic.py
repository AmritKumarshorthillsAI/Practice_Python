def check_age(age):
    """Check if the person is a minor, adult, or senior."""
    if age < 18:
        return "You are a minor."
    elif age < 65:
        return "You are an adult."
    else:
        return "You are a senior."

def categorize_temperature(temperature):
    """Categorize the weather based on temperature."""
    if temperature < 0:
        return "It's freezing!"
    elif temperature < 20:
        return "It's cold."
    elif temperature < 30:
        return "It's warm."
    else:
        return "It's hot!"

def is_even_or_odd(number):
    """Determine if a number is even or odd."""
    return "Even" if number % 2 == 0 else "Odd"

def validate_input(value):
    """Check if the input value is valid (greater than zero)."""
    if value <= 0:
        return "Invalid input! Please enter a positive number."
    return "Valid input."

def main():
    # Example of using the functions

    # Check age category
    age = int(input("Enter your age: "))
    print(check_age(age))

    # Check temperature category
    temperature = float(input("Enter the temperature: "))
    print(categorize_temperature(temperature))

    # Check if a number is even or odd
    number = int(input("Enter a number: "))
    print(f"The number is {is_even_or_odd(number)}.")

    # Validate user input
    user_input = float(input("Enter a positive number: "))
    print(validate_input(user_input))

if __name__ == "__main__":
    main()
