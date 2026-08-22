"""Solutions for the Chapter 26 exercises."""

from collections import Counter
from functools import partial, reduce
from itertools import chain


def q01_square_versions():
    """Return squares made with ``map`` and with a comprehension."""
    mapped = list(map(lambda number: number ** 2, range(1, 11)))
    comprehended = [number ** 2 for number in range(1, 11)]
    return mapped, comprehended


def q02_divisible_by_three_versions():
    """Return 1..50 multiples of three from ``filter`` and a comprehension."""
    filtered = list(filter(lambda number: number % 3 == 0, range(1, 51)))
    comprehended = [number for number in range(1, 51) if number % 3 == 0]
    return filtered, comprehended


def q03_word_checks(words):
    """Return ``any(len > 10)`` and ``all(len >= 3)`` results."""
    return any(len(word) > 10 for word in words), all(len(word) >= 3 for word in words)


def q04_even_integer_sum(strings):
    """Convert strings with ``map``, filter even integers, and sum them."""
    return sum(filter(lambda number: number % 2 == 0, map(int, strings)))


def q05_longest_with_reduce(strings):
    """Return the first longest string using ``reduce`` rather than ``max``."""
    if not strings:
        raise ValueError("at least one string is required")
    return reduce(lambda first, second: first if len(first) >= len(second) else second, strings)


def q06_score_pipeline(names, scores):
    """Build and filter scores once with ``zip`` and once with a comprehension."""
    if len(names) != len(scores):
        raise ValueError("names and scores must have equal lengths")
    zipped_mapping = dict(zip(names, scores))
    zipped_high_scores = list(filter(lambda item: item[1] > 80, zipped_mapping.items()))
    comprehended_mapping = {name: score for name, score in zip(names, scores)}
    comprehended_high_scores = list(
        filter(lambda item: item[1] > 80, comprehended_mapping.items())
    )
    return (
        (zipped_mapping, zipped_high_scores),
        (comprehended_mapping, comprehended_high_scores),
    )


def q07_compose(first, second):
    """Return ``h`` such that ``h(x) == first(second(x))``."""
    return lambda value: first(second(value))


def q08_process_numbers(numbers, threshold):
    """Purely deduplicate, keep values above *threshold*, and return their sum."""
    seen = set()
    unique = []
    for number in numbers:
        if number not in seen:
            seen.add(number)
            unique.append(number)
    filtered = [number for number in unique if number > threshold]
    return filtered, sum(filtered)


def q09_word_frequencies(lines):
    """Return lowercase word counts without an explicit loop over words."""
    words = chain.from_iterable(line.lower().split() for line in lines)
    return dict(Counter(words))


def q10_apply_discounts(*discounts, price):
    """Apply percentage discounts one after another to *price*."""
    def apply_one(running_price, discount):
        return running_price * (1 - discount / 100)

    return reduce(apply_one, discounts, price)


q10_student_discount = partial(q10_apply_discounts, 10)
q10_vip_discount = partial(q10_apply_discounts, 20, 5)


if __name__ == "__main__":
    print(q01_square_versions())
    print(q04_even_integer_sum(["10", "15", "20", "25", "30"]))
    print(q10_vip_discount(price=100))
