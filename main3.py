"""
Temperature Converter - Buggy Version
This script has multiple issues for you to find!
"""

import math  # Unused import - linter will catch this

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    # Bug: Wrong formula!
    return celsius * 9/5 + 30  # Should be +32, not +30


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    # Bug: Missing parentheses - wrong order of operations
    return fahrenheit - 32 * 5/9  # Should be (fahrenheit - 32) * 5/9


def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    # Fixed syntax: added missing colon after function definition
    return kelvin - 273.15


def main():
    """Main function to run the temperature converter."""
    print("Temperature Converter")
    print("=" * 40)
    
    # Convert some temperatures
    temp_c = 25
    temp_f = celsius_to_fahrenheit(temp_c)
    print(f"{temp_c}°C = {temp_f:.1f}°F")
    
    temp_f = 77
    temp_c = fahrenheit_to_celsius(temp_f)
    print(f"{temp_f}°F = {temp_c:.1f}°C")
    
    # Unused variable - linter will warn
    unused_variable = 42
    
    # Try with freezing point
    freezing_c = 0
    freezing_f = celsius_to_fahrenheit(freezing_c)
    print(f"\nFreezing point: {freezing_c}°C = {freezing_f:.1f}°F")
    
    # Bug: Typo in variable name
    boiling_c = 100
    boiling_f = celsius_to_fahrenheit(boiling_c)
    print(f"Boiling point: {boiling_C}°C = {boiling_f:.1f}°F")  # 'C' should be lowercase 'c'
    
    # Bug: Dividing by zero
    result = calculate_average([1, 2, 3])
    print(f"\nAverage: {result}")


def calculate_average(numbers):
    """Calculate average of numbers."""
    total = 0
    count = 0
    # Bug: count stays 0, will cause division by zero
    for num in numbers:
        total += num
    return total / count  # Division by zero!


if __name__ == "__main__":
    main()