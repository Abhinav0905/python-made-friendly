"""Solutions for the Chapter 29 exercises."""

from collections import deque


def q01_first_negative(numbers):
    """Return the first negative number, or ``None`` when none exists."""
    for number in numbers:
        if number < 0:
            return number
    return None


def q02_contains_duplicates(items):
    """Detect an equal pair without using a set."""
    seen = []
    for item in items:
        if item in seen:
            return True
        seen.append(item)
    return False


def q03_count_vowels(text):
    """Count vowels with one generator expression."""
    return sum(1 for character in text.lower() if character in "aeiou")


def q04_index_of_max(numbers):
    """Return the first maximum's index, or ``None`` for empty input."""
    if not numbers:
        return None
    maximum_index = 0
    for index in range(1, len(numbers)):
        if numbers[index] > numbers[maximum_index]:
            maximum_index = index
    return maximum_index


def q05_find_all(items, target):
    """Return every index at which *target* occurs."""
    return [index for index, item in enumerate(items) if item == target]


def q06_pairs_summing_to(items, target):
    """Yield occurrence pairs ``(a, b)`` where ``a < b`` and the sum matches."""
    for index, first in enumerate(items):
        for second in items[index + 1:]:
            if first < second and first + second == target:
                yield first, second


def q07_group_consecutive(items):
    """Return ``(value, count)`` tuples for equal consecutive runs."""
    iterator = iter(items)
    try:
        current = next(iterator)
    except StopIteration:
        return []
    count = 1
    result = []
    for item in iterator:
        if item == current:
            count += 1
        else:
            result.append((current, count))
            current = item
            count = 1
    result.append((current, count))
    return result


def q08_flatten(nested):
    """Recursively flatten lists while treating non-list objects as values."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(q08_flatten(item))
        else:
            result.append(item)
    return result


def q09_longest_increasing_run(numbers):
    """Return the first longest contiguous strictly increasing run."""
    if not numbers:
        return []
    best_start = current_start = 0
    best_length = 1
    for index in range(1, len(numbers)):
        if numbers[index] > numbers[index - 1]:
            current_length = index - current_start + 1
            if current_length > best_length:
                best_start = current_start
                best_length = current_length
        else:
            current_start = index
    return list(numbers[best_start:best_start + best_length])


def q10_moving_average(numbers, window):
    """Yield each full sliding-window average in constant extra space."""
    if window <= 0:
        raise ValueError("window must be positive")
    values = deque(maxlen=window)
    running_total = 0
    for number in numbers:
        if len(values) == window:
            running_total -= values[0]
        values.append(number)
        running_total += number
        if len(values) == window:
            yield running_total / window


if __name__ == "__main__":
    print(q01_first_negative([3, 5, -2, 7, -8]))
    print(q07_group_consecutive([1, 1, 2, 3, 3, 3, 1]))
    print(list(q10_moving_average([1, 2, 3, 4, 5], 3)))
