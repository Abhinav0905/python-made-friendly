"""Tests for Chapter 9 exercises."""

import io
import unittest
from contextlib import redirect_stdout

from chapters.chapter_09_bitwise_operators import solutions


class Chapter09Tests(unittest.TestCase):
    def test_q01_binary_breakdown(self):
        binaries, powers = solutions.q01_binary_breakdown()
        self.assertEqual(binaries, {10: "0b1010", 20: "0b10100", 100: "0b1100100"})
        self.assertEqual(powers, (64, 32, 4))
        self.assertEqual(sum(powers), 100)

    def test_q02_bitwise_results(self):
        self.assertEqual(solutions.q02_bitwise_results(), (8, 14, 6))

    def test_q03_power_of_two(self):
        self.assertEqual(solutions.q03_power_of_two(10), 1024)
        with self.assertRaises(ValueError):
            solutions.q03_power_of_two(-1)

    def test_q04_is_even(self):
        self.assertTrue(solutions.q04_is_even(-4))
        self.assertFalse(solutions.q04_is_even(-3))

    def test_q05_count_bits(self):
        for number in (0, 1, 13, 255, 1024):
            self.assertEqual(solutions.q05_count_bits(number), bin(number).count("1"))
        with self.assertRaises(ValueError):
            solutions.q05_count_bits(-1)

    def test_q06_xor_swap(self):
        self.assertEqual(solutions.q06_xor_swap(5, 9), (9, 5))
        self.assertEqual(solutions.q06_xor_swap(7, 7), (7, 7))

    def test_q07_event_handler_prints_each_set_flag(self):
        output = io.StringIO()
        with redirect_stdout(output):
            messages = solutions.q07_handle(solutions.CLICK | solutions.SCROLL)
        self.assertEqual(messages, ["Click detected", "Scroll detected"])
        self.assertEqual(output.getvalue(), "Click detected\nScroll detected\n")
        recorded = []
        messages = solutions.q07_handle(
            solutions.CLICK | solutions.KEYPRESS | solutions.RESIZE,
            output=recorded.append,
        )
        self.assertEqual(
            messages,
            ["Click detected", "Keypress detected", "Resize detected"],
        )
        self.assertEqual(recorded, messages)
        self.assertEqual(solutions.q07_handle(0, output=lambda text: None), ["No events"])

    def test_q08_sets_and_clears_bits(self):
        self.assertEqual(solutions.q08_set_bit(0b1010, 0), 0b1011)
        self.assertEqual(solutions.q08_set_bit(0b1010, 2), 0b1110)
        self.assertEqual(solutions.q08_clear_bit(0b1010, 1), 0b1000)
        self.assertEqual(solutions.q08_clear_bit(0b1010, 3), 0b0010)
        with self.assertRaises(ValueError):
            solutions.q08_set_bit(1, -1)


if __name__ == "__main__":
    unittest.main()
