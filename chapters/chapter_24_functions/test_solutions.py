"""Tests for Chapter 24."""

import unittest

from chapters.chapter_24_functions import solutions


class FunctionTests(unittest.TestCase):
    def test_easy_exercises(self):
        self.assertEqual(solutions.q01_area_of_rectangle(5, 3), 15)
        self.assertEqual(solutions.q01_area_of_rectangle(2.5, 4), 10.0)
        self.assertTrue(solutions.q02_is_even(-2))
        self.assertFalse(solutions.q02_is_even(7))
        self.assertEqual(solutions.q03_greet("Ada"), "Hello, Ada!")
        self.assertEqual(solutions.q03_greet("Ada", "Hi"), "Hi, Ada!")

    def test_medium_exercises(self):
        self.assertEqual(solutions.q04_word_count("  one\ttwo\nthree  "), 3)
        self.assertEqual(solutions.q04_word_count(""), 0)
        self.assertEqual(solutions.q05_max_of_three(7, 7, 2), 7)
        self.assertEqual(solutions.q05_max_of_three(-3, -1, -2), -1)
        self.assertEqual(solutions.q06_safe_divide(10, 2), 5.0)
        self.assertIsNone(solutions.q06_safe_divide(10, 0))

    def test_mutable_default_bug_and_fix(self):
        shared_default = solutions.q07_buggy_add_student.__defaults__[0]
        shared_default.clear()
        first = solutions.q07_buggy_add_student("Alice")
        second = solutions.q07_buggy_add_student("Bob")
        self.assertIs(first, second)
        self.assertEqual(second, ["Alice", "Bob"])
        shared_default.clear()
        fixed_first = solutions.q07_add_student("Alice")
        fixed_second = solutions.q07_add_student("Bob")
        self.assertEqual(fixed_first, ["Alice"])
        self.assertEqual(fixed_second, ["Bob"])
        self.assertIsNot(fixed_first, fixed_second)

    def test_hard_exercises(self):
        self.assertEqual(solutions.q08_fibonacci(0), [])
        self.assertEqual(solutions.q08_fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        self.assertIn("Parameters", solutions.q08_fibonacci.__doc__)
        with self.assertRaises(ValueError):
            solutions.q08_fibonacci(-1)
        for prime in (2, 3, 17, 97):
            self.assertTrue(solutions.q09_is_prime(prime))
        for composite in (-1, 0, 1, 4, 25, 99):
            self.assertFalse(solutions.q09_is_prime(composite))
        self.assertEqual(solutions.q10_apply_n_times(lambda value: value * 2, 1, 5), 32)
        self.assertEqual(solutions.q10_apply_n_times(lambda value: value + 1, 10, 0), 10)
        with self.assertRaises(ValueError):
            solutions.q10_apply_n_times(lambda value: value, 1, -1)


if __name__ == "__main__":
    unittest.main()
