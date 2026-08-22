"""Solutions for the Chapter 17 exercises."""


def q01_cubes():
    """Return the cubes of the integers 1 through 20."""
    return [number ** 3 for number in range(1, 21)]


def q02_uppercase(words):
    """Return a new list containing uppercase versions of *words*."""
    return [word.upper() for word in words]


def q03_divisible_by_seven():
    """Return the integers from 1 through 100 divisible by seven."""
    return [number for number in range(1, 101) if number % 7 == 0]


def q04_word_lengths(words):
    """Return ``(word, length)`` pairs for *words*."""
    return [(word, len(word)) for word in words]


def q05_non_positive_to_zero(numbers):
    """Keep positive numbers and replace every other value with zero."""
    return [number if number > 0 else 0 for number in numbers]


def q06_multiplication_table():
    """Return a 5 by 5 multiplication table for factors 1 through 5."""
    return [[row * column for column in range(1, 6)] for row in range(1, 6)]


def q07_words_from_sentences(sentences):
    """Return all whitespace-separated words from *sentences*."""
    return [word for sentence in sentences for word in sentence.split()]


def q08_pairs_less_than(xs, ys):
    """Return all cross-product pairs ``(x, y)`` for which ``x < y``."""
    return [(x, y) for x in xs for y in ys if x < y]


def q09_long_word_lengths(words):
    """Map words of length at least four to their lengths."""
    return {word: len(word) for word in words if len(word) >= 4}


def q10_exclusive_running_sums(numbers):
    """Return the sum of all preceding values at every input position."""
    result = []
    total = 0
    for number in numbers:
        result.append(total)
        total += number
    return result


if __name__ == "__main__":
    print(q01_cubes())
    print(q06_multiplication_table())
    print(q10_exclusive_running_sums([1, 2, 3, 4]))
