"""Solutions for the Chapter 24 exercises."""


def q01_area_of_rectangle(width, height):
    """Return the area of a rectangle."""
    return width * height


def q02_is_even(number):
    """Return whether *number* is even."""
    return number % 2 == 0


def q03_greet(name, greeting="Hello"):
    """Return a greeting for *name*."""
    return "{}, {}!".format(greeting, name)


def q04_word_count(text):
    """Return the number of whitespace-separated words in *text*."""
    return len(text.split())


def q05_max_of_three(first, second, third):
    """Return the largest of three values without calling ``max``."""
    largest = first
    if second > largest:
        largest = second
    if third > largest:
        largest = third
    return largest


def q06_safe_divide(numerator, denominator):
    """Return a quotient, or ``None`` when *denominator* is zero."""
    if denominator == 0:
        return None
    return numerator / denominator


def q07_buggy_add_student(name, roster=[]):
    """Deliberately demonstrate a shared mutable default."""
    roster.append(name)
    return roster


def q07_add_student(name, roster=None):
    """Add a student, creating a fresh default roster for every call."""
    if roster is None:
        roster = []
    roster.append(name)
    return roster


def q08_fibonacci(n):
    """Return the first *n* Fibonacci numbers.

    Parameters
    ----------
    n : int
        Number of values to return. It must not be negative.

    Returns
    -------
    list
        The sequence beginning with 0 and 1. Zero returns an empty list.
    """
    if n < 0:
        raise ValueError("n must not be negative")
    if n == 0:
        return []
    if n == 1:
        return [0]
    result = [0, 1]
    for _ in range(2, n):
        result.append(result[-1] + result[-2])
    return result


def q09_is_prime(n: int) -> bool:
    """Return whether *n* is a positive prime number."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def q10_apply_n_times(function, value, n):
    """Apply a one-argument function to a value *n* times."""
    if n < 0:
        raise ValueError("n must not be negative")
    result = value
    for _ in range(n):
        result = function(result)
    return result


if __name__ == "__main__":
    print(q03_greet("Ada"))
    print(q08_fibonacci(10))
    print(q10_apply_n_times(lambda value: value * 2, 1, 5))
