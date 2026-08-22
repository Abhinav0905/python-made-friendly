"""Solutions to the nine Chapter 8 exercises."""

import math
import time
from typing import Callable, Iterable, NamedTuple, Tuple


class DivisionResult(NamedTuple):
    """Floor quotient, remainder and reconstruction of the dividend."""

    quotient: int
    remainder: int
    reconstructed: int


class DiscountResult(NamedTuple):
    """Unrounded discount amount and final price."""

    saved: float
    final_price: float


class TemperatureResult(NamedTuple):
    """A Celsius input converted to three other scales."""

    fahrenheit: float
    kelvin: float
    rankine: float


class ModularTiming(NamedTuple):
    """Results and elapsed times for two modular-power methods."""

    pow_result: int
    pow_seconds: float
    direct_result: int
    direct_seconds: float

    @property
    def results_equal(self) -> bool:
        return self.pow_result == self.direct_result


def _integer(value: int, field_name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("{} must be an integer".format(field_name))
    return value


def _finite_number(value: float, field_name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError("{} must be a number".format(field_name))
    number = float(value)
    if not math.isfinite(number):
        raise ValueError("{} must be finite".format(field_name))
    return number


def floor_division_and_modulus(
    dividend: int = 100,
    divisor: int = 7,
) -> DivisionResult:
    """Return ``dividend // divisor``, ``dividend % divisor`` and their check."""
    left = _integer(dividend, "dividend")
    right = _integer(divisor, "divisor")
    if right == 0:
        raise ValueError("divisor cannot be zero")

    quotient, remainder = divmod(left, right)
    reconstructed = quotient * right + remainder
    return DivisionResult(quotient, remainder, reconstructed)


def trapezoid_area(side_a: float, side_b: float, height: float) -> float:
    """Return ``(side_a + side_b) * height / 2``."""
    a = _finite_number(side_a, "side_a")
    b = _finite_number(side_b, "side_b")
    h = _finite_number(height, "height")
    if a < 0 or b < 0 or h < 0:
        raise ValueError("sides and height cannot be negative")
    return (a + b) * h / 2


def maximum_absolute_value(values: Iterable[float]) -> float:
    """Return the largest magnitude, using ``abs``, ``min`` and ``max``."""
    if isinstance(values, (str, bytes)):
        raise TypeError("values must be an iterable of numbers")
    try:
        numbers = tuple(_finite_number(value, "each value") for value in values)
    except TypeError:
        raise TypeError("values must be an iterable of numbers")
    if not numbers:
        raise ValueError("values cannot be empty")

    smallest = min(numbers)
    largest = max(numbers)
    return max(abs(smallest), abs(largest))


def seconds_to_hms(total_seconds: int) -> Tuple[int, int, int]:
    """Split nonnegative seconds into hours, minutes and seconds with divmod."""
    total = _integer(total_seconds, "total_seconds")
    if total < 0:
        raise ValueError("total_seconds cannot be negative")
    hours, remainder = divmod(total, 3600)
    minutes, seconds = divmod(remainder, 60)
    return hours, minutes, seconds


def format_hms(total_seconds: int) -> str:
    """Format the result of exercise 4."""
    hours, minutes, seconds = seconds_to_hms(total_seconds)
    return "{}s = {}h {}m {}s".format(total_seconds, hours, minutes, seconds)


def three_digit_digits(number: int) -> Tuple[int, int, int]:
    """Return a positive three-digit integer's digits without string conversion."""
    value = _integer(number, "number")
    if value < 100 or value > 999:
        raise ValueError("number must be a positive three-digit integer")
    hundreds = value // 100
    tens = (value // 10) % 10
    units = value % 10
    return hundreds, tens, units


def discount_details(price: float, discount_percent: float) -> DiscountResult:
    """Calculate the amount saved and final price for a percentage discount."""
    original = _finite_number(price, "price")
    percent = _finite_number(discount_percent, "discount_percent")
    if original < 0:
        raise ValueError("price cannot be negative")
    if percent < 0 or percent > 100:
        raise ValueError("discount_percent must be between 0 and 100")

    saved = original * percent / 100
    return DiscountResult(saved, original - saved)


def format_discount(result: DiscountResult) -> str:
    """Format both discount values to two decimal places."""
    if not isinstance(result, DiscountResult):
        raise TypeError("result must be a DiscountResult")
    return "Amount saved: ${:.2f}\nFinal price:  ${:.2f}".format(
        result.saved, result.final_price
    )


def temperature_conversions(celsius: float) -> TemperatureResult:
    """Convert Celsius to Fahrenheit, Kelvin and Rankine."""
    value = _finite_number(celsius, "celsius")
    if value < -273.15:
        raise ValueError("celsius cannot be below absolute zero")

    fahrenheit = value * 9 / 5 + 32
    kelvin = value + 273.15
    rankine = fahrenheit + 459.67
    return TemperatureResult(fahrenheit, kelvin, rankine)


def format_temperatures(result: TemperatureResult) -> str:
    """Format all three converted temperatures with units."""
    if not isinstance(result, TemperatureResult):
        raise TypeError("result must be a TemperatureResult")
    return (
        "Fahrenheit: {:.2f} °F\n"
        "Kelvin:     {:.2f} K\n"
        "Rankine:    {:.2f} °R"
    ).format(result.fahrenheit, result.kelvin, result.rankine)


def sum_digits(number: int) -> int:
    """Return the digit sum of a positive integer using ``%`` and ``//``."""
    remaining = _integer(number, "number")
    if remaining <= 0:
        raise ValueError("number must be a positive integer")

    total = 0
    while remaining > 0:
        total += remaining % 10
        remaining //= 10
    return total


def compare_modular_exponentiation(
    base: int = 2,
    exponent: int = 1000,
    modulus: int = 10_000_007,
    clock: Callable[[], float] = time.perf_counter,
) -> ModularTiming:
    """Time three-argument ``pow`` and direct exponentiation followed by ``%``."""
    checked_base = _integer(base, "base")
    checked_exponent = _integer(exponent, "exponent")
    checked_modulus = _integer(modulus, "modulus")
    if checked_exponent < 0:
        raise ValueError("exponent cannot be negative")
    if checked_modulus <= 0:
        raise ValueError("modulus must be greater than zero")
    if not callable(clock):
        raise TypeError("clock must be callable")

    started = clock()
    pow_result = pow(checked_base, checked_exponent, checked_modulus)
    pow_seconds = clock() - started

    started = clock()
    direct_result = checked_base ** checked_exponent % checked_modulus
    direct_seconds = clock() - started
    return ModularTiming(pow_result, pow_seconds, direct_result, direct_seconds)


def q01_floor_division_and_modulus(
    dividend: int = 100,
    divisor: int = 7,
) -> DivisionResult:
    """Return the solution for Exercise 1."""
    return floor_division_and_modulus(dividend, divisor)


def q02_trapezoid_area(side_a: float, side_b: float, height: float) -> float:
    """Return the solution for Exercise 2."""
    return trapezoid_area(side_a, side_b, height)


def q03_maximum_absolute_value(values: Iterable[float]) -> float:
    """Return the solution for Exercise 3."""
    return maximum_absolute_value(values)


def q04_seconds_to_hms(total_seconds: int) -> Tuple[int, int, int]:
    """Return the solution for Exercise 4."""
    return seconds_to_hms(total_seconds)


def q05_three_digit_digits(number: int) -> Tuple[int, int, int]:
    """Return the solution for Exercise 5."""
    return three_digit_digits(number)


def q06_discount_details(price: float, discount_percent: float) -> DiscountResult:
    """Return the solution for Exercise 6."""
    return discount_details(price, discount_percent)


def q07_temperature_conversions(celsius: float) -> TemperatureResult:
    """Return the solution for Exercise 7."""
    return temperature_conversions(celsius)


def q08_sum_digits(number: int) -> int:
    """Return the solution for Exercise 8."""
    return sum_digits(number)


def q09_compare_modular_exponentiation(
    base: int = 2,
    exponent: int = 1000,
    modulus: int = 10_000_007,
    clock: Callable[[], float] = time.perf_counter,
) -> ModularTiming:
    """Return the solution for Exercise 9."""
    return compare_modular_exponentiation(base, exponent, modulus, clock)


def main() -> None:
    """Print one demonstration for each exercise."""
    division = floor_division_and_modulus()
    print("100 // 7 =", division.quotient)
    print("100 % 7 =", division.remainder)
    print("Reconstructed:", division.reconstructed)
    print("Trapezoid area:", trapezoid_area(8, 12, 5))
    print("Largest absolute value:", maximum_absolute_value([-7, 3, -2, 8, -10]))
    print(format_hms(7_381))
    print(*three_digit_digits(527), sep="\n")
    print(format_discount(discount_details(49.99, 15)))
    print(format_temperatures(temperature_conversions(25)))
    print("Sum of digits:", sum_digits(1234))

    timing = compare_modular_exponentiation()
    print(
        "pow(2, 1000, 10000007) = {} ({:.6f}s)".format(
            timing.pow_result, timing.pow_seconds
        )
    )
    print(
        "2 ** 1000 % 10000007   = {} ({:.6f}s)".format(
            timing.direct_result, timing.direct_seconds
        )
    )
    print("Results equal:", timing.results_equal)


if __name__ == "__main__":
    main()
