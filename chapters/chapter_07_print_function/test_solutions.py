"""Tests for the Chapter 7 solutions."""

from io import StringIO
import unittest

from chapters.chapter_07_print_function.solutions import (
    animate_progress_bar,
    format_money,
    format_numbers_one_to_ten,
    print_numbers_one_to_ten,
    print_timed_dots,
    progress_bar_frame,
)


class TrackingStringIO(StringIO):
    """A text stream that counts explicit flushes."""

    def __init__(self) -> None:
        super().__init__()
        self.flush_count = 0

    def flush(self) -> None:
        self.flush_count += 1
        super().flush()


class ChapterSevenTests(unittest.TestCase):
    """Check formatting, terminal control and validation."""

    def test_exercise_1_formats_numbers_with_commas(self) -> None:
        expected = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"
        self.assertEqual(format_numbers_one_to_ten(), expected)

        stream = StringIO()
        returned = print_numbers_one_to_ten(stream)
        self.assertEqual(returned, expected)
        self.assertEqual(stream.getvalue(), expected + "\n")

    def test_exercise_2_formats_money(self) -> None:
        self.assertEqual(format_money(1234.56), "$1,234.56")
        self.assertEqual(format_money(42), "$42.00")
        self.assertEqual(format_money(1_000_000), "$1,000,000.00")

    def test_exercise_2_rejects_non_finite_amount(self) -> None:
        with self.assertRaises(ValueError):
            format_money(float("nan"))

    def test_exercise_3_flushes_each_dot_and_waits(self) -> None:
        stream = TrackingStringIO()
        delays = []
        returned = print_timed_dots(3, 0.1, stream, delays.append)

        self.assertEqual(returned, "...")
        self.assertEqual(stream.getvalue(), "...\n")
        self.assertEqual(stream.flush_count, 3)
        self.assertEqual(delays, [0.1, 0.1, 0.1])

    def test_exercise_3_rejects_negative_count_or_delay(self) -> None:
        with self.assertRaises(ValueError):
            print_timed_dots(-1, sleep_function=lambda _seconds: None)
        with self.assertRaises(ValueError):
            print_timed_dots(1, -0.1, sleep_function=lambda _seconds: None)

    def test_exercise_4_builds_requested_halfway_frame(self) -> None:
        self.assertEqual(progress_bar_frame(5, 10), "[#####.....] 50%")
        self.assertEqual(progress_bar_frame(1, 3, 6), "[##....] 33%")

    def test_exercise_4_animates_with_carriage_returns(self) -> None:
        stream = TrackingStringIO()
        delays = []
        final_frame = animate_progress_bar(2, 4, 0.05, stream, delays.append)

        self.assertEqual(final_frame, "[####] 100%")
        self.assertEqual(
            stream.getvalue(),
            "\r[....] 0%\r[##..] 50%\r[####] 100%\n",
        )
        self.assertEqual(stream.flush_count, 3)
        self.assertEqual(delays, [0.05, 0.05, 0.05])

    def test_exercise_4_rejects_invalid_progress(self) -> None:
        with self.assertRaises(ValueError):
            progress_bar_frame(11, 10)
        with self.assertRaises(ValueError):
            progress_bar_frame(0, 0)


if __name__ == "__main__":
    unittest.main()
