"""Worked exercises for Chapter 14."""

import random
from typing import Iterable, List, Optional, Sequence, Tuple


def q01_numbers_1_to_20() -> List[int]:
    """Return 1 through 20 after building the result with a for loop."""
    numbers = []
    for number in range(1, 21):
        numbers.append(number)
    return numbers


def q02_sum_even_numbers() -> int:
    """Sum all even integers from 2 through 100 with a loop."""
    total = 0
    for number in range(2, 101, 2):
        total += number
    return total


def q03_powers_of_two(limit: int = 1000) -> List[int]:
    """Return positive powers of two strictly below *limit* with a while loop."""
    if limit <= 0:
        return []
    powers = []
    power = 1
    while power < limit:
        powers.append(power)
        power *= 2
    return powers


def q04_multiples_of_three_or_five(limit: int) -> List[int]:
    """Return integers from 1 through a positive limit divisible by 3 or 5."""
    if not isinstance(limit, int):
        raise TypeError("limit must be an integer")
    if limit <= 0:
        raise ValueError("limit must be positive")
    matches = []
    for number in range(1, limit + 1):
        if number % 3 == 0 or number % 5 == 0:
            matches.append(number)
    return matches


def q05_score_statistics(
    scores: Sequence[float] = (72, 88, 95, 61, 40, 79),
) -> Tuple[Tuple[float, float, float], Tuple[float, float, float]]:
    """Return ``(average, highest, lowest)`` from a loop and built-ins."""
    if not scores:
        raise ValueError("scores must not be empty")
    total = 0.0
    highest = scores[0]
    lowest = scores[0]
    for score in scores:
        total += score
        if score > highest:
            highest = score
        if score < lowest:
            lowest = score
    manual = total / len(scores), highest, lowest
    built_in = sum(scores) / len(scores), max(scores), min(scores)
    return manual, built_in


def q06_password_result(
    attempts: Iterable[str],
    password: str = "hunter2",
    max_attempts: int = 3,
) -> str:
    """Return access or lockout after at most *max_attempts* guesses."""
    if max_attempts <= 0:
        raise ValueError("max_attempts must be positive")
    for attempt_number, guess in enumerate(attempts, start=1):
        if attempt_number > max_attempts:
            break
        if guess == password:
            return "Access granted."
    return "Locked out."


def q07_multiplication_table(size: int = 10) -> List[str]:
    """Return a multiplication table whose numeric fields are five characters."""
    if size <= 0:
        raise ValueError("size must be positive")
    header = "     "
    for column in range(1, size + 1):
        header += "{:5}".format(column)
    lines = [header]
    lines.append("     " + "-" * (size * 5))
    for row in range(1, size + 1):
        cells = []
        for column in range(1, size + 1):
            cells.append("{:5}".format(row * column))
        lines.append("{:3} |".format(row) + "".join(cells))
    return lines


def q08_primes_up_to(limit: int) -> List[int]:
    """Return prime numbers through *limit* using nested trial-division loops."""
    if not isinstance(limit, int):
        raise TypeError("limit must be an integer")
    if limit <= 0:
        raise ValueError("limit must be positive")
    primes = []
    for number in range(2, limit + 1):
        is_prime = True
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return primes


def q09_numbered_words(words: Iterable[str]) -> List[str]:
    """Return one-based numbered lines for *words*."""
    numbered = []
    for index, word in enumerate(words, start=1):
        numbered.append("{}. {}".format(index, word))
    return numbered


def q10_guessing_game(
    guesses: Sequence[int],
    secret: Optional[int] = None,
) -> List[str]:
    """Return feedback for at most ten guesses, using a for/else result path."""
    if secret is None:
        secret = random.randint(1, 100)
    if not 1 <= secret <= 100:
        raise ValueError("secret must be between 1 and 100")
    messages = []
    for turn in range(1, 11):
        if turn > len(guesses):
            raise ValueError("supply ten guesses unless the secret is found earlier")
        guess = guesses[turn - 1]
        if not isinstance(guess, int) or not 1 <= guess <= 100:
            raise ValueError("every guess must be an integer between 1 and 100")
        if guess < secret:
            messages.append("Higher.")
        elif guess > secret:
            messages.append("Lower.")
        else:
            messages.append("Correct! The number was {}.".format(secret))
            break
    else:
        messages.append("Out of guesses. The number was {}.".format(secret))
    return messages


def main() -> None:
    """Print a small demonstration."""
    for number in q01_numbers_1_to_20():
        print(number)
    print(q02_sum_even_numbers())
    print(q03_powers_of_two())
    print(q04_multiples_of_three_or_five(20))
    print(q05_score_statistics())
    print(q06_password_result(["wrong", "hunter2"]))
    for line in q07_multiplication_table():
        print(line)
    print(q08_primes_up_to(30))
    print(q09_numbered_words(["apple", "banana"]))
    print(q10_guessing_game([25, 75, 50], secret=50))


if __name__ == "__main__":
    main()
