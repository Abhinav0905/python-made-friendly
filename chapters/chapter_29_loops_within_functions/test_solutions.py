"""Tests for Chapter 29."""

import unittest

from chapters.chapter_29_loops_within_functions import solutions


class LoopsWithinFunctionsTests(unittest.TestCase):
    def test_easy_exercises(self):
        self.assertEqual(solutions.q01_first_negative([3, 5, -2, -8]), -2)
        self.assertIsNone(solutions.q01_first_negative([1, 2, 3]))
        self.assertFalse(solutions.q02_contains_duplicates([1, 2, 3]))
        self.assertTrue(solutions.q02_contains_duplicates([[1], [2], [1]]))
        self.assertEqual(solutions.q03_count_vowels("Hello World"), 3)
        self.assertEqual(solutions.q03_count_vowels("rhythm"), 0)

    def test_medium_exercises(self):
        self.assertEqual(solutions.q04_index_of_max([3, 9, 1, 9]), 1)
        self.assertIsNone(solutions.q04_index_of_max([]))
        self.assertEqual(solutions.q05_find_all([1, 2, 3, 2, 4, 2], 2), [1, 3, 5])
        self.assertEqual(
            list(solutions.q06_pairs_summing_to([5, 2, 3, 4, 5, 2], 7)),
            [(2, 5), (3, 4)],
        )
        self.assertEqual(
            solutions.q07_group_consecutive([1, 1, 2, 3, 3, 3, 1]),
            [(1, 2), (2, 1), (3, 3), (1, 1)],
        )
        self.assertEqual(solutions.q07_group_consecutive(iter([])), [])

    def test_hard_exercises(self):
        self.assertEqual(
            solutions.q08_flatten([1, [2, [3, 4], 5], 6]),
            [1, 2, 3, 4, 5, 6],
        )
        self.assertEqual(solutions.q08_flatten([("tuple",)]), [("tuple",)])
        self.assertEqual(
            solutions.q09_longest_increasing_run([1, 2, 1, 2, 3, 4, 1, 2]),
            [1, 2, 3, 4],
        )
        self.assertEqual(solutions.q09_longest_increasing_run([5, 4, 3]), [5])
        self.assertEqual(
            list(solutions.q10_moving_average([1, 2, 3, 4, 5], 3)),
            [2.0, 3.0, 4.0],
        )
        self.assertEqual(list(solutions.q10_moving_average([1, 2], 3)), [])
        with self.assertRaises(ValueError):
            list(solutions.q10_moving_average([1, 2], 0))


if __name__ == "__main__":
    unittest.main()
