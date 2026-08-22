"""Worked exercises for Chapter 37: The __name__ Special Variable."""

import math
import re
import shlex
import subprocess
import sys
from collections import Counter
from pathlib import Path


def q01_mymod_path():
    """Return the path of the Exercise 1 module that prints ``__name__``."""
    return Path(__file__).parent / "examples" / "mymod.py"


def q02_observe_name_modes(module_path=None):
    """Run a module directly and import it, returning both output strings."""
    path = (
        Path(module_path).resolve()
        if module_path is not None
        else q01_mymod_path().resolve()
    )
    if not path.stem.isidentifier():
        raise ValueError("module filename must be a valid Python identifier")
    direct = subprocess.run(
        [sys.executable, str(path)],
        cwd=str(path.parent),
        check=True,
        text=True,
        capture_output=True,
    )
    imported = subprocess.run(
        [sys.executable, "-c", f"import {path.stem}"],
        cwd=str(path.parent),
        check=True,
        text=True,
        capture_output=True,
    )
    return direct.stdout.strip(), imported.stdout.strip()


def q03_is_prime(number):
    """Return whether an integer is prime, using exact integer square roots."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for divisor in range(3, math.isqrt(number) + 1, 2):
        if number % divisor == 0:
            return False
    return True


def q03_first_primes(count=10):
    """Return the first ``count`` prime numbers."""
    if count < 0:
        raise ValueError("count cannot be negative")
    primes = []
    candidate = 2
    while len(primes) < count:
        if q03_is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes


def q04_primes_main(output_fn=print):
    """Print and return the list used by the guarded ``primes.py`` entry point."""
    primes = q03_first_primes(10)
    output_fn(f"First 10 primes: {primes}")
    return primes


def q05_add(a, b):
    return a + b


def q05_subtract(a, b):
    return a - b


def q05_multiply(a, b):
    return a * b


def q05_divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


_OPERATIONS = {
    "+": q05_add,
    "-": q05_subtract,
    "*": q05_multiply,
    "/": q05_divide,
}


def q05_calculate_expression(expression):
    """Evaluate a three-token calculator expression."""
    tokens = shlex.split(expression) if isinstance(expression, str) else list(expression)
    if len(tokens) != 3:
        raise ValueError("expression must be NUM OP NUM")
    first_text, operator, second_text = tokens
    if operator not in _OPERATIONS:
        raise ValueError(f"unknown operator: {operator}")
    return _OPERATIONS[operator](float(first_text), float(second_text))


def q06_celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def q06_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def q06_convert(temperature, unit):
    """Convert from unit ``C`` or ``F`` and return ``(value, output_unit)``."""
    unit = unit.upper()
    if unit == "C":
        return q06_celsius_to_fahrenheit(float(temperature)), "F"
    if unit == "F":
        return q06_fahrenheit_to_celsius(float(temperature)), "C"
    raise ValueError("unit must be C or F")


def q07_mean(data):
    if not data:
        raise ValueError("mean needs at least one value")
    return sum(data) / len(data)


def q07_median(data):
    if not data:
        raise ValueError("median needs at least one value")
    ordered = sorted(data)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def q07_stdev(data):
    if len(data) < 2:
        raise ValueError("stdev needs at least two values")
    average = q07_mean(data)
    squared_differences = sum((value - average) ** 2 for value in data)
    return math.sqrt(squared_differences / (len(data) - 1))


def q07_file_stats(path):
    """Read one number per nonblank line and return mean, median, stdev."""
    with open(path, "r", encoding="utf-8") as input_file:
        values = [float(line) for line in input_file if line.strip()]
    return q07_mean(values), q07_median(values), q07_stdev(values)


_LOG_LINE = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s+\S+\s+\S+\s+'
    r'\[[^]]+\]\s+"(?P<method>[A-Z]+)\s+'
    r'(?P<path>\S+)\s+[^\"]+"\s+(?P<status>\d{3})\b'
)


def q08_parse_line(line):
    """Parse a common-format web log line into a dictionary or ``None``."""
    match = _LOG_LINE.search(line)
    return match.groupdict() if match else None


def q08_summarize_log(path):
    """Count parsed requests by IP address and status code."""
    ips = Counter()
    statuses = Counter()
    with open(path, "r", encoding="utf-8") as input_file:
        for line in input_file:
            parsed = q08_parse_line(line)
            if parsed is not None:
                ips[parsed["ip"]] += 1
                statuses[parsed["status"]] += 1
    return ips, statuses


def q09_data_path(filename="data.txt", module_file=None):
    """Return a data path beside a module, independent of the current CWD."""
    location = Path(module_file) if module_file is not None else Path(__file__)
    return location.resolve().parent / filename


def q09_read_adjacent_data(filename="data.txt", module_file=None):
    return q09_data_path(filename, module_file).read_text(encoding="utf-8")


def q10_is_palindrome(text):
    """Ignore case and non-alphanumeric characters when checking text."""
    cleaned = "".join(character.lower() for character in text if character.isalnum())
    return cleaned == cleaned[::-1]


def q10_find_palindromes(words):
    return [word for word in words if q10_is_palindrome(word)]


def main():
    print("First 10 primes:", q03_first_primes())


if __name__ == "__main__":
    main()
