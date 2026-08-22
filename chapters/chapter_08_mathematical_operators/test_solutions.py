"""Tests for the Chapter 8 solutions."""

import unittest

from chapters.chapter_08_mathematical_operators.solutions import (
    compare_modular_exponentiation,
    discount_details,
    floor_division_and_modulus,
    format_discount,
    format_hms,
    format_temperatures,
    maximum_absolute_value,
    seconds_to_hms,
    sum_digits,
    temperature_conversions,
    three_digit_digits,
    trapezoid_area,
)


class ChapterEightTests(unittest.TestCase):
    """Check all nine mathematical-operator exercises."""

    def test_exercise_1_floor_division_modulus_and_invariant(self) -> None:
        result = floor_division_and_modulus(100, 7)
        self.assertEqual(result.quotient, 14)
        self.assertEqual(result.remainder, 2)
        self.assertEqual(result.reconstructed, 100)

    def test_exercise_1_handles_negative_dividend(self) -> None:
        result = floor_division_and_modulus(-7, 2)
        self.assertEqual((result.quotient, result.remainder), (-4, 1))
        self.assertEqual(result.reconstructed, -7)

    def test_exercise_1_rejects_zero_divisor(self) -> None:
        with self.assertRaises(ValueError):
            floor_division_and_modulus(100, 0)

    def test_exercise_2_trapezoid_area(self) -> None:
        self.assertEqual(trapezoid_area(8, 12, 5), 50.0)
        self.assertEqual(trapezoid_area(2.5, 4.5, 3), 10.5)

    def test_exercise_2_rejects_negative_measurement(self) -> None:
        with self.assertRaises(ValueError):
            trapezoid_area(8, 12, -5)

    def test_exercise_3_maximum_absolute_value(self) -> None:
        self.assertEqual(maximum_absolute_value([-7, 3, -2, 8, -10]), 10.0)
        self.assertEqual(maximum_absolute_value([1, 9, -3]), 9.0)

    def test_exercise_3_rejects_empty_values(self) -> None:
        with self.assertRaises(ValueError):
            maximum_absolute_value([])

    def test_exercise_4_converts_seconds_with_divmod(self) -> None:
        self.assertEqual(seconds_to_hms(7_381), (2, 3, 1))
        self.assertEqual(format_hms(7_381), "7381s = 2h 3m 1s")
        self.assertEqual(seconds_to_hms(0), (0, 0, 0))

    def test_exercise_4_rejects_negative_seconds(self) -> None:
        with self.assertRaises(ValueError):
            seconds_to_hms(-1)

    def test_exercise_5_splits_three_digit_number_without_strings(self) -> None:
        self.assertEqual(three_digit_digits(527), (5, 2, 7))
        self.assertEqual(three_digit_digits(100), (1, 0, 0))

    def test_exercise_5_requires_three_digits(self) -> None:
        with self.assertRaises(ValueError):
            three_digit_digits(99)
        with self.assertRaises(ValueError):
            three_digit_digits(1000)

    def test_exercise_6_calculates_and_formats_discount(self) -> None:
        result = discount_details(49.99, 15)
        self.assertAlmostEqual(result.saved, 7.4985)
        self.assertAlmostEqual(result.final_price, 42.4915)
        self.assertEqual(
            format_discount(result),
            "Amount saved: $7.50\nFinal price:  $42.49",
        )

    def test_exercise_6_validates_discount_range(self) -> None:
        with self.assertRaises(ValueError):
            discount_details(10, 101)
        with self.assertRaises(ValueError):
            discount_details(-1, 10)

    def test_exercise_7_converts_and_formats_temperature(self) -> None:
        result = temperature_conversions(25)
        self.assertEqual(result.fahrenheit, 77.0)
        self.assertAlmostEqual(result.kelvin, 298.15)
        self.assertAlmostEqual(result.rankine, 536.67)
        self.assertEqual(
            format_temperatures(result),
            "Fahrenheit: 77.00 °F\n"
            "Kelvin:     298.15 K\n"
            "Rankine:    536.67 °R",
        )

    def test_exercise_7_minus_forty_is_same_in_celsius_and_fahrenheit(self) -> None:
        self.assertEqual(temperature_conversions(-40).fahrenheit, -40.0)

    def test_exercise_7_rejects_below_absolute_zero(self) -> None:
        with self.assertRaises(ValueError):
            temperature_conversions(-273.16)

    def test_exercise_8_sums_digits_with_integer_operators(self) -> None:
        self.assertEqual(sum_digits(1234), 10)
        self.assertEqual(sum_digits(900_009), 18)

    def test_exercise_8_requires_positive_integer(self) -> None:
        with self.assertRaises(ValueError):
            sum_digits(0)
        with self.assertRaises(TypeError):
            sum_digits(12.3)

    def test_exercise_9_compares_equal_results_and_timings(self) -> None:
        ticks = iter((1.0, 1.1, 2.0, 2.4))
        timing = compare_modular_exponentiation(clock=lambda: next(ticks))
        self.assertTrue(timing.results_equal)
        self.assertEqual(timing.pow_result, pow(2, 1000, 10_000_007))
        self.assertAlmostEqual(timing.pow_seconds, 0.1)
        self.assertAlmostEqual(timing.direct_seconds, 0.4)

    def test_exercise_9_rejects_invalid_modular_power_inputs(self) -> None:
        with self.assertRaises(ValueError):
            compare_modular_exponentiation(exponent=-1)
        with self.assertRaises(ValueError):
            compare_modular_exponentiation(modulus=0)


if __name__ == "__main__":
    unittest.main()
