"""Tests for Chapter 17."""

import unittest

from chapters.chapter_17_list_comprehensions import solutions


class ListComprehensionTests(unittest.TestCase):
    def test_easy_exercises(self):
        self.assertEqual(solutions.q01_cubes()[0:3], [1, 8, 27])
        self.assertEqual(solutions.q01_cubes()[-1], 8000)
        self.assertEqual(solutions.q02_uppercase(["Hello", "python"]), ["HELLO", "PYTHON"])
        self.assertEqual(solutions.q03_divisible_by_seven(), list(range(7, 101, 7)))

    def test_medium_exercises(self):
        self.assertEqual(solutions.q04_word_lengths(["cat", "python"]), [("cat", 3), ("python", 6)])
        self.assertEqual(solutions.q05_non_positive_to_zero([-2, 0, 4]), [0, 0, 4])
        self.assertEqual(solutions.q06_multiplication_table()[-1], [5, 10, 15, 20, 25])
        self.assertEqual(
            solutions.q07_words_from_sentences(["one two", "three"]),
            ["one", "two", "three"],
        )

    def test_hard_exercises(self):
        self.assertEqual(solutions.q08_pairs_less_than([1, 3], [2, 4]), [(1, 2), (1, 4), (3, 4)])
        self.assertEqual(
            solutions.q09_long_word_lengths(["cat", "pear", "banana"]),
            {"pear": 4, "banana": 6},
        )
        self.assertEqual(solutions.q10_exclusive_running_sums([1, 2, 3, 4]), [0, 1, 3, 6])
        self.assertEqual(solutions.q10_exclusive_running_sums([]), [])


if __name__ == "__main__":
    unittest.main()
