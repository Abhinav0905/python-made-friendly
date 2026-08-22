"""Worked exercises for Chapter 35: Importing Modules."""

import datetime as dt
import importlib
import inspect
import math
import os
import sys
import sysconfig
from random import choice


def q01_math_values():
    """Return sqrt(2), pi, and 10 factorial using the ``math`` prefix."""
    return math.sqrt(2), math.pi, math.factorial(10)


def q02_pick_food(foods, choice_fn=choice):
    """Choose one favorite food with a directly imported ``choice`` function."""
    if not foods:
        raise ValueError("foods must not be empty")
    return choice_fn(foods)


def q03_hello(name):
    """Return the greeting implemented in ``examples/q03_greetings``."""
    return f"Hello, {name}!"


def q04_add(a, b):
    return a + b


def q04_subtract(a, b):
    return a - b


def q04_multiply(a, b):
    return a * b


def q04_divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


def q05_calculator_demo(a=10, b=5):
    """Return the four results printed by the guarded calculator demo."""
    return {
        "add": q04_add(a, b),
        "subtract": q04_subtract(a, b),
        "multiply": q04_multiply(a, b),
        "divide": q04_divide(a, b),
    }


def q06_current_time(now_fn=None):
    """Return a current-time string while importing ``datetime`` as ``dt``."""
    if now_fn is None:
        now_fn = dt.datetime.now
    return now_fn().strftime("%H:%M:%S")


def q07_fetch_summary(get_fn, url="https://www.python.org", timeout=10):
    """Call an injected requests-like getter and summarize its response.

    The caller supplies ``get_fn``. Tests use a fake, so importing this project
    neither requires ``requests`` nor makes a network call.
    """
    response = get_fn(url, timeout=timeout)
    response.raise_for_status()
    return {
        "status_code": response.status_code,
        "content_length": len(response.text),
        "content_type": response.headers.get("content-type"),
    }


def q08_format_name(first, last):
    """Format a name as the helpers module in the three-file project does."""
    return f"{last.upper()}, {first}"


def q09_sys_path_report(entries=None):
    """Label each import-search entry with its usual role."""
    if entries is None:
        entries = sys.path
    stdlib = os.path.realpath(sysconfig.get_path("stdlib"))
    report = []
    for index, entry in enumerate(entries):
        resolved = os.path.realpath(entry or os.getcwd())
        if not entry:
            description = "current working directory"
        elif "site-packages" in resolved or "dist-packages" in resolved:
            description = "installed third-party packages"
        elif resolved.endswith((".zip", ".egg")):
            description = "import archive"
        elif resolved == stdlib or resolved.startswith(stdlib + os.sep):
            description = "Python standard library"
        else:
            description = "application or configured import directory"
        report.append((index, entry, description))
    return report


def q09_import_from_directory(directory, module_name):
    """Temporarily prepend a directory, import a module, then restore state."""
    original_path = sys.path[:]
    missing = object()
    previous_module = sys.modules.get(module_name, missing)
    try:
        sys.path.insert(0, os.fspath(directory))
        sys.modules.pop(module_name, None)
        importlib.invalidate_caches()
        return importlib.import_module(module_name)
    finally:
        sys.path[:] = original_path
        if previous_module is missing:
            sys.modules.pop(module_name, None)
        else:
            sys.modules[module_name] = previous_module
        importlib.invalidate_caches()


def q10_inspect_module(module_name):
    """Return a dynamically imported module's docstring and public functions."""
    module = importlib.import_module(module_name)
    docstring = module.__doc__.strip() if module.__doc__ else None
    functions = sorted(
        name
        for name, value in inspect.getmembers(module, inspect.isfunction)
        if not name.startswith("_")
    )
    return docstring, functions


def main():
    sqrt_two, pi, factorial_ten = q01_math_values()
    print("sqrt(2) =", sqrt_two)
    print("pi =", pi)
    print("10! =", factorial_ten)


if __name__ == "__main__":
    main()
