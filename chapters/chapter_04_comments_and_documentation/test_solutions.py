"""Tests for Chapter 4 exercises."""

import doctest
import unittest

from chapters.chapter_04_comments_and_documentation import solutions


class Chapter04Tests(unittest.TestCase):
    def test_q01_converts_temperature_and_has_docstring_examples(self):
        self.assertEqual(solutions.q01_celsius_to_fahrenheit(0), 32.0)
        self.assertEqual(solutions.q01_celsius_to_fahrenheit(100), 212.0)
        failures, attempted = doctest.testmod(solutions)
        self.assertEqual(failures, 0)
        self.assertGreaterEqual(attempted, 2)

    def test_q02_renders_help(self):
        help_text = solutions.q02_help_for_temperature_function()
        self.assertIn("q01_celsius_to_fahrenheit(celsius", help_text)
        self.assertIn("Temperature in degrees Celsius", help_text)

    def test_q03_reads_and_uses_standard_library_documentation(self):
        self.assertIn("r-length", solutions.q03_combinations_docstring())
        self.assertEqual(
            solutions.q03_combinations("ABCD", 2),
            [("A", "B"), ("A", "C"), ("A", "D"), ("B", "C"), ("B", "D"), ("C", "D")],
        )
        with self.assertRaises(ValueError):
            solutions.q03_combinations([1, 2], -1)

    def test_q04_collects_real_comments_only(self):
        source = '# reason\nlabel = "item #1"  # ids start at one\n'
        self.assertEqual(
            solutions.q04_collect_comments(source),
            [(1, "reason"), (2, "ids start at one")],
        )


if __name__ == "__main__":
    unittest.main()
