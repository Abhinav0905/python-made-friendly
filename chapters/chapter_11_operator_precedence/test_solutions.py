"""Tests for Chapter 11 exercises."""

import unittest

from chapters.chapter_11_operator_precedence import solutions


class Chapter11Tests(unittest.TestCase):
    def test_q01_precedence_results(self):
        self.assertEqual(solutions.q01_precedence_results(), (11, 21, 4, 512))

    def test_q02_negative_square(self):
        self.assertEqual(solutions.q02_negative_square(), -9)

    def test_q03_explicit_grouping(self):
        self.assertEqual(solutions.q03_grouped_expression(1, 2, 3, 8, 4), 5.0)

    def test_q04_average_forms(self):
        grouped, rewritten = solutions.q04_average_forms(3, 6, 9)
        self.assertEqual(grouped, 6.0)
        self.assertEqual(rewritten, 6.0)

    def test_q05_mixed_results(self):
        self.assertEqual(solutions.q05_mixed_results(), (True, False, False, True))

    def test_q06_and_binds_more_tightly_than_or(self):
        self.assertEqual(
            solutions.q06_compare_groupings(True, False, False),
            (True, False),
        )

    def test_q07_long_expression(self):
        self.assertEqual(solutions.q07_evaluate_expression(), 17.0)

    def test_q08_chained_comparisons(self):
        self.assertEqual(solutions.q08_chained_comparisons(), (True, True))


if __name__ == "__main__":
    unittest.main()
