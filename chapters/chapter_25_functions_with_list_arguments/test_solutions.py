"""Tests for Chapter 25."""

import unittest

from chapters.chapter_25_functions_with_list_arguments import solutions


class ListArgumentTests(unittest.TestCase):
    def test_doubling_exercises(self):
        values = [1, 2, 3]
        result = solutions.q01_double_in_place(values)
        self.assertIsNone(result)
        self.assertEqual(values, [2, 4, 6])
        original = [1, 2, 3]
        doubled = solutions.q02_doubled(original)
        self.assertEqual(original, [1, 2, 3])
        self.assertEqual(doubled, [2, 4, 6])
        self.assertIsNot(original, doubled)
        self.assertEqual(
            solutions.q03_compare_doubling([1, 2]),
            ([2, 4], None, [1, 2], [2, 4]),
        )

    def test_medium_exercises(self):
        values = [3, 1, 3, 2, 1, 4]
        self.assertIsNone(solutions.q04_remove_duplicates_in_place(values))
        self.assertEqual(values, [3, 1, 2, 4])
        original = [1, 2, 3, 4, 5]
        self.assertEqual(solutions.q05_split_at(original, 3), ([1, 2, 3], [4, 5]))
        self.assertEqual(solutions.q05_split_at(original, 99), (original, []))
        self.assertEqual(solutions.q06_stats([3, 7, 1, 9, 4]), (1, 9, 24, 4.8))
        self.assertEqual(solutions.q06_stats([]), (None, None, None, None))

    def test_hard_exercises(self):
        self.assertEqual(
            solutions.q07_partition([1, 2, 3, 4, 5], lambda number: number % 2 == 0),
            ([2, 4], [1, 3, 5]),
        )
        self.assertEqual(
            solutions.q08_merge_sorted([1, 2, 2, 5], [2, 3, 4]),
            [1, 2, 2, 2, 3, 4, 5],
        )
        self.assertEqual(solutions.q08_merge_sorted([], [1, 2]), [1, 2])
        values = [1, 2, 3, 4]
        result = solutions.q09_shuffle_in_place(values, randint=lambda low, high: 0)
        self.assertIsNone(result)
        self.assertEqual(values, [2, 3, 4, 1])
        with self.assertRaises(ValueError):
            solutions.q09_shuffle_in_place([1, 2], randint=lambda low, high: high + 1)


if __name__ == "__main__":
    unittest.main()
