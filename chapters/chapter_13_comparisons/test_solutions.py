"""Tests for Chapter 13 exercises."""

import unittest

from chapters.chapter_13_comparisons import solutions


class Chapter13Tests(unittest.TestCase):
    def test_q01_cross_type_equality(self):
        self.assertEqual(solutions.q01_equality_results(), (True, False, True, False))

    def test_q02_inclusive_range(self):
        self.assertTrue(solutions.q02_between_1_and_100(1))
        self.assertTrue(solutions.q02_between_1_and_100(100))
        self.assertFalse(solutions.q02_between_1_and_100(100.1))

    def test_q03_weekday_membership(self):
        self.assertTrue(solutions.q03_is_weekday("Wed"))
        self.assertFalse(solutions.q03_is_weekday("Sat"))

    def test_q04_counts_values_in_range(self):
        self.assertEqual(solutions.q04_count_in_range([45, 50, 72, 100, 101]), 3)

    def test_q05_unicode_case_insensitive_equality(self):
        self.assertTrue(solutions.q05_case_insensitive_equal("Straße", "STRASSE"))
        self.assertFalse(solutions.q05_case_insensitive_equal("cat", "dog"))

    def test_q06_phrase_palindrome(self):
        self.assertTrue(solutions.q06_is_phrase_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(solutions.q06_is_phrase_palindrome("race a car"))

    def test_q07_chained_comparisons(self):
        self.assertEqual(solutions.q07_chained_results(), (True, True, True, True))

    def test_q08_registered_user_lookup(self):
        registered = ["Alice", "Bob", "Charlie", "Diana"]
        self.assertTrue(solutions.q08_is_registered("aLiCe", registered))
        self.assertFalse(solutions.q08_is_registered("Eve", registered))

    def test_q09_vowels_in_alphabetical_order(self):
        self.assertEqual(solutions.q09_vowels_present("The quick brown fox"), ["e", "i", "o", "u"])
        self.assertEqual(solutions.q09_vowels_present("rhythm"), [])


if __name__ == "__main__":
    unittest.main()
