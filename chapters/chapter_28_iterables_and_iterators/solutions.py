"""Solutions for the Chapter 28 exercises."""

from collections import deque
from itertools import chain, count, islice


def q01_step_characters(text="hello"):
    """Collect characters by repeatedly calling ``next`` on an iterator."""
    iterator = iter(text)
    characters = []
    while True:
        try:
            characters.append(next(iterator))
        except StopIteration:
            return characters


def q02_sum_of_squares():
    """Return the sum of squares from 1 through 10 using a generator."""
    return sum(number ** 2 for number in range(1, 11))


def q03_chain_iterator():
    """Return one iterator over a list, tuple, and string."""
    return chain([1, 2, 3], (4, 5), "abc")


def q04_evens_up_to(n):
    """Yield even numbers from zero through *n*, inclusive."""
    for number in range(0, n + 1, 2):
        yield number


def q05_fibonacci():
    """Yield the Fibonacci sequence forever, beginning with zero."""
    first, second = 0, 1
    while True:
        yield first
        first, second = second, first + second


def q06_running_sum(iterable):
    """Yield the cumulative sum after each input value."""
    total = 0
    for value in iterable:
        total += value
        yield total


def q07_error_lines(filename):
    """Yield newline-stripped file lines containing uppercase ``ERROR``."""
    with open(filename, encoding="utf-8") as log_file:
        for line in log_file:
            if "ERROR" in line:
                yield line.rstrip("\r\n")


def q08_first_hundred_multiples_of_seven():
    """Return an iterator over 7, 14, ... 700."""
    return islice(count(7, 7), 100)


def q09_group(iterable, size):
    """Yield tuples of at most *size* items from *iterable*."""
    if size <= 0:
        raise ValueError("size must be positive")
    iterator = iter(iterable)
    while True:
        group = tuple(islice(iterator, size))
        if not group:
            return
        yield group


def q10_window(iterable, size):
    """Yield each complete sliding window as a tuple."""
    if size <= 0:
        raise ValueError("size must be positive")
    iterator = iter(iterable)
    buffer = deque(islice(iterator, size), maxlen=size)
    if len(buffer) < size:
        return
    yield tuple(buffer)
    for item in iterator:
        buffer.append(item)
        yield tuple(buffer)


if __name__ == "__main__":
    print(q01_step_characters())
    print(list(islice(q05_fibonacci(), 20)))
    print(list(q10_window([1, 2, 3, 4, 5], 3)))
