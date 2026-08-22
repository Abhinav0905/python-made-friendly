"""Tests for Chapter 2 exercises."""

import unittest

from chapters.chapter_02_data_types import solutions


class Chapter02Tests(unittest.TestCase):
    def test_q01_literal_types(self):
        self.assertEqual(solutions.q01_literal_types(), (int, float, str, bool))

    def test_q02_large_integer(self):
        self.assertEqual(solutions.q02_large_integer(), 1_125_899_906_842_624)

    def test_q03_float_comparisons(self):
        self.assertEqual(solutions.q03_float_comparisons(), (False, True))

    def test_q04_convert_and_add(self):
        self.assertEqual(solutions.q04_convert_and_add(), 125)
        self.assertEqual(solutions.q04_convert_and_add("0"), 25)
        with self.assertRaises(ValueError):
            solutions.q04_convert_and_add("ten")

    def test_q05_nonempty_string_is_truthy(self):
        self.assertTrue(solutions.q05_nonempty_string_is_truthy("False"))
        self.assertTrue(solutions.q05_nonempty_string_is_truthy("0"))
        self.assertFalse(solutions.q05_nonempty_string_is_truthy(""))


if __name__ == "__main__":
    unittest.main()
