"""Tests for Chapter 14 exercises."""

import unittest

from chapters.chapter_14_loops import solutions


class Chapter14Tests(unittest.TestCase):
    def test_q01_numbers_1_to_20(self):
        self.assertEqual(solutions.q01_numbers_1_to_20(), list(range(1, 21)))

    def test_q02_even_sum(self):
        self.assertEqual(solutions.q02_sum_even_numbers(), 2550)

    def test_q03_powers_below_1000(self):
        self.assertEqual(solutions.q03_powers_of_two(), [1, 2, 4, 8, 16, 32, 64, 128, 256, 512])

    def test_q04_multiples(self):
        self.assertEqual(solutions.q04_multiples_of_three_or_five(20), [3, 5, 6, 9, 10, 12, 15, 18, 20])
        with self.assertRaises(ValueError):
            solutions.q04_multiples_of_three_or_five(0)

    def test_q05_manual_and_builtin_statistics_match(self):
        manual, built_in = solutions.q05_score_statistics()
        self.assertEqual(manual, (72.5, 95, 40))
        self.assertEqual(manual, built_in)
        with self.assertRaises(ValueError):
            solutions.q05_score_statistics([])

    def test_q06_password_attempt_limit(self):
        self.assertEqual(solutions.q06_password_result(["bad", "hunter2"]), "Access granted.")
        self.assertEqual(solutions.q06_password_result(["bad"] * 4), "Locked out.")

    def test_q07_table_uses_five_character_fields(self):
        table = solutions.q07_multiplication_table()
        self.assertEqual(len(table), 12)
        self.assertTrue(table[0].endswith("   10"))
        self.assertTrue(table[-1].endswith("  100"))
        self.assertEqual(len(table[2]), len(table[-1]))

    def test_q08_nested_loop_primes(self):
        self.assertEqual(solutions.q08_primes_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(solutions.q08_primes_up_to(1), [])
        with self.assertRaises(ValueError):
            solutions.q08_primes_up_to(0)

    def test_q09_enumerated_words(self):
        self.assertEqual(solutions.q09_numbered_words(["apple", "banana"]), ["1. apple", "2. banana"])

    def test_q10_guessing_game_break_and_else_paths(self):
        self.assertEqual(
            solutions.q10_guessing_game([25, 75, 50], secret=50),
            ["Higher.", "Lower.", "Correct! The number was 50."],
        )
        self.assertEqual(
            solutions.q10_guessing_game([1] * 10, secret=50)[-1],
            "Out of guesses. The number was 50.",
        )
        self.assertEqual(
            solutions.q10_guessing_game([1] * 10 + [50], secret=50),
            ["Higher."] * 10 + ["Out of guesses. The number was 50."],
        )
        with self.assertRaises(ValueError):
            solutions.q10_guessing_game([0] * 10, secret=50)


if __name__ == "__main__":
    unittest.main()
