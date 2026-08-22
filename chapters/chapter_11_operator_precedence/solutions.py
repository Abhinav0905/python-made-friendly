"""Worked exercises for Chapter 11."""

from typing import Any, Tuple


def q01_precedence_results() -> Tuple[int, int, int, int]:
    """Return the results of the four introductory expressions."""
    return 5 + 2 * 3, (5 + 2) * 3, 10 - 4 - 2, 2 ** 3 ** 2


def q02_negative_square() -> int:
    """Return ``-3 ** 2`` using Python's normal precedence."""
    return -3 ** 2


def q03_grouped_expression(a: float, b: float, c: float, d: float, e: float) -> float:
    """Evaluate ``(a + (b * c)) - (d / e)``."""
    return (a + (b * c)) - (d / e)


def q04_average_forms(a: float, b: float, c: float) -> Tuple[float, float]:
    """Return the grouped average and its parenthesis-free rewrite."""
    return (a + b + c) / 3, a / 3 + b / 3 + c / 3


def q05_mixed_results() -> Tuple[bool, bool, bool, bool]:
    """Return the four mixed precedence and comparison results."""
    return 1 + 2 < 4, not 1 < 2, not 1 < 2 or 3 > 4, True == 1 == 1.0


def q06_compare_groupings(x: Any, y: Any, z: Any) -> Tuple[Any, Any]:
    """Return Python's grouping and the explicitly different grouping."""
    return x or y and z, (x or y) and z


def q07_evaluate_expression(
    a: float = 1,
    b: float = 2,
    c: float = 3,
    d: float = 8,
    e: float = 4,
) -> float:
    """Evaluate ``(a + (b * (c ** 2))) - (d / e)``."""
    return (a + (b * (c ** 2))) - (d / e)


def q08_chained_comparisons() -> Tuple[bool, bool]:
    """Return the two chained-comparison results."""
    return 1 < 2 < 3, True == True == True


def main() -> None:
    """Print a small demonstration."""
    print(q01_precedence_results())
    print(q02_negative_square())
    print(q03_grouped_expression(1, 2, 3, 8, 4))
    print(q04_average_forms(3, 6, 9))
    print(q05_mixed_results())
    print(q06_compare_groupings(True, False, False))
    print(q07_evaluate_expression())
    print(q08_chained_comparisons())


if __name__ == "__main__":
    main()
