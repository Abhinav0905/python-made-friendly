"""Solutions for the Chapter 25 exercises."""

import random


def q01_double_in_place(numbers):
    """Double every list value in place and return ``None``."""
    for index in range(len(numbers)):
        numbers[index] *= 2


def q02_doubled(numbers):
    """Return doubled values in a new list."""
    return [number * 2 for number in numbers]


def q03_compare_doubling(numbers):
    """Return snapshots that expose mutation versus new-list behavior."""
    in_place_input = list(numbers)
    in_place_result = q01_double_in_place(in_place_input)
    new_list_input = list(numbers)
    new_list_result = q02_doubled(new_list_input)
    return in_place_input, in_place_result, new_list_input, new_list_result


def q04_remove_duplicates_in_place(items):
    """Remove duplicate hashable values in place, keeping first occurrences."""
    seen = set()
    write_index = 0
    for item in items:
        if item not in seen:
            seen.add(item)
            items[write_index] = item
            write_index += 1
    del items[write_index:]


def q05_split_at(items, value):
    """Return copies split immediately after the first occurrence of *value*."""
    try:
        index = items.index(value)
    except ValueError:
        return list(items), []
    return list(items[:index + 1]), list(items[index + 1:])


def q06_stats(numbers):
    """Return minimum, maximum, total, and average, or four ``None`` values."""
    if not numbers:
        return None, None, None, None
    low = high = numbers[0]
    total = 0
    for number in numbers:
        if number < low:
            low = number
        if number > high:
            high = number
        total += number
    return low, high, total, total / len(numbers)


def q07_partition(items, predicate):
    """Return items for which *predicate* is true and false, in order."""
    matching = []
    remaining = []
    for item in items:
        if predicate(item):
            matching.append(item)
        else:
            remaining.append(item)
    return matching, remaining


def q08_merge_sorted(first, second):
    """Merge two sorted sequences into a new sorted list."""
    result = []
    first_index = second_index = 0
    while first_index < len(first) and second_index < len(second):
        if first[first_index] <= second[second_index]:
            result.append(first[first_index])
            first_index += 1
        else:
            result.append(second[second_index])
            second_index += 1
    result.extend(first[first_index:])
    result.extend(second[second_index:])
    return result


def q09_shuffle_in_place(items, randint=random.randint):
    """Shuffle *items* in place with the Fisher-Yates algorithm."""
    for index in range(len(items) - 1, 0, -1):
        swap_index = randint(0, index)
        if not 0 <= swap_index <= index:
            raise ValueError("randint returned an index outside the requested range")
        items[index], items[swap_index] = items[swap_index], items[index]


if __name__ == "__main__":
    values = [1, 2, 3, 4]
    q01_double_in_place(values)
    print(values)
    print(q05_split_at([1, 2, 3, 4, 5], 3))
