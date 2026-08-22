"""Worked exercises for Chapter 13."""

from typing import Iterable, List, Tuple


def q01_equality_results() -> Tuple[bool, bool, bool, bool]:
    """Return the requested equality results."""
    return 5 == 5.0, "5" == 5, True == 1, [1, 2] == (1, 2)


def q02_between_1_and_100(number: float) -> bool:
    """Return whether *number* lies in the inclusive range 1 through 100."""
    return 1 <= number <= 100


def q03_is_weekday(day: str) -> bool:
    """Return whether *day* is one of the five requested abbreviations."""
    return day in ("Mon", "Tue", "Wed", "Thu", "Fri")


def q04_count_in_range(numbers: Iterable[float]) -> int:
    """Count values between 50 and 100 inclusive."""
    return sum(50 <= number <= 100 for number in numbers)


def q05_case_insensitive_equal(first: str, second: str) -> bool:
    """Compare two strings after Unicode-aware case folding."""
    return first.casefold() == second.casefold()


def q06_is_phrase_palindrome(text: str) -> bool:
    """Return whether alphanumeric text reads the same in both directions."""
    cleaned = "".join(character.casefold() for character in text if character.isalnum())
    return cleaned == cleaned[::-1]


def q07_chained_results() -> Tuple[bool, bool, bool, bool]:
    """Return the four chained-comparison predictions."""
    return 1 < 2 < 3, 1 < 2 > 0.5, True == 1 == 1.0, "abc" < "abd" < "abe"


def q08_is_registered(name: str, registered: Iterable[str]) -> bool:
    """Return whether *name* matches any registered name ignoring case."""
    folded_name = name.casefold()
    return any(folded_name == registered_name.casefold() for registered_name in registered)


def q09_vowels_present(sentence: str) -> List[str]:
    """Return distinct vowels found in alphabetical order."""
    lowered = sentence.casefold()
    vowels_found = []
    for vowel in "aeiou":
        if vowel in lowered:
            vowels_found.append(vowel)
    return vowels_found


def main() -> None:
    """Print a small demonstration."""
    print(q01_equality_results())
    print(q02_between_1_and_100(50), q03_is_weekday("Mon"))
    print(q04_count_in_range([45, 50, 75, 101]))
    print(q05_case_insensitive_equal("Straße", "STRASSE"))
    print(q06_is_phrase_palindrome("A man, a plan, a canal: Panama"))
    print(q07_chained_results())
    print(q08_is_registered("alice", ["Alice", "Bob"]))
    print(q09_vowels_present("The quick brown fox"))


if __name__ == "__main__":
    main()
