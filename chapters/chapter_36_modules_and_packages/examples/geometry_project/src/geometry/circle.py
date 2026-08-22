"""Circle calculations and a direct-execution demo."""

import math

__all__ = ["area", "circumference"]


def area(radius):
    return math.pi * radius ** 2


def circumference(radius):
    return 2 * math.pi * radius


def _diameter(radius):
    return 2 * radius


def main():
    radius = 5
    print("Circle Demo")
    print(f"Radius: {radius}")
    print(f"Area: {area(radius):.2f}")
    print(f"Circumference: {circumference(radius):.2f}")


if __name__ == "__main__":
    main()
