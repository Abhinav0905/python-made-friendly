"""Exercise 10 for Chapter 30. Requires Python 3.11 or newer."""


def raise_group():
    raise ExceptionGroup(
        "two failures",
        [ValueError("bad value"), TypeError("bad type")],
    )


def handle_group():
    handled = []
    try:
        raise_group()
    except* ValueError as group:
        handled.extend(type(error).__name__ for error in group.exceptions)
    except* TypeError as group:
        handled.extend(type(error).__name__ for error in group.exceptions)
    return handled


if __name__ == "__main__":
    print(handle_group())
