"""Solutions for the Chapter 18 exercises."""

from collections import namedtuple
from math import hypot


Person = namedtuple("Person", ["name", "age", "email"])
Rectangle = namedtuple("Rectangle", ["width", "height"])


def q01_prime_tuple_details():
    """Return the tuple, its second and last values, and its length."""
    primes = (2, 3, 5, 7, 11)
    return primes, primes[1], primes[-1], len(primes)


def q02_unpack_person(person):
    """Unpack and return a three-value person tuple."""
    name, age, job = person
    return name, age, job


def q03_swap(first, second):
    """Swap two values through tuple packing and unpacking."""
    first, second = second, first
    return first, second


def q04_manual_stats(numbers):
    """Return minimum, maximum, and average without min, max, or sum."""
    if not numbers:
        return None, None, None
    low = high = numbers[0]
    total = 0
    for number in numbers:
        if number < low:
            low = number
        if number > high:
            high = number
        total += number
    return low, high, total / len(numbers)


def q05_format_scores(records):
    """Return name-score rows with names aligned to the widest name."""
    records = list(records)
    width = max((len(name) for name, _ in records), default=0)
    return ["{:<{}}  {}".format(name, width, score) for name, score in records]


def q06_name_email_pairs(people):
    """Return each named tuple's name and email."""
    return [(person.name, person.email) for person in people]


def q07_rank_scores(records):
    """Sort by descending score and then ascending name."""
    return sorted(records, key=lambda record: (-record[1], record[0]))


def q08_extended_unpack(items):
    """Return the first two items, middle list, and last item."""
    if len(items) <= 5:
        raise ValueError("items must contain more than five values")
    first, second, *middle, last = items
    return first, second, middle, last


def q09_farthest_points(points):
    """Return the first farthest point pair and their Euclidean distance."""
    if len(points) < 2:
        raise ValueError("at least two points are required")
    best_pair = (points[0], points[1])
    best_distance = hypot(points[1][0] - points[0][0], points[1][1] - points[0][1])
    for index, first in enumerate(points):
        for second in points[index + 1:]:
            distance = hypot(second[0] - first[0], second[1] - first[1])
            if distance > best_distance:
                best_pair = (first, second)
                best_distance = distance
    return best_pair[0], best_pair[1], best_distance


def q10_rectangle_area(rectangle):
    """Return a rectangle's area."""
    return rectangle.width * rectangle.height


def q10_rectangle_perimeter(rectangle):
    """Return a rectangle's perimeter."""
    return 2 * (rectangle.width + rectangle.height)


if __name__ == "__main__":
    print(q01_prime_tuple_details())
    print(q02_unpack_person(("Alice", 30, "Engineer")))
    print(q09_farthest_points([(0, 0), (3, 4), (1, 1)]))
