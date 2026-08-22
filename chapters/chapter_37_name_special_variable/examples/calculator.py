"""Importable arithmetic and a guarded command-line calculator."""

import sys


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide}


def main(arguments=None):
    arguments = sys.argv[1:] if arguments is None else arguments
    if len(arguments) != 3:
        print("Usage: calculator.py NUM OP NUM", file=sys.stderr)
        return 2
    first_text, operator, second_text = arguments
    try:
        first, second = float(first_text), float(second_text)
        operation = OPERATIONS[operator]
        result = operation(first, second)
    except ValueError as error:
        print(error, file=sys.stderr)
        return 2
    except KeyError:
        print(f"unknown operator: {operator}", file=sys.stderr)
        return 2
    print(f"{first:g} {operator} {second:g} = {result:g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
