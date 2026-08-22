"""Tests for Chapter 26."""

import unittest

from chapters.chapter_26_functional_programming import solutions


class FunctionalProgrammingTests(unittest.TestCase):
    def test_easy_exercises(self):
        mapped, comprehended = solutions.q01_square_versions()
        self.assertEqual(mapped, comprehended)
        self.assertEqual(mapped, [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
        filtered, comprehended = solutions.q02_divisible_by_three_versions()
        self.assertEqual(filtered, comprehended)
        self.assertEqual(filtered[0], 3)
        self.assertEqual(filtered[-1], 48)
        self.assertEqual(solutions.q03_word_checks(["cat", "hippopotamus", "dog"]), (True, True))
        self.assertEqual(solutions.q03_word_checks([]), (False, True))

    def test_medium_exercises(self):
        self.assertEqual(solutions.q04_even_integer_sum(["10", "15", "20", "25", "30"]), 60)
        self.assertEqual(
            solutions.q05_longest_with_reduce(["cat", "elephant", "hippopotamus", "ant"]),
            "hippopotamus",
        )
        with self.assertRaises(ValueError):
            solutions.q05_longest_with_reduce([])
        zipped, comprehended = solutions.q06_score_pipeline(
            ["Alice", "Bob", "Charlie"], [92, 78, 85]
        )
        expected_mapping = {"Alice": 92, "Bob": 78, "Charlie": 85}
        expected_high_scores = [("Alice", 92), ("Charlie", 85)]
        self.assertEqual(zipped, (expected_mapping, expected_high_scores))
        self.assertEqual(comprehended, (expected_mapping, expected_high_scores))
        with self.assertRaises(ValueError):
            solutions.q06_score_pipeline(["Alice"], [90, 80])
        composed = solutions.q07_compose(lambda value: value ** 2, lambda value: value + 1)
        self.assertEqual(composed(5), 36)

    def test_hard_exercises(self):
        numbers = [3, 7, 3, 1, 9, 7, 5, 1, 8, 5]
        self.assertEqual(solutions.q08_process_numbers(numbers, 4), ([7, 9, 5, 8], 29))
        self.assertEqual(numbers, [3, 7, 3, 1, 9, 7, 5, 1, 8, 5])
        self.assertEqual(
            solutions.q09_word_frequencies(["the quick fox", "the lazy fox"]),
            {"the": 2, "quick": 1, "fox": 2, "lazy": 1},
        )
        self.assertAlmostEqual(solutions.q10_apply_discounts(15, 10, 5, price=100), 72.675)
        self.assertAlmostEqual(solutions.q10_student_discount(price=100), 90.0)
        self.assertAlmostEqual(solutions.q10_vip_discount(price=100), 76.0)


if __name__ == "__main__":
    unittest.main()
