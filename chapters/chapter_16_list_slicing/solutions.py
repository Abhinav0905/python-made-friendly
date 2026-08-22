"""Worked exercises for Chapter 16."""

from typing import List, Sequence, Tuple, TypeVar, Union


T = TypeVar("T")


def q01_slice_views() -> Tuple[List[int], List[int], List[int], List[int]]:
    """Return the first three, last two, alternating and reversed views."""
    values = [10, 20, 30, 40, 50]
    return values[:3], values[-2:], values[::2], values[::-1]


def q02_string_segments(text: str = "programming") -> Tuple[str, str, str]:
    """Extract ``gram``, ``prog`` and reverse-tail ``gni`` with slices."""
    return text[3:7], text[:4], text[-1:-4:-1]


def q03_reverse_list(values: Sequence[T]) -> List[T]:
    """Return a reversed list copy using a negative-step slice."""
    return list(values)[::-1]


def q04_first_n_last_n(values: Sequence[T], count: int) -> List[T]:
    """Return the first *count* and last *count* values with no middle."""
    if not isinstance(count, int):
        raise TypeError("count must be an integer")
    if count < 0:
        raise ValueError("count must not be negative")
    if count == 0:
        return []
    copied = list(values)
    return copied[:count] + copied[-count:]


def q05_remove_every_other(values: Sequence[T]) -> List[T]:
    """Return a copy after deleting positions 1, 3, 5 and so on."""
    copied = list(values)
    del copied[1::2]
    return copied


def q06_chunk(values: Sequence[T], size: int) -> List[List[T]]:
    """Split a sequence into consecutive list chunks of positive *size*."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size <= 0:
        raise ValueError("size must be positive")
    copied = list(values)
    return [copied[index:index + size] for index in range(0, len(copied), size)]


def q07_interleave(first: Sequence[T], second: Sequence[T]) -> List[T]:
    """Interleave two equal-length sequences through extended slice assignment."""
    if len(first) != len(second):
        raise ValueError("the two sequences must have equal length")
    result = [None] * (len(first) + len(second))  # type: List[Union[T, None]]
    result[::2] = first
    result[1::2] = second
    return list(result)  # type: ignore


def q08_is_palindrome(value: Union[str, Sequence[T]]) -> bool:
    """Check palindrome form by comparing a sequence with its reverse."""
    if isinstance(value, str):
        folded = value.casefold()
        return folded == folded[::-1]
    copied = list(value)
    return copied == copied[::-1]


def q09_reverse_words(text: str) -> str:
    """Return the whitespace-separated words in reverse order."""
    return " ".join(text.split()[::-1])


def main() -> None:
    """Print a small demonstration."""
    print(q01_slice_views())
    print(q02_string_segments())
    print(q03_reverse_list([1, 2, 3]))
    print(q04_first_n_last_n([1, 2, 3, 4, 5, 6, 7, 8], 2))
    print(q05_remove_every_other(list(range(10))))
    print(q06_chunk([1, 2, 3, 4, 5, 6, 7], 3))
    print(q07_interleave([1, 3, 5, 7], [2, 4, 6, 8]))
    print(q08_is_palindrome("Racecar"))
    print(q09_reverse_words("hello world python"))


if __name__ == "__main__":
    main()
