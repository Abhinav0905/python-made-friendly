"""Worked exercises for Chapter 30: Exceptions."""

import time
from contextlib import contextmanager
from pathlib import Path


def q01_read_integer(prompt="Enter an integer: ", input_fn=input, output_fn=print):
    """Exercise 1: keep asking until input can be converted to int."""
    while True:
        try:
            return int(input_fn(prompt))
        except ValueError:
            output_fn("That is not a valid integer. Try again.")


def q02_ensure_data_file(directory=Path("."), output_fn=print):
    """Exercise 2: create an empty data.txt when it does not exist."""
    path = Path(directory) / "data.txt"
    try:
        path.open("x", encoding="utf-8").close()
    except FileExistsError:
        return path, False
    output_fn(f"{path} did not exist, so an empty file was created.")
    return path, True


def q03_four_clause_demo(text, output_fn=print):
    """Exercise 3: demonstrate all four clauses and return their events."""
    events = ["try"]
    try:
        value = int(text)
    except ValueError:
        events.append("except")
        value = None
    else:
        events.append("else")
        output_fn(f"Parsed {value}")
    finally:
        events.append("finally")
    return value, events


def q04_safe_divide(a, b):
    """Exercise 4: return None when division by zero is attempted."""
    try:
        return a / b
    except ZeroDivisionError:
        return None


def q05_robust_parse(text):
    """Exercise 5: parse int first, float second, or raise ValueError."""
    try:
        return int(text)
    except ValueError:
        try:
            return float(text)
        except ValueError as error:
            raise ValueError(f"cannot parse {text!r} as a number") from error


def q06_sum_valid_integers(lines):
    """Exercise 6: skip invalid lines and sum the valid integers."""
    total = 0
    for line in lines:
        try:
            total += int(line)
        except (TypeError, ValueError):
            continue
    return total


def q07_first_value(mapping, *keys):
    """Exercise 7: return the first present key's value, or None."""
    for key in keys:
        try:
            return mapping[key]
        except KeyError:
            pass
    return None


def q08_retry(function, attempts=3, delay=1, sleep_fn=time.sleep):
    """Exercise 8: retry a callable and re-raise its final exception."""
    if attempts < 1:
        raise ValueError("attempts must be at least 1")
    if delay < 0:
        raise ValueError("delay cannot be negative")
    for attempt in range(1, attempts + 1):
        try:
            return function()
        except Exception:
            if attempt == attempts:
                raise
            sleep_fn(delay)


@contextmanager
def q09_timer(output_fn=print, clock=time.perf_counter):
    """Exercise 9: print elapsed time even if the timed block fails."""
    start = clock()
    try:
        yield
    finally:
        elapsed = clock() - start
        output_fn(f"Elapsed: {elapsed:.6f} seconds")


def main():
    print("safe_divide(10, 2):", q04_safe_divide(10, 2))
    print("safe_divide(10, 0):", q04_safe_divide(10, 0))
    print("robust_parse('3.5'):", q05_robust_parse("3.5"))
    with q09_timer():
        sum(range(10000))


if __name__ == "__main__":
    main()
