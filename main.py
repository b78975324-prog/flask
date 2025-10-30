"""
Temperature Converter - Clean Version
This script converts temperatures between Celsius and Fahrenheit.
"""


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


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
    # Try with freezing point
    freezing_c = 0
    freezing_f = celsius_to_fahrenheit(freezing_c)
    print(f"\nFreezing point: {freezing_c}°C = {freezing_f:.1f}°F")
    # Try with boiling point
    boiling_c = 100
    boiling_f = celsius_to_fahrenheit(boiling_c)
    print(f"Boiling point: {boiling_c}°C = {boiling_f:.1f}°F")


if __name__ == "__main__":
    main()
