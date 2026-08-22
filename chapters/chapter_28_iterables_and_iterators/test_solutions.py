"""Tests for Chapter 28."""

import tempfile
import unittest
from itertools import islice
from pathlib import Path

from chapters.chapter_28_iterables_and_iterators import solutions


class IterableAndIteratorTests(unittest.TestCase):
    def test_easy_exercises(self):
        self.assertEqual(solutions.q01_step_characters(), list("hello"))
        self.assertEqual(solutions.q01_step_characters(""), [])
        self.assertEqual(solutions.q02_sum_of_squares(), 385)
        iterator = solutions.q03_chain_iterator()
        self.assertIs(iter(iterator), iterator)
        self.assertEqual(list(iterator), [1, 2, 3, 4, 5, "a", "b", "c"])
        self.assertEqual(list(iterator), [])

    def test_medium_exercises(self):
        self.assertEqual(list(solutions.q04_evens_up_to(10)), [0, 2, 4, 6, 8, 10])
        self.assertEqual(list(solutions.q04_evens_up_to(-1)), [])
        self.assertEqual(
            list(islice(solutions.q05_fibonacci(), 10)),
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34],
        )
        self.assertEqual(list(solutions.q06_running_sum([1, 2, 3, 4])), [1, 3, 6, 10])
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "app.log"
            path.write_text("INFO start\nERROR failed\nDEBUG retry\nERROR stopped\n", encoding="utf-8")
            self.assertEqual(
                list(solutions.q07_error_lines(path)),
                ["ERROR failed", "ERROR stopped"],
            )

    def test_hard_exercises(self):
        multiples = solutions.q08_first_hundred_multiples_of_seven()
        self.assertEqual(list(multiples), list(range(7, 701, 7)))
        self.assertEqual(list(multiples), [])
        self.assertEqual(
            list(solutions.q09_group([1, 2, 3, 4, 5, 6, 7], 3)),
            [(1, 2, 3), (4, 5, 6), (7,)],
        )
        with self.assertRaises(ValueError):
            list(solutions.q09_group([1, 2], 0))
        self.assertEqual(
            list(solutions.q10_window([1, 2, 3, 4, 5], 3)),
            [(1, 2, 3), (2, 3, 4), (3, 4, 5)],
        )
        self.assertEqual(list(solutions.q10_window([1, 2], 3)), [])
        with self.assertRaises(ValueError):
            list(solutions.q10_window([1, 2], 0))


if __name__ == "__main__":
    unittest.main()
