"""Worked exercises for Chapter 2."""

import math
from typing import Tuple, Type


def q01_literal_types() -> Tuple[Type[object], ...]:
    """Return the types of 42, 42.0, "42", and True."""
    return type(42), type(42.0), type("42"), type(True)


def q02_large_integer() -> int:
    """Return 2 raised to the 50th power."""
    return 2 ** 50


def q03_float_comparisons() -> Tuple[bool, bool]:
    """Return exact and tolerant comparisons of 0.1 + 0.2 with 0.3."""
    total = 0.1 + 0.2
    return total == 0.3, math.isclose(total, 0.3)


def q04_convert_and_add(text: str = "100") -> int:
    """Convert an integer string and add 25.

    ``int`` deliberately supplies the prompt's strict validation: malformed
    input raises ``ValueError`` rather than being guessed or silently changed.
    """
    return int(text) + 25


def q05_nonempty_string_is_truthy(text: str = "False") -> bool:
    """Return the truth value of a string; content does not affect the rule."""
    return bool(text)


def main() -> None:
    """Print sample results for the exercises."""
    print(q01_literal_types())
    print(q02_large_integer())
    print(q03_float_comparisons())
    print(q04_convert_and_add())
    print(q05_nonempty_string_is_truthy())


if __name__ == "__main__":
    main()
