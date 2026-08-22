"""Worked exercises for Chapter 32: Common Exceptions."""

import json
import sys
from pathlib import Path


def _capture_exception(action):
    try:
        action()
    except Exception as error:
        return type(error).__name__, str(error)
    raise AssertionError("the demonstration did not raise an exception")


def q01_common_exception_messages():
    """Exercise 1: trigger and capture five common exception types."""
    demonstrations = [
        lambda: int("hello"),
        lambda: "abc" + 5,
        lambda: [1, 2, 3][10],
        lambda: {"a": 1}["b"],
        lambda: 10 / 0,
    ]
    return [_capture_exception(action) for action in demonstrations]


def q02_get_item_lbyl(items, index, default=None):
    """Exercise 2a: check bounds before indexing, including negatives."""
    if -len(items) <= index < len(items):
        return items[index]
    return default


def q02_get_item_eafp(items, index, default=None):
    """Exercise 2b: try the operation and catch an invalid index."""
    try:
        return items[index]
    except IndexError:
        return default


def q03_read_integer(prompt="Enter an integer: ", input_fn=input, output_fn=print):
    """Exercise 3: keep asking until int conversion succeeds."""
    while True:
        try:
            return int(input_fn(prompt))
        except ValueError:
            output_fn("Not a valid integer. Try again.")


def q04_write_user_file(path, text, open_fn=open):
    """Exercise 4: write text and return a specific status message."""
    try:
        with open_fn(path, "w", encoding="utf-8") as output_file:
            output_file.write(text)
    except FileNotFoundError:
        return f"Parent folder not found: {path}"
    except PermissionError:
        return f"Permission denied: {path}"
    except IsADirectoryError:
        return f"That path is a directory: {path}"
    except OSError as error:
        return f"Could not write {path}: {error}"
    return f"Wrote {len(text)} characters to {path}"


def q05_safe_divide(a, b):
    """Exercise 5: return None for bad types or division by zero."""
    try:
        return a / b
    except (TypeError, ZeroDivisionError):
        return None


def q06_read_config(path):
    """Exercise 6: return parsed JSON or None for two expected failures."""
    try:
        with open(path, encoding="utf-8") as config_file:
            return json.load(config_file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def _recurse_forever():
    return _recurse_forever()


def q07_recursion_report():
    """Exercise 7: catch deliberate runaway recursion and report the limit."""
    try:
        _recurse_forever()
    except RecursionError as error:
        return sys.getrecursionlimit(), type(error).__name__, str(error)
    raise AssertionError("runaway recursion did not raise RecursionError")


class FileReadError(Exception):
    """A file failed every permitted reading attempt."""

    def __init__(self, path, original_error):
        super().__init__(f"cannot read {path!r}: {original_error}")
        self.path = Path(path)
        self.original_error = original_error


def q08_resilient_read(path, encodings=("utf-8", "latin-1")):
    """Exercise 8: try encodings in order, then raise a structured error."""
    last_error = None
    for encoding in encodings:
        try:
            with open(path, encoding=encoding) as input_file:
                return input_file.read()
        except UnicodeDecodeError as error:
            last_error = error
        except (FileNotFoundError, PermissionError, OSError) as error:
            last_error = error
            break
    raise FileReadError(path, last_error)


def q09_summarize_directory(directory):
    """Exercise 9: categorize files as readable, failed, or skipped."""
    result = {"ok": [], "errors": [], "skipped": []}
    directory = Path(directory)
    try:
        entries = sorted(directory.iterdir(), key=lambda path: path.name)
    except OSError as error:
        result["errors"].append((directory.name, type(error).__name__, str(error)))
        return result

    for entry in entries:
        if not entry.is_file():
            result["skipped"].append(entry.name)
            continue
        try:
            with entry.open(encoding="utf-8") as input_file:
                line_count = sum(1 for line in input_file)
            result["ok"].append((entry.name, line_count))
        except (OSError, UnicodeError) as error:
            result["errors"].append((entry.name, type(error).__name__, str(error)))
    return result


def main():
    for name, message in q01_common_exception_messages():
        print(f"{name}: {message}")
    print("safe_divide(8, 2):", q05_safe_divide(8, 2))
    limit, name, message = q07_recursion_report()
    print(f"{name} below recursion limit {limit}: {message}")


if __name__ == "__main__":
    main()
