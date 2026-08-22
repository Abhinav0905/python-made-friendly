"""Worked exercises for Chapter 12."""

import math
from typing import Tuple


def q01_number_sign(number: float) -> str:
    """Classify a number with an if/elif/else chain."""
    if number > 0:
        return "positive"
    if number < 0:
        return "negative"
    return "zero"


def q02_is_leap_year(year: int) -> bool:
    """Classify a Gregorian year with ordered conditional branches."""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def q03_number_sign_expression(number: float) -> str:
    """Classify a number with a nested conditional expression."""
    return "positive" if number > 0 else ("negative" if number < 0 else "zero")


def q04_triangle_type(a: float, b: float, c: float) -> str:
    """Validate three lengths and return the triangle's type."""
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
        return "not a triangle"
    if a == b == c:
        return "equilateral"
    if a == b or a == c or b == c:
        return "isosceles"
    return "scalene"


def q05_bmi_category(weight_kg: float, height_m: float) -> Tuple[float, str]:
    """Return BMI and its category after validating positive measurements."""
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if height_m <= 0:
        raise ValueError("height must be positive")
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        category = "underweight"
    elif bmi < 25:
        category = "normal weight"
    elif bmi < 30:
        category = "overweight"
    else:
        category = "obese"
    return bmi, category


def q06_days_in_month(month: int) -> int:
    """Return the days in a month of a non-leap year."""
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month in (4, 6, 9, 11):
        return 30
    if month == 2:
        return 28
    raise ValueError("month must be in the range 1 through 12")


def q07_rock_paper_scissors(player_1: str, player_2: str) -> str:
    """Return the result for two validated rock-paper-scissors choices."""
    wins_against = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    first = player_1.strip().casefold()
    second = player_2.strip().casefold()
    if first not in wins_against or second not in wins_against:
        raise ValueError("choices must be rock, paper, or scissors")
    if first == second:
        return "Tie!"
    if wins_against[first] == second:
        return "Player 1 wins!"
    return "Player 2 wins!"


def q08_integer_labels(number: int) -> Tuple[str, str, str, str]:
    """Return sign, parity, digit-count and primality labels."""
    sign = "positive" if number > 0 else "negative" if number < 0 else "zero"
    parity = "even" if number % 2 == 0 else "odd"
    digit_count = "single-digit" if abs(number) < 10 else "multi-digit"
    if number <= 1:
        primality = "neither prime nor composite"
    else:
        primality = "prime"
        for divisor in range(2, math.isqrt(number) + 1):
            if number % divisor == 0:
                primality = "composite"
                break
    return sign, parity, digit_count, primality


def q09_income_tax(income: float) -> float:
    """Return tax due under the exercise's three marginal brackets."""
    if income < 0:
        raise ValueError("income must not be negative")
    if income <= 10_000:
        return income * 0.10
    if income <= 40_000:
        return 10_000 * 0.10 + (income - 10_000) * 0.20
    return 10_000 * 0.10 + 30_000 * 0.20 + (income - 40_000) * 0.30


def main() -> None:
    """Print a small demonstration."""
    print(q01_number_sign(-2), q03_number_sign_expression(-2))
    print(q02_is_leap_year(2024))
    print(q04_triangle_type(3, 4, 5))
    print(q05_bmi_category(70, 1.75))
    print(q06_days_in_month(4))
    print(q07_rock_paper_scissors("rock", "scissors"))
    print(q08_integer_labels(17))
    print(q09_income_tax(50_000))


if __name__ == "__main__":
    main()
