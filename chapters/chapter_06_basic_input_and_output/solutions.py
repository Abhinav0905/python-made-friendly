"""Solutions to the Chapter 6 exercises."""

import math
from typing import Callable, NamedTuple, Tuple


class BmiResult(NamedTuple):
    """A calculated BMI and its category."""

    value: float
    category: str


def _required_text(value: str, field_name: str) -> str:
    if not isinstance(value, str):
        raise TypeError("{} must be a string".format(field_name))
    cleaned = value.strip()
    if not cleaned:
        raise ValueError("{} cannot be empty".format(field_name))
    return cleaned


def _finite_number(value: float, field_name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError("{} must be a number".format(field_name))
    result = float(value)
    if not math.isfinite(result):
        raise ValueError("{} must be finite".format(field_name))
    return result


def build_greeting(first_name: str, last_name: str) -> str:
    """Return the greeting from exercise 1."""
    first = _required_text(first_name, "first_name")
    last = _required_text(last_name, "last_name")
    return "Hello, {} {}! Nice to meet you.".format(first, last)


def greeting_from_input(
    input_function: Callable[[str], str] = input,
) -> str:
    """Ask for first and last names, then return the complete greeting."""
    first = input_function("First name? ")
    last = input_function("Last name? ")
    return build_greeting(first, last)


def bmi_with_category(weight_kg: float, height_m: float) -> BmiResult:
    """Calculate adult BMI and select the category used in the chapter."""
    weight = _finite_number(weight_kg, "weight_kg")
    height = _finite_number(height_m, "height_m")
    if weight <= 0:
        raise ValueError("weight_kg must be greater than zero")
    if height <= 0:
        raise ValueError("height_m must be greater than zero")

    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "underweight"
    elif bmi < 25:
        category = "normal weight"
    elif bmi < 30:
        category = "overweight"
    else:
        category = "obese"
    return BmiResult(bmi, category)


def format_bmi(result: BmiResult) -> str:
    """Format a BMI result as the two lines printed by the exercise."""
    if not isinstance(result, BmiResult):
        raise TypeError("result must be a BmiResult")
    return "Your BMI is {:.1f}\nCategory: {}".format(result.value, result.category)


def bmi_from_input(
    input_function: Callable[[str], str] = input,
) -> BmiResult:
    """Read BMI inputs, preserving ``float`` conversion errors."""
    weight = float(input_function("Weight in kilograms? "))
    height = float(input_function("Height in meters? "))
    return bmi_with_category(weight, height)


def average_of_three(line: str) -> float:
    """Parse exactly three whitespace-separated numbers and average them."""
    if not isinstance(line, str):
        raise TypeError("line must be a string")
    parts = line.split()
    if len(parts) != 3:
        raise ValueError("please enter exactly three numbers")

    first_text, second_text, third_text = parts
    first = float(first_text)
    second = float(second_text)
    third = float(third_text)
    if (
        not math.isfinite(first)
        or not math.isfinite(second)
        or not math.isfinite(third)
    ):
        raise ValueError("all three numbers must be finite")
    return (first + second + third) / 3


def average_from_input(
    input_function: Callable[[str], str] = input,
) -> float:
    """Read one line and return the average of the three numbers on it."""
    line = input_function("Enter three numbers separated by spaces: ")
    return average_of_three(line)


def read_redirected_profile(
    input_function: Callable[[str], str] = input,
) -> Tuple[str, str, str]:
    """Read the three lines used in the redirection experiment.

    ``EOFError`` is intentionally not caught. When a redirected file supplies
    fewer than three lines, callers see the same clear failure as ``input()``.
    """
    name = input_function("Name? ")
    age = input_function("Age? ")
    city = input_function("City? ")
    return name, age, city


def format_profile(profile: Tuple[str, str, str]) -> str:
    """Format the three values read by ``read_redirected_profile``."""
    if len(profile) != 3:
        raise ValueError("profile must contain name, age, and city")
    name, age, city = profile
    return "{} is {} and lives in {}.".format(name, age, city)


def q01_build_greeting(first_name: str, last_name: str) -> str:
    """Return the solution for Exercise 1."""
    return build_greeting(first_name, last_name)


def q02_bmi_with_category(weight_kg: float, height_m: float) -> BmiResult:
    """Return the solution for Exercise 2."""
    return bmi_with_category(weight_kg, height_m)


def q03_average_of_three(line: str) -> float:
    """Return the solution for Exercise 3."""
    return average_of_three(line)


def q04_read_redirected_profile(
    input_function: Callable[[str], str] = input,
) -> Tuple[str, str, str]:
    """Return the solution for Exercise 4."""
    return read_redirected_profile(input_function)


def main() -> None:
    """Run the interactive exercises."""
    print(greeting_from_input())
    print(format_bmi(bmi_from_input()))
    print("The average is {:.2f}".format(average_from_input()))


if __name__ == "__main__":
    main()
