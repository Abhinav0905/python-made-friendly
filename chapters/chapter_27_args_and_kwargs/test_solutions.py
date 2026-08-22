"""Tests for Chapter 27."""

import io
import unittest
from contextlib import redirect_stdout

from chapters.chapter_27_args_and_kwargs import solutions


class ArgsAndKwargsTests(unittest.TestCase):
    def test_easy_exercises(self):
        self.assertEqual(solutions.q01_average(1, 2, 3, 4, 5), 3.0)
        self.assertIsNone(solutions.q01_average())
        output = io.StringIO()
        with redirect_stdout(output):
            result = solutions.q02_show(name="Ada", age=37)
        self.assertIsNone(result)
        self.assertEqual(output.getvalue(), "name = Ada\nage = 37\n")
        self.assertEqual(solutions.q03_max_from_sequence([3, 1, 4]), 4)
        with self.assertRaises(ValueError):
            solutions.q03_max_from_sequence([1, 2])

    def test_medium_exercises(self):
        self.assertEqual(
            solutions.q04_tag("a", href="https://example.com", id="home"),
            '<a href="https://example.com" id="home">',
        )
        self.assertEqual(solutions.q04_tag("br"), "<br>")
        self.assertEqual(
            solutions.q05_make_person("Ada", age=37, email="ada@example.com"),
            {"name": "Ada", "age": 37, "email": "ada@example.com"},
        )
        with self.assertRaises(TypeError):
            solutions.q05_make_person("Ada", 37, "ada@example.com")
        with self.assertRaises(TypeError):
            solutions.q05_make_person("Ada", age=37)
        self.assertEqual(
            solutions.q06_summarize(1, 2, 3, separator=" | ", prefix="[", suffix="]"),
            "[1 | 2 | 3]",
        )

    def test_forwarding_exercises(self):
        def add(first, second=0):
            return first + second

        output = io.StringIO()
        with redirect_stdout(output):
            result = solutions.q07_log_and_call(add, 3, second=4)
        self.assertEqual(result, 7)
        self.assertIn("Calling add", output.getvalue())
        self.assertIn("Result: 7", output.getvalue())
        self.assertEqual(
            solutions.q08_call_all([lambda value: value ** 2, lambda value: -value], 5),
            [25, -5],
        )

    def test_timing_decorator(self):
        ticks = iter([10.0, 10.125])

        def double(value):
            """Double one value."""
            return value * 2

        timed = solutions.q09_timing(double, clock=lambda: next(ticks))
        output = io.StringIO()
        with redirect_stdout(output):
            self.assertEqual(timed(6), 12)
        self.assertEqual(output.getvalue(), "double took 0.125000 seconds\n")
        self.assertEqual(timed.__name__, "double")
        self.assertEqual(timed.__doc__, "Double one value.")


if __name__ == "__main__":
    unittest.main()
