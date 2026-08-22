"""Console entry point for ``mycalc NUM OP NUM``."""

import sys

from . import add, divide, multiply, subtract


OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculate(arguments):
    if len(arguments) != 3:
        raise ValueError("usage: mycalc NUM OP NUM")
    first_text, operator, second_text = arguments
    if operator not in OPERATIONS:
        raise ValueError(f"unknown operator: {operator}")
    return OPERATIONS[operator](float(first_text), float(second_text))


def main():
    try:
        result = calculate(sys.argv[1:])
    except (ValueError, ZeroDivisionError) as error:
        print(error, file=sys.stderr)
        return 2
    print(f"{result:g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
