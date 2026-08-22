"""Worked exercises for Chapter 4."""

import io
import itertools
import pydoc
import tokenize
from typing import Iterable, List, Tuple, TypeVar


T = TypeVar("T")


def q01_celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit.

    Parameters
    ----------
    celsius : float
        Temperature in degrees Celsius.

    Returns
    -------
    float
        Temperature in degrees Fahrenheit.

    Examples
    --------
    >>> q01_celsius_to_fahrenheit(0)
    32.0
    >>> q01_celsius_to_fahrenheit(100)
    212.0
    """
    return celsius * 9 / 5 + 32


def q02_help_for_temperature_function() -> str:
    """Return the text that Python's help system renders for exercise 1."""
    rendered = pydoc.render_doc(q01_celsius_to_fahrenheit, title="Help on %s")
    return pydoc.plain(rendered)


def q03_combinations_docstring() -> str:
    """Return the standard-library documentation for combinations."""
    return itertools.combinations.__doc__ or ""


def q03_combinations(values: Iterable[T], length: int) -> List[Tuple[T, ...]]:
    """Return all ordered-by-input combinations of the requested length."""
    if length < 0:
        raise ValueError("length must not be negative")
    return list(itertools.combinations(values, length))


def q04_collect_comments(source: str) -> List[Tuple[int, str]]:
    """Return ``(line_number, text)`` pairs for a manual comment audit.

    Deciding whether a comment explains *why* requires human context. This
    helper finds the comments without mistaking a ``#`` inside a string for one.
    """
    comments = []
    reader = io.StringIO(source).readline
    for token in tokenize.generate_tokens(reader):
        if token.type == tokenize.COMMENT:
            comments.append((token.start[0], token.string[1:].strip()))
    return comments


def main() -> None:
    """Print a small demonstration."""
    print(q01_celsius_to_fahrenheit(0))
    print(q02_help_for_temperature_function().splitlines()[0])
    print(q03_combinations("ABCD", 2))
    print(q04_collect_comments('value = "#1"  # external ids start at one\n'))


if __name__ == "__main__":
    main()
