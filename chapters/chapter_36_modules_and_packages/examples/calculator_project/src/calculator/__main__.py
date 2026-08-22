"""Run the calculator package with ``python -m calculator``."""

from . import add, divide, multiply, subtract


def main():
    print("Calculator Package Demo")
    print("add(10, 5) =", add(10, 5))
    print("subtract(10, 5) =", subtract(10, 5))
    print("multiply(10, 5) =", multiply(10, 5))
    print("divide(10, 5) =", divide(10, 5))


if __name__ == "__main__":
    main()
