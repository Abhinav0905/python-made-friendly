"""Solutions to the Chapter 7 exercises."""

import math
import sys
import time
from typing import Callable, Optional, TextIO


def _nonnegative_integer(value: int, field_name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{field_name} must be an integer")
    if value < 0:
        raise ValueError(f"{field_name} must be zero or greater")
    return value


def _nonnegative_delay(value: float) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError("delay must be a number")
    delay = float(value)
    if not math.isfinite(delay) or delay < 0:
        raise ValueError("delay must be a finite, nonnegative number")
    return delay


def format_numbers_one_to_ten() -> str:
    """Return the numbers 1 through 10 separated by commas."""
    line = ""
    for number in range(1, 11):
        if line:
            line += ", "
        line += str(number)
    return line


def print_numbers_one_to_ten(stream: Optional[TextIO] = None) -> str:
    """Print exercise 1 with ``sep`` and return the line that was printed."""
    output = sys.stdout if stream is None else stream
    line = format_numbers_one_to_ten()
    print(*range(1, 11), sep=", ", file=output)
    return line


def format_money(amount: float) -> str:
    """Return an amount with a dollar sign, grouping and two decimals."""
    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        raise TypeError("amount must be a number")
    number = float(amount)
    if not math.isfinite(number):
        raise ValueError("amount must be finite")
    return f"${number:,.2f}"


def print_timed_dots(
    count: int = 40,
    delay: float = 0.1,
    stream: Optional[TextIO] = None,
    sleep_function: Callable[[float], None] = time.sleep,
) -> str:
    """Print flushed dots on one line, pausing after each dot.

    The stream and sleeper are arguments so the terminal behavior can be tested
    without making the test suite wait four seconds.
    """
    dot_count = _nonnegative_integer(count, "count")
    seconds = _nonnegative_delay(delay)
    if not callable(sleep_function):
        raise TypeError("sleep_function must be callable")

    output = sys.stdout if stream is None else stream
    for _ in range(dot_count):
        print(".", end="", file=output, flush=True)
        sleep_function(seconds)
    print(file=output)
    return "." * dot_count


def progress_bar_frame(completed: int, total: int, width: int = 10) -> str:
    """Build one progress-bar frame such as ``[#####.....] 50%``."""
    completed_steps = _nonnegative_integer(completed, "completed")
    total_steps = _nonnegative_integer(total, "total")
    bar_width = _nonnegative_integer(width, "width")
    if total_steps == 0:
        raise ValueError("total must be greater than zero")
    if bar_width == 0:
        raise ValueError("width must be greater than zero")
    if completed_steps > total_steps:
        raise ValueError("completed cannot be greater than total")

    filled = completed_steps * bar_width // total_steps
    percent = completed_steps * 100 // total_steps
    bar = "#" * filled + "." * (bar_width - filled)
    return f"[{bar}] {percent}%"


def animate_progress_bar(
    total_steps: int = 10,
    width: int = 10,
    delay: float = 0.05,
    stream: Optional[TextIO] = None,
    sleep_function: Callable[[float], None] = time.sleep,
) -> str:
    """Print all progress frames using carriage returns and immediate flushing."""
    steps = _nonnegative_integer(total_steps, "total_steps")
    if steps == 0:
        raise ValueError("total_steps must be greater than zero")
    _nonnegative_integer(width, "width")
    seconds = _nonnegative_delay(delay)
    if not callable(sleep_function):
        raise TypeError("sleep_function must be callable")

    output = sys.stdout if stream is None else stream
    final_frame = ""
    for completed in range(steps + 1):
        final_frame = progress_bar_frame(completed, steps, width)
        print(f"\r{final_frame}", end="", file=output, flush=True)
        sleep_function(seconds)
    print(file=output)
    return final_frame


def q01_format_numbers_one_to_ten() -> str:
    """Return the solution for Exercise 1."""
    return format_numbers_one_to_ten()


def q02_format_money(amount: float) -> str:
    """Return the solution for Exercise 2."""
    return format_money(amount)


def q03_print_timed_dots(
    count: int = 40,
    delay: float = 0.1,
    stream: Optional[TextIO] = None,
    sleep_function: Callable[[float], None] = time.sleep,
) -> str:
    """Return the solution for Exercise 3."""
    return print_timed_dots(count, delay, stream, sleep_function)


def q04_animate_progress_bar(
    total_steps: int = 10,
    width: int = 10,
    delay: float = 0.05,
    stream: Optional[TextIO] = None,
    sleep_function: Callable[[float], None] = time.sleep,
) -> str:
    """Return the solution for Exercise 4."""
    return animate_progress_bar(total_steps, width, delay, stream, sleep_function)


def main() -> None:
    """Run all four printing demonstrations."""
    print_numbers_one_to_ten()
    print(format_money(1234.56))
    print_timed_dots()
    animate_progress_bar()


if __name__ == "__main__":
    main()
