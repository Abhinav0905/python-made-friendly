"""Worked exercise helpers for Chapter 36: Modules and Packages."""

import math
from pathlib import Path


def q01_circle_area(radius):
    return math.pi * radius ** 2


def q01_rectangle_area(width, height):
    return width * height


def q02_friendly_geometry_areas(radius, width, height):
    """Return results exposed by the geometry package's friendly imports."""
    return q01_circle_area(radius), q01_rectangle_area(width, height)


def q03_circle_demo(radius=5):
    """Return the guarded circle demo's three output lines."""
    return [
        f"Radius: {radius}",
        f"Area: {q01_circle_area(radius):.2f}",
        f"Circumference: {2 * math.pi * radius:.2f}",
    ]


def q04_sphere_volume(radius):
    return (4 / 3) * math.pi * radius ** 3


def q04_cube_volume(side):
    return side ** 3


def q05_public_circle_names():
    """Return the public API declared by the example circle module."""
    return ("area", "circumference")


def q06_calculator_operations(a, b):
    """Return the package-level results for the four calculator functions."""
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a + b, a - b, a * b, a / b


def q07_calculator_demo(a=10, b=5):
    """Return the values printed by ``python -m calculator``."""
    return q06_calculator_operations(a, b)


def q08_project_layout():
    """Return the essential paths in the example src-layout project."""
    return (
        "pyproject.toml",
        "src/calculator/__init__.py",
        "src/calculator/functions.py",
        "tests/test_functions.py",
    )


def q09_cli_calculate(first, operator, second):
    """Evaluate the same three tokens accepted by the ``mycalc`` entry point."""
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }
    if operator not in operations:
        raise ValueError(f"unknown operator: {operator}")
    return operations[operator](float(first), float(second))


def q10_config_values():
    """Return values from two equally named modules in separate namespaces."""
    return "from package A", "from package B"


def example_root():
    """Return the fixture root independent of the caller's current directory."""
    return Path(__file__).parent / "examples"


def main():
    print("Geometry circle area:", q01_circle_area(5))
    print("Calculator add:", q06_calculator_operations(3, 4)[0])


if __name__ == "__main__":
    main()
