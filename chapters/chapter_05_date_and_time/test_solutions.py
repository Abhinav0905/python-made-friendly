"""Tests for the Chapter 5 solutions."""

from datetime import date, datetime
import unittest

from chapters.chapter_05_date_and_time.solutions import (
    days_until_next_january_first,
    format_current_date,
    parse_and_format_datetime,
    sum_integers_with_timing,
)


class ChapterFiveTests(unittest.TestCase):
    """Check every Try It Yourself exercise and its input boundaries."""

    def test_exercise_1_formats_date_without_leading_zero(self) -> None:
        self.assertEqual(
            format_current_date(date(2026, 4, 19)),
            "Sunday, April 19, 2026",
        )

    def test_exercise_1_rejects_datetime_in_place_of_date(self) -> None:
        with self.assertRaises(TypeError):
            format_current_date(datetime(2026, 4, 19, 12, 0))

    def test_exercise_2_counts_to_next_year(self) -> None:
        self.assertEqual(days_until_next_january_first(date(2026, 4, 19)), 257)
        self.assertEqual(days_until_next_january_first(date(2024, 1, 1)), 366)
        self.assertEqual(days_until_next_january_first(date(2026, 12, 31)), 1)

    def test_exercise_3_parses_and_formats(self) -> None:
        parsed, displayed = parse_and_format_datetime("2024-07-04 09:30")
        self.assertEqual(parsed, datetime(2024, 7, 4, 9, 30))
        self.assertEqual(displayed, "4 Jul 2024, 9:30 AM")

    def test_exercise_3_handles_noon_and_midnight(self) -> None:
        _, midnight = parse_and_format_datetime("2024-07-04 00:05")
        _, noon = parse_and_format_datetime("2024-07-04 12:05")
        self.assertEqual(midnight, "4 Jul 2024, 12:05 AM")
        self.assertEqual(noon, "4 Jul 2024, 12:05 PM")

    def test_exercise_3_rejects_bad_input(self) -> None:
        with self.assertRaises(ValueError):
            parse_and_format_datetime("July 4, 2024")

    def test_exercise_4_uses_a_loop_and_reports_elapsed_time(self) -> None:
        clock_values = iter((10.0, 10.25))
        total, elapsed = sum_integers_with_timing(5, lambda: next(clock_values))
        self.assertEqual(total, 15)
        self.assertEqual(elapsed, 0.25)

    def test_exercise_4_default_target_has_expected_sum(self) -> None:
        total, elapsed = sum_integers_with_timing()
        self.assertEqual(total, 500_000_500_000)
        self.assertGreaterEqual(elapsed, 0.0)

    def test_exercise_4_rejects_negative_limit(self) -> None:
        with self.assertRaises(ValueError):
            sum_integers_with_timing(-1)


if __name__ == "__main__":
    unittest.main()
