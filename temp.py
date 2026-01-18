import sys

def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    default_celsius = 0.0
    celsius = float(sys.argv[1]) if len(sys.argv) > 1 else default_celsius

    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"Temperature in Fahrenheit: {fahrenheit}")
