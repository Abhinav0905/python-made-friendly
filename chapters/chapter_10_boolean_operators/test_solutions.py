"""Tests for Chapter 10 exercises."""

import io
import unittest
from contextlib import redirect_stdout

from chapters.chapter_10_boolean_operators import solutions


class Chapter10Tests(unittest.TestCase):
    def test_q01_truth_table_checks(self):
        self.assertEqual(solutions.q01_truth_table_checks(), (False, True, False, True))

    def test_q02_range_expression(self):
        self.assertTrue(solutions.q02_is_between_zero_and_100(50))
        self.assertFalse(solutions.q02_is_between_zero_and_100(0))
        self.assertFalse(solutions.q02_is_between_zero_and_100(100))

    def test_q03_returns_last_truthy_operand(self):
        self.assertEqual(solutions.q03_last_truthy_value(), "last")

    def test_q04_requires_two_nonempty_fields(self):
        self.assertEqual(solutions.q04_log_on("Ada", "pw"), "welcome")
        self.assertEqual(solutions.q04_log_on("  ", "pw"), "Both fields are required.")

    def test_q05_entry_policy(self):
        self.assertTrue(solutions.q05_may_enter(True, True, False))
        self.assertTrue(solutions.q05_may_enter(True, False, True))
        self.assertFalse(solutions.q05_may_enter(False, True, True))

    def test_q06_leap_year(self):
        self.assertTrue(solutions.q06_is_leap_year(2024))
        self.assertFalse(solutions.q06_is_leap_year(1900))
        self.assertTrue(solutions.q06_is_leap_year(2000))

    def test_q07_operand_results_and_short_circuit(self):
        output = io.StringIO()
        with redirect_stdout(output):
            result = solutions.q07_operand_results()
        self.assertEqual(result, (20, 10, "hello", "", None, 0.0))
        self.assertEqual(output.getvalue(), "")

    def test_q08_default_display_name(self):
        self.assertEqual(solutions.q08_display_name("Ada"), "Ada")
        self.assertEqual(solutions.q08_display_name(None), "Guest")
        self.assertEqual(solutions.q08_display_name(""), "Guest")


if __name__ == "__main__":
    unittest.main()
