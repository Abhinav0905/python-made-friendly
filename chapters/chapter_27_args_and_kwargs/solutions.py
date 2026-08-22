"""Solutions for the Chapter 27 exercises."""

import time
from functools import wraps


def q01_average(*numbers):
    """Return the mean of any number of values, or ``None`` when empty."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def q02_show(**attributes):
    """Print each keyword argument in insertion order."""
    for name, value in attributes.items():
        print("{} = {}".format(name, value))


def _max_of_three(first, second, third):
    largest = first
    if second > largest:
        largest = second
    if third > largest:
        largest = third
    return largest


def q03_max_from_sequence(values):
    """Unpack exactly three values into a largest-of-three call."""
    if len(values) != 3:
        raise ValueError("values must contain exactly three items")
    return _max_of_three(*values)


def q04_tag(name, **attrs):
    """Return an HTML-like opening tag with quoted attributes."""
    pairs = ['{}="{}"'.format(key, value) for key, value in attrs.items()]
    if not pairs:
        return "<{}>".format(name)
    return "<{} {}>".format(name, " ".join(pairs))


def q05_make_person(name, *, age, email):
    """Return a person dictionary with required keyword-only fields."""
    return {"name": name, "age": age, "email": email}


def q06_summarize(*items, separator=", ", prefix="", suffix=""):
    """Join string forms of *items* and wrap the result."""
    body = separator.join(str(item) for item in items)
    return "{}{}{}".format(prefix, body, suffix)


def q07_log_and_call(function, *args, **kwargs):
    """Print a call description and result, then return the result."""
    print("Calling {}(*{}, **{})".format(function.__name__, args, kwargs))
    result = function(*args, **kwargs)
    print("Result: {}".format(result))
    return result


def q08_call_all(functions, *args, **kwargs):
    """Call every function with the same forwarded arguments."""
    return [function(*args, **kwargs) for function in functions]


def q09_timing(function, clock=time.perf_counter):
    """Decorate a function to print its execution time and preserve metadata."""
    @wraps(function)
    def wrapper(*args, **kwargs):
        start = clock()
        result = function(*args, **kwargs)
        elapsed = clock() - start
        print("{} took {:.6f} seconds".format(function.__name__, elapsed))
        return result

    return wrapper


if __name__ == "__main__":
    print(q01_average(1, 2, 3, 4, 5))
    print(q04_tag("a", href="https://example.com", id="home"))

    @q09_timing
    def demo(value):
        return value * 2

    print(demo(5))
