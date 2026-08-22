"""Tests for Chapter 1 exercises."""

import io
import unittest
from contextlib import redirect_stdout

from chapters.chapter_01_getting_started import solutions


class Chapter01Tests(unittest.TestCase):
    def test_q01_multiplies_values(self):
        self.assertEqual(solutions.q01_multiply_15_by_23(), 345)

    def test_q02_greets_me(self):
        self.assertEqual(solutions.q02_greet_me("Guido"), "Hello, Guido")

    def test_q03_extends_hello_script(self):
        self.assertEqual(
            solutions.q03_hello_with_color("Mina", "green"),
            ("Hello, Mina", "Your favorite color is green", "Welcome to Python."),
        )

    def test_q04_checks_supported_version(self):
        self.assertFalse(solutions.q04_python_version_is_supported((3, 7, 9)))
        self.assertTrue(solutions.q04_python_version_is_supported((3, 8, 0)))
        self.assertTrue(solutions.q04_python_version_is_supported((4, 0)))
        with self.assertRaises(ValueError):
            solutions.q04_python_version_is_supported((3,))

    def test_main_demo(self):
        output = io.StringIO()
        with redirect_stdout(output):
            solutions.main()
        self.assertIn("345", output.getvalue())
        self.assertIn("Your favorite color is blue", output.getvalue())


if __name__ == "__main__":
    unittest.main()
