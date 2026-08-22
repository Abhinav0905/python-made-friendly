"""Literal Chapter 12 match solution. Requires Python 3.10 or newer."""


def q06_days_in_month_match(month):
    """Return a non-leap-year month's day count with match/case."""
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31
        case 4 | 6 | 9 | 11:
            return 30
        case 2:
            return 28
        case _:
            raise ValueError("month must be in the range 1 through 12")
