"""Worked exercises for Chapter 1."""

import sys
from typing import Sequence, Tuple


def q01_multiply_15_by_23() -> int:
    """Return the result of the REPL expression from exercise 1."""
    return 15 * 23


def q02_greet_me(me: str) -> str:
    """Return a greeting for the value assigned to ``me``."""
    return "Hello, " + me


def q03_hello_with_color(name: str, color: str) -> Tuple[str, str, str]:
    """Return the three output lines from the extended ``hello.py``."""
    return (
        "Hello, " + name,
        "Your favorite color is " + color,
        "Welcome to Python.",
    )


def q04_python_version_is_supported(
    version: Sequence[int] = sys.version_info,
) -> bool:
    """Return whether *version* is Python 3.8 or newer."""
    if len(version) < 2:
        raise ValueError("version must contain major and minor numbers")
    return tuple(version[:2]) >= (3, 8)


def main() -> None:
    """Print a non-interactive sample of all four exercises."""
    print(q01_multiply_15_by_23())
    print(q02_greet_me("Ada"))
    for line in q03_hello_with_color("Ada", "blue"):
        print(line)
    print("Python 3.8 or newer:", q04_python_version_is_supported())


if __name__ == "__main__":
    main()
