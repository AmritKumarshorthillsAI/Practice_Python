import re
from datetime import datetime

def calculate_bmi(weight_kg, height_m):
    """
    Calculate BMI (Body Mass Index) given weight in kg and height in meters.
    """
    if height_m <= 0:
        raise ValueError("Height must be greater than 0")
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)

def is_valid_email(email):
    """
    Check if the given email address is valid using a simple regex pattern.
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def get_age(birthdate):
    """
    Calculate age given a birthdate in 'YYYY-MM-DD' format.
    """
    birth_date = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.now()
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    return age

def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    """
    return (celsius * 9/5) + 32

def word_frequency(text):
    """
    Count the frequency of words in a given text.
    Returns a dictionary with words as keys and their frequencies as values.
    """
    words = text.lower().split()
    return {word: words.count(word) for word in set(words)}

# Example usage:
if __name__ == "__main__":
    print(f"BMI: {calculate_bmi(70, 1.75)}")
    print(f"Is valid email: {is_valid_email('user@example.com')}")
    print(f"Age: {get_age('1990-05-15')}")
    print(f"32°C in Fahrenheit: {celsius_to_fahrenheit(32):.1f}°F")
    print(f"Word frequency: {word_frequency('the quick brown fox jumps over the lazy dog')}")

