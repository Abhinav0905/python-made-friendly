"""Worked exercises for Chapter 40: The math Module."""

import math
from itertools import combinations


def q01_constants():
    """Exercise 1: return pi, e, tau, and the tau identity check."""
    return math.pi, math.e, math.tau, math.tau == 2 * math.pi


def q02_special_angles():
    """Exercise 2: calculate common degree-based trig values."""
    return (
        round(math.sin(math.radians(30)), 4),
        round(math.cos(math.radians(60)), 4),
        round(math.tan(math.radians(45)), 4),
    )


def q03_factorial_and_combination():
    """Exercise 3: return 10! and 10 choose 3."""
    return math.factorial(10), math.comb(10, 3)


def q04_number_summary(value):
    """Exercise 4: calculate a square root and logs where defined."""
    result = {
        "square_root": None,
        "natural_log": None,
        "log_base_10": None,
        "messages": [],
    }
    try:
        if isinstance(value, bool):
            raise TypeError
        number = float(value)
    except (TypeError, ValueError):
        result["messages"].append("input is not a number")
        return result
    if not math.isfinite(number):
        result["messages"].append("input must be finite")
        return result

    if number < 0:
        result["messages"].append("square root is not real for a negative number")
    else:
        result["square_root"] = math.sqrt(number)

    if number <= 0:
        result["messages"].append("logarithms require a positive number")
    else:
        result["natural_log"] = math.log(number)
        result["log_base_10"] = math.log10(number)
    return result


def q05_distance_comparison(x=3, y=4):
    """Exercise 5: compare equivalent distance formulas."""
    hypotenuse = math.hypot(x, y)
    square_root = math.sqrt(x * x + y * y)
    return hypotenuse, square_root, square_root / 2, math.isclose(hypotenuse, square_root)


def q06_trig_summary(angle_degrees):
    """Exercise 6: return sine, cosine, and tangent for a degree angle."""
    radians = math.radians(angle_degrees)
    return math.sin(radians), math.cos(radians), math.tan(radians)


def q07_almost_equal(a, b, tolerance=1e-9):
    """Exercise 7: compare floats with one absolute and relative tolerance."""
    if tolerance < 0:
        raise ValueError("tolerance cannot be negative")
    return math.isclose(a, b, rel_tol=tolerance, abs_tol=tolerance)


def q08_newton_sqrt(value, tolerance=1e-12):
    """Exercise 8: approximate a square root with Newton's method."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError("value must be a real number")
    if not math.isfinite(value):
        raise ValueError("value must be finite")
    if isinstance(tolerance, bool) or not isinstance(tolerance, (int, float)):
        raise TypeError("tolerance must be a real number")
    if not math.isfinite(tolerance) or tolerance <= 0:
        raise ValueError("tolerance must be positive and finite")
    if value < 0:
        raise ValueError("square root is not real for a negative number")
    if value == 0:
        return 0.0
    guess = value if value >= 1 else 1.0
    while True:
        next_guess = (guess + value / guess) / 2
        if abs(next_guess - guess) < tolerance:
            return next_guess
        guess = next_guess


def haversine_km(point_a, point_b):
    """Return great-circle distance between two (latitude, longitude) pairs."""
    latitude_1, longitude_1 = map(math.radians, point_a)
    latitude_2, longitude_2 = map(math.radians, point_b)
    latitude_delta = latitude_2 - latitude_1
    longitude_delta = longitude_2 - longitude_1
    haversine = (
        math.sin(latitude_delta / 2) ** 2
        + math.cos(latitude_1)
        * math.cos(latitude_2)
        * math.sin(longitude_delta / 2) ** 2
    )
    central_angle = 2 * math.atan2(math.sqrt(haversine), math.sqrt(1 - haversine))
    return 6371.0088 * central_angle


def q09_city_distances(cities=None):
    """Exercise 9: return pair distances and the farthest city pair."""
    if cities is None:
        cities = {
            "London": (51.5074, -0.1278),
            "New York": (40.7128, -74.0060),
            "Tokyo": (35.6762, 139.6503),
        }
    distances = {}
    for first, second in combinations(sorted(cities), 2):
        distances[(first, second)] = haversine_km(cities[first], cities[second])
    farthest = max(distances, key=distances.get)
    return distances, farthest


def q10_leibniz_pi(terms=1000):
    """Exercise 10: approximate pi using a requested number of terms."""
    if terms <= 0:
        raise ValueError("terms must be positive")
    total = 0.0
    for index in range(terms):
        total += (-1.0) ** index / (2 * index + 1)
    return 4 * total


def main():
    print("sin 30, cos 60, tan 45:", q02_special_angles())
    print("10! and 10 choose 3:", q03_factorial_and_combination())
    print("Newton sqrt(2):", q08_newton_sqrt(2))
    distances, farthest = q09_city_distances()
    print("Farthest pair:", farthest, f"{distances[farthest]:.1f} km")
    print("Leibniz pi (1,000 terms):", q10_leibniz_pi())


if __name__ == "__main__":
    main()
