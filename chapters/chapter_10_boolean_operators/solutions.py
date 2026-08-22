"""Worked exercises for Chapter 10."""

from typing import Any, Optional, Tuple


def q01_truth_table_checks() -> Tuple[bool, bool, bool, bool]:
    """Return the four requested truth-table results."""
    return True and False, True or False, not True, not (True and False)


def q02_is_between_zero_and_100(number: int) -> bool:
    """Return whether *number* is greater than 0 and less than 100."""
    return number > 0 and number < 100


def q03_last_truthy_value() -> str:
    """Return the result of ``0 or [] or None or 'last'``."""
    return 0 or [] or None or "last"


def q04_log_on(username: str, password: str) -> str:
    """Return the log-on message after treating whitespace-only fields as empty."""
    if username.strip() and password.strip():
        return "welcome"
    return "Both fields are required."


def q05_may_enter(has_ticket: bool, has_id: bool, is_minor: bool) -> bool:
    """Return whether the stated ticket and ID policy permits entry."""
    return has_ticket and (has_id or is_minor)


def q06_is_leap_year(year: int) -> bool:
    """Return whether *year* follows the Gregorian leap-year rule."""
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)


def q07_operand_results() -> Tuple[Any, ...]:
    """Return the six results whose output the exercise asks readers to predict."""
    return (
        10 and 20,
        10 or 20,
        [] or "hello",
        "hello" and "",
        None and print("hi"),
        0 or False or None or 0.0,
    )


def q08_display_name(user_name: Optional[str]) -> str:
    """Return a truthy user name, or the default display name."""
    return user_name or "Guest"


def main() -> None:
    """Print a small demonstration."""
    print(q01_truth_table_checks())
    print(q02_is_between_zero_and_100(42))
    print(q03_last_truthy_value())
    print(q04_log_on("Ada", "secret"))
    print(q05_may_enter(True, False, True))
    print(q06_is_leap_year(2024))
    print(q07_operand_results())
    print(q08_display_name(None))


if __name__ == "__main__":
    main()
