"""Tests for Chapter 18."""

import unittest

from chapters.chapter_18_tuples import solutions


class TupleTests(unittest.TestCase):
    def test_easy_exercises(self):
        self.assertEqual(solutions.q01_prime_tuple_details(), ((2, 3, 5, 7, 11), 3, 11, 5))
        person = ("Alice", 30, "Engineer")
        self.assertEqual(solutions.q02_unpack_person(person), person)
        self.assertEqual(solutions.q03_swap("left", "right"), ("right", "left"))

    def test_manual_stats_and_formatting(self):
        self.assertEqual(solutions.q04_manual_stats([3, 7, 1, 9, 4]), (1, 9, 4.8))
        self.assertEqual(solutions.q04_manual_stats([]), (None, None, None))
        self.assertEqual(
            solutions.q05_format_scores([("Ada", 91), ("Grace", 100)]),
            ["Ada    91", "Grace  100"],
        )

    def test_named_tuple_and_ranking(self):
        people = [
            solutions.Person("Ada", 37, "ada@example.com"),
            solutions.Person("Linus", 54, "linus@example.com"),
        ]
        self.assertEqual(
            solutions.q06_name_email_pairs(people),
            [("Ada", "ada@example.com"), ("Linus", "linus@example.com")],
        )
        records = [("Charlie", 92), ("Bob", 85), ("Alice", 92)]
        self.assertEqual(
            solutions.q07_rank_scores(records),
            [("Alice", 92), ("Charlie", 92), ("Bob", 85)],
        )

    def test_hard_exercises(self):
        self.assertEqual(
            solutions.q08_extended_unpack([1, 2, 3, 4, 5, 6]),
            (1, 2, [3, 4, 5], 6),
        )
        with self.assertRaises(ValueError):
            solutions.q08_extended_unpack([1, 2, 3, 4, 5])
        first, second, distance = solutions.q09_farthest_points([(0, 0), (3, 4), (1, 1)])
        self.assertEqual((first, second), ((0, 0), (3, 4)))
        self.assertEqual(distance, 5.0)
        rectangle = solutions.Rectangle(3, 4)
        self.assertEqual(solutions.q10_rectangle_area(rectangle), 12)
        self.assertEqual(solutions.q10_rectangle_perimeter(rectangle), 14)


if __name__ == "__main__":
    unittest.main()
