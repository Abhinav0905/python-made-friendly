"""Tests for Chapter 23."""

import sys
import unittest

from chapters.chapter_23_enumerations import solutions


class EnumerationTests(unittest.TestCase):
    def test_weekday_exercises(self):
        members = solutions.q01_weekday_members()
        self.assertEqual([name for name, _ in members], [
            "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"
        ])
        self.assertEqual(len({value for _, value in members}), 7)
        self.assertFalse(solutions.q02_is_weekend(solutions.Weekday.MONDAY))
        self.assertTrue(solutions.q02_is_weekend(solutions.Weekday.SATURDAY))
        self.assertEqual(
            solutions.q03_lookup_friday(),
            (solutions.Weekday.FRIDAY, solutions.Weekday.FRIDAY),
        )

    def test_suit_status_and_log_level(self):
        self.assertTrue(solutions.q04_is_red(solutions.Suit.HEARTS))
        self.assertFalse(solutions.q04_is_red(solutions.Suit.CLUBS))
        self.assertEqual(
            solutions.q05_describe_status(solutions.Status.PAID),
            "Payment received; preparing to ship",
        )
        with self.assertRaises(ValueError):
            solutions.q05_describe_status("PAID")
        self.assertEqual(
            solutions.q06_log(solutions.LogLevel.ERROR, "failed"),
            "[ERROR] failed",
        )
        self.assertEqual(solutions.LogLevel.ERROR, "ERROR")

    def test_permissions(self):
        permissions = solutions.Permission.READ
        permissions = solutions.q07_set_permission(permissions, solutions.Permission.WRITE)
        self.assertTrue(solutions.q07_has_permission(permissions, solutions.Permission.READ))
        self.assertTrue(solutions.q07_has_permission(permissions, solutions.Permission.WRITE))
        permissions = solutions.q07_clear_permission(permissions, solutions.Permission.READ)
        self.assertFalse(solutions.q07_has_permission(permissions, solutions.Permission.READ))

    def test_unique_alias_and_directions(self):
        error, is_alias, names = solutions.q08_unique_and_alias_demo()
        self.assertIn("duplicate values", error)
        self.assertTrue(is_alias)
        self.assertEqual(names, ["PENDING", "PAID", "DELIVERED"])
        self.assertEqual(solutions.q09_direction_values()["NORTH"], (0, -1))
        self.assertEqual(solutions.q09_move(5, 5, solutions.Direction.EAST), (6, 5))

    @unittest.skipIf(sys.version_info < (3, 11), "match and StrEnum examples require Python 3.11+")
    def test_literal_modern_examples(self):
        from chapters.chapter_23_enumerations import modern_examples

        self.assertEqual(
            modern_examples.q05_describe_status_match(solutions.Status.SHIPPED),
            "On the way",
        )
        self.assertEqual(
            modern_examples.q06_log_strenum(modern_examples.LogLevel.WARNING, "Disk space low"),
            "[WARNING] Disk space low",
        )
        self.assertEqual(modern_examples.LogLevel.ERROR, "ERROR")


if __name__ == "__main__":
    unittest.main()
