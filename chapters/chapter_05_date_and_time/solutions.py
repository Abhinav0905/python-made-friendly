"""Solutions to the Chapter 5 exercises.

The functions accept dates, clocks, or limits as arguments so their results can
be checked without depending on the machine's current date or clock speed.
"""

from datetime import date, datetime
import time
from typing import Callable, Optional, Tuple


def _checked_date(value: date) -> date:
    """Return *value* when it is a date but not a datetime."""
    if not isinstance(value, date) or isinstance(value, datetime):
        raise TypeError("value must be a datetime.date object")
    return value


def format_current_date(current_date: Optional[date] = None) -> str:
    """Return a date such as ``Sunday, April 19, 2026``.

    Building the unpadded day with ``date.day`` works on Windows, macOS, and
    Linux. Platform-specific ``%-d`` and ``%#d`` format flags are not needed.
    """
    day = date.today() if current_date is None else _checked_date(current_date)
    return "{}, {} {}, {}".format(
        day.strftime("%A"), day.strftime("%B"), day.day, day.year
    )


def days_until_next_january_first(current_date: Optional[date] = None) -> int:
    """Return the number of calendar days until January 1 of the next year."""
    today = date.today() if current_date is None else _checked_date(current_date)
    next_new_year = date(today.year + 1, 1, 1)
    return (next_new_year - today).days


def parse_and_format_datetime(value: str) -> Tuple[datetime, str]:
    """Parse ``YYYY-MM-DD HH:MM`` and return the object and requested display.

    A malformed value raises ``ValueError``, just as ``datetime.strptime`` does.
    """
    if not isinstance(value, str):
        raise TypeError("value must be a string")

    parsed = datetime.strptime(value, "%Y-%m-%d %H:%M")
    hour = parsed.strftime("%I").lstrip("0") or "0"
    displayed = "{} {} {}, {}:{} {}".format(
        parsed.day,
        parsed.strftime("%b"),
        parsed.year,
        hour,
        parsed.strftime("%M"),
        parsed.strftime("%p"),
    )
    return parsed, displayed


def sum_integers_with_timing(
    limit: int = 1_000_000,
    clock: Callable[[], float] = time.perf_counter,
) -> Tuple[int, float]:
    """Sum ``1`` through *limit* with a loop and return total and elapsed time."""
    if isinstance(limit, bool) or not isinstance(limit, int):
        raise TypeError("limit must be an integer")
    if limit < 0:
        raise ValueError("limit must be zero or greater")
    if not callable(clock):
        raise TypeError("clock must be callable")

    started = clock()
    total = 0
    for number in range(1, limit + 1):
        total += number
    elapsed = clock() - started
    return total, elapsed


def q01_format_current_date(current_date: Optional[date] = None) -> str:
    """Return the solution for Exercise 1."""
    return format_current_date(current_date)


def q02_days_until_next_january_first(current_date: Optional[date] = None) -> int:
    """Return the solution for Exercise 2."""
    return days_until_next_january_first(current_date)


def q03_parse_and_format_datetime(value: str) -> Tuple[datetime, str]:
    """Return the solution for Exercise 3."""
    return parse_and_format_datetime(value)


def q04_sum_integers_with_timing(
    limit: int = 1_000_000,
    clock: Callable[[], float] = time.perf_counter,
) -> Tuple[int, float]:
    """Return the solution for Exercise 4."""
    return sum_integers_with_timing(limit, clock)


def main() -> None:
    """Run the four exercises with the values printed in the chapter."""
    print(format_current_date())
    print("Days until next January 1:", days_until_next_january_first())

    parsed, displayed = parse_and_format_datetime("2024-07-04 09:30")
    print("Parsed object:", repr(parsed))
    print("Formatted date:", displayed)

    total, elapsed = sum_integers_with_timing()
    print("Sum: {}, Time: {:.6f} s".format(total, elapsed))


if __name__ == "__main__":
    main()
