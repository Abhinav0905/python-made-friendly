"""Worked exercises for Chapter 15."""

import copy
from typing import Dict, Iterable, List, Sequence, Tuple, TypeVar


T = TypeVar("T")


def q01_first_middle_last() -> Tuple[List[int], Tuple[int, int, int]]:
    """Return the first ten positive integers and three indexed values."""
    numbers = list(range(1, 11))
    return numbers, (numbers[0], numbers[4], numbers[-1])


def q02_sorted_names(
    names: Sequence[str] = (
        "Peterson, Sylvia",
        "Mark, Melanie",
        "Diane, Matthew",
        "Johnson, Maryann",
        "Henry, Marie",
    ),
) -> Tuple[List[str], List[str]]:
    """Return an unchanged list copy and a separate alphabetically sorted copy."""
    original = list(names)
    return original, sorted(original)


def q03_modify_list() -> List[List[int]]:
    """Return snapshots after append, insert and remove operations."""
    numbers = [5, 1, 4, 2, 8]
    states = []
    numbers.append(3)
    states.append(numbers.copy())
    numbers.insert(0, 7)
    states.append(numbers.copy())
    numbers.remove(4)
    states.append(numbers.copy())
    return states


def q04_number_statistics(numbers: Sequence[int]) -> Dict[str, float]:
    """Return smallest, largest, average and median for ten positive integers."""
    if len(numbers) != 10:
        raise ValueError("exactly ten integers are required")
    for number in numbers:
        if not isinstance(number, int) or isinstance(number, bool):
            raise TypeError("all values must be integers")
        if number <= 0:
            raise ValueError("all integers must be positive")
    ordered = sorted(numbers)
    median = (ordered[4] + ordered[5]) / 2
    return {
        "smallest": min(numbers),
        "largest": max(numbers),
        "average": sum(numbers) / len(numbers),
        "median": median,
    }


def q05_long_words(words: Iterable[str]) -> List[str]:
    """Return words containing more than five characters."""
    long_words = []
    for word in words:
        if len(word) > 5:
            long_words.append(word)
    return long_words


def q06_sort_words(words: Iterable[str]) -> List[str]:
    """Sort longest first and alphabetically among words of equal length."""
    return sorted(words, key=lambda word: (-len(word), word))


def q07_remove_duplicates(values: Iterable[T]) -> List[T]:
    """Remove repeated values with a helper list while preserving first occurrence."""
    unique = []
    for value in values:
        if value not in unique:
            unique.append(value)
    return unique


def q08_rotate(values: Sequence[T], positions: int) -> List[T]:
    """Return a left-rotated copy; a negative count rotates right."""
    if not isinstance(positions, int):
        raise TypeError("positions must be an integer")
    copied = list(values)
    if not copied:
        return copied
    offset = positions % len(copied)
    return copied[offset:] + copied[:offset]


def q09_second_largest_unique(numbers: Iterable[float]) -> float:
    """Return the second-largest distinct numeric value."""
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    unique.sort(reverse=True)
    if len(unique) < 2:
        raise ValueError("at least two distinct values are required")
    return unique[1]


def q10_copy_trap() -> Dict[str, List[List[int]]]:
    """Return snapshots that contrast a shallow copy with a deep copy."""
    shallow_original = [[1, 2], [3, 4], [5, 6]]
    shallow = shallow_original.copy()
    shallow[0][0] = 99

    deep_original = [[1, 2], [3, 4], [5, 6]]
    deep = copy.deepcopy(deep_original)
    deep[0][0] = 99
    return {
        "shallow_original": shallow_original,
        "shallow_copy": shallow,
        "deep_original": deep_original,
        "deep_copy": deep,
    }


def main() -> None:
    """Print a small demonstration."""
    print(q01_first_middle_last())
    print(q02_sorted_names())
    print(q03_modify_list())
    print(q04_number_statistics(list(range(1, 11))))
    print(q05_long_words(["pear", "banana", "orange"]))
    print(q06_sort_words(["pear", "fig", "plum", "banana"]))
    print(q07_remove_duplicates([1, 2, 1, 3]))
    print(q08_rotate([1, 2, 3, 4, 5], 2))
    print(q09_second_largest_unique([10, 5, 10, 8, 3]))
    print(q10_copy_trap())


if __name__ == "__main__":
    main()
