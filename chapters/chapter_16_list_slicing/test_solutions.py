"""Tests for Chapter 16 exercises."""

import unittest

from chapters.chapter_16_list_slicing import solutions


class Chapter16Tests(unittest.TestCase):
    def test_q01_slice_views(self):
        self.assertEqual(
            solutions.q01_slice_views(),
            ([10, 20, 30], [40, 50], [10, 30, 50], [50, 40, 30, 20, 10]),
        )

    def test_q02_string_segments(self):
        self.assertEqual(solutions.q02_string_segments(), ("gram", "prog", "gni"))

    def test_q03_reverses_without_mutating_input(self):
        original = [1, 2, 3]
        self.assertEqual(solutions.q03_reverse_list(original), [3, 2, 1])
        self.assertEqual(original, [1, 2, 3])

    def test_q04_first_and_last_values(self):
        self.assertEqual(solutions.q04_first_n_last_n(list(range(1, 9)), 2), [1, 2, 7, 8])
        self.assertEqual(solutions.q04_first_n_last_n([1, 2], 0), [])
        with self.assertRaises(ValueError):
            solutions.q04_first_n_last_n([1, 2], -1)

    def test_q05_deletes_odd_indices(self):
        original = list(range(10))
        self.assertEqual(solutions.q05_remove_every_other(original), [0, 2, 4, 6, 8])
        self.assertEqual(original, list(range(10)))

    def test_q06_chunks_and_validates_size(self):
        self.assertEqual(
            solutions.q06_chunk([1, 2, 3, 4, 5, 6, 7], 3),
            [[1, 2, 3], [4, 5, 6], [7]],
        )
        with self.assertRaises(ValueError):
            solutions.q06_chunk([1, 2], 0)

    def test_q07_interleaves_equal_length_lists(self):
        self.assertEqual(
            solutions.q07_interleave([1, 3, 5, 7], [2, 4, 6, 8]),
            [1, 2, 3, 4, 5, 6, 7, 8],
        )
        with self.assertRaises(ValueError):
            solutions.q07_interleave([1], [2, 3])

    def test_q08_palindromes_for_strings_and_lists(self):
        self.assertTrue(solutions.q08_is_palindrome("Racecar"))
        self.assertTrue(solutions.q08_is_palindrome([1, 2, 3, 2, 1]))
        self.assertFalse(solutions.q08_is_palindrome([1, 2, 3]))

    def test_q09_reverses_words(self):
        self.assertEqual(solutions.q09_reverse_words("hello world python"), "python world hello")
        self.assertEqual(solutions.q09_reverse_words("  one   two "), "two one")


if __name__ == "__main__":
    unittest.main()
