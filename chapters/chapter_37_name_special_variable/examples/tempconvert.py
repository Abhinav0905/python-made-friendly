"""Temperature conversions with a guarded CLI."""

import sys


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main(arguments=None):
    arguments = sys.argv[1:] if arguments is None else arguments
    if len(arguments) != 2:
        print("Usage: tempconvert.py TEMP UNIT", file=sys.stderr)
        return 2
    try:
        temperature = float(arguments[0])
    except ValueError:
        print("TEMP must be a number", file=sys.stderr)
        return 2
    unit = arguments[1].upper()
    if unit == "C":
        print(f"{temperature:.1f} C = {celsius_to_fahrenheit(temperature):.1f} F")
    elif unit == "F":
        print(f"{temperature:.1f} F = {fahrenheit_to_celsius(temperature):.1f} C")
    else:
        print("UNIT must be C or F", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
