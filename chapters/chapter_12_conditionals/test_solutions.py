"""Tests for Chapter 12 exercises."""

import importlib
import sys
import unittest

from chapters.chapter_12_conditionals import solutions


class Chapter12Tests(unittest.TestCase):
    def test_q01_classifies_sign(self):
        self.assertEqual(solutions.q01_number_sign(3.5), "positive")
        self.assertEqual(solutions.q01_number_sign(-0.1), "negative")
        self.assertEqual(solutions.q01_number_sign(0), "zero")

    def test_q02_classifies_leap_year(self):
        self.assertTrue(solutions.q02_is_leap_year(2000))
        self.assertFalse(solutions.q02_is_leap_year(1900))
        self.assertTrue(solutions.q02_is_leap_year(2024))
        self.assertFalse(solutions.q02_is_leap_year(2023))

    def test_q03_conditional_expression(self):
        cases = ((-2, "negative"), (0, "zero"), (2, "positive"))
        for number, expected in cases:
            self.assertEqual(solutions.q03_number_sign_expression(number), expected)

    def test_q04_triangle_validation_and_types(self):
        self.assertEqual(solutions.q04_triangle_type(3, 3, 3), "equilateral")
        self.assertEqual(solutions.q04_triangle_type(3, 3, 4), "isosceles")
        self.assertEqual(solutions.q04_triangle_type(3, 4, 5), "scalene")
        self.assertEqual(solutions.q04_triangle_type(1, 2, 3), "not a triangle")
        self.assertEqual(solutions.q04_triangle_type(-1, 2, 2), "not a triangle")

    def test_q05_bmi_categories_and_validation(self):
        self.assertEqual(solutions.q05_bmi_category(50, 1.8)[1], "underweight")
        self.assertEqual(solutions.q05_bmi_category(70, 1.75)[1], "normal weight")
        self.assertEqual(solutions.q05_bmi_category(90, 1.8)[1], "overweight")
        self.assertEqual(solutions.q05_bmi_category(120, 1.8)[1], "obese")
        with self.assertRaises(ValueError):
            solutions.q05_bmi_category(70, 0)

    def test_q06_month_days_and_validation(self):
        self.assertEqual(solutions.q06_days_in_month(1), 31)
        self.assertEqual(solutions.q06_days_in_month(4), 30)
        self.assertEqual(solutions.q06_days_in_month(2), 28)
        with self.assertRaises(ValueError):
            solutions.q06_days_in_month(13)

    def test_q07_rock_paper_scissors(self):
        self.assertEqual(solutions.q07_rock_paper_scissors("Rock", "scissors"), "Player 1 wins!")
        self.assertEqual(solutions.q07_rock_paper_scissors("paper", "paper"), "Tie!")
        self.assertEqual(solutions.q07_rock_paper_scissors("rock", "paper"), "Player 2 wins!")
        with self.assertRaises(ValueError):
            solutions.q07_rock_paper_scissors("water", "rock")

    def test_q08_integer_labels(self):
        self.assertEqual(solutions.q08_integer_labels(17), ("positive", "odd", "multi-digit", "prime"))
        self.assertEqual(solutions.q08_integer_labels(0), ("zero", "even", "single-digit", "neither prime nor composite"))
        self.assertEqual(solutions.q08_integer_labels(-12), ("negative", "even", "multi-digit", "neither prime nor composite"))
        self.assertEqual(solutions.q08_integer_labels(21)[-1], "composite")

    def test_q09_marginal_income_tax(self):
        self.assertEqual(solutions.q09_income_tax(10_000), 1_000)
        self.assertEqual(solutions.q09_income_tax(25_000), 4_000)
        self.assertEqual(solutions.q09_income_tax(50_000), 10_000)
        with self.assertRaises(ValueError):
            solutions.q09_income_tax(-1)

    @unittest.skipIf(sys.version_info < (3, 10), "match requires Python 3.10+")
    def test_exact_match_solution(self):
        module = importlib.import_module(
            "chapters.chapter_12_conditionals.modern_examples"
        )
        self.assertEqual(module.q06_days_in_month_match(1), 31)
        self.assertEqual(module.q06_days_in_month_match(2), 28)
        self.assertEqual(module.q06_days_in_month_match(4), 30)
        with self.assertRaises(ValueError):
            module.q06_days_in_month_match(13)


if __name__ == "__main__":
    unittest.main()
