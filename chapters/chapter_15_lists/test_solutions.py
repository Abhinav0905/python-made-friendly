"""Tests for Chapter 15 exercises."""

import unittest

from chapters.chapter_15_lists import solutions


class Chapter15Tests(unittest.TestCase):
    def test_q01_first_middle_last(self):
        numbers, selected = solutions.q01_first_middle_last()
        self.assertEqual(numbers, list(range(1, 11)))
        self.assertEqual(selected, (1, 5, 10))

    def test_q02_sorted_copy_preserves_original(self):
        original, sorted_names = solutions.q02_sorted_names(["Zoe", "Alice", "Bob"])
        self.assertEqual(original, ["Zoe", "Alice", "Bob"])
        self.assertEqual(sorted_names, ["Alice", "Bob", "Zoe"])

    def test_q03_all_modification_states(self):
        self.assertEqual(
            solutions.q03_modify_list(),
            [
                [5, 1, 4, 2, 8, 3],
                [7, 5, 1, 4, 2, 8, 3],
                [7, 5, 1, 2, 8, 3],
            ],
        )

    def test_q04_statistics_and_input_validation(self):
        self.assertEqual(
            solutions.q04_number_statistics([10, 1, 9, 2, 8, 3, 7, 4, 6, 5]),
            {"smallest": 1, "largest": 10, "average": 5.5, "median": 5.5},
        )
        with self.assertRaises(ValueError):
            solutions.q04_number_statistics([1, 2])
        with self.assertRaises(ValueError):
            solutions.q04_number_statistics([0] + list(range(1, 10)))
        with self.assertRaises(TypeError):
            solutions.q04_number_statistics([1.5] + list(range(2, 11)))

    def test_q05_filters_long_words(self):
        self.assertEqual(solutions.q05_long_words(["pear", "banana", "orange", "fig"]), ["banana", "orange"])

    def test_q06_sorts_by_length_then_alphabetically(self):
        self.assertEqual(
            solutions.q06_sort_words(["pear", "banana", "plum", "orange", "fig"]),
            ["banana", "orange", "pear", "plum", "fig"],
        )

    def test_q07_removes_duplicates_without_reordering(self):
        self.assertEqual(solutions.q07_remove_duplicates([3, 1, 3, 2, 1]), [3, 1, 2])
        self.assertEqual(solutions.q07_remove_duplicates([[1], [1], [2]]), [[1], [2]])

    def test_q08_rotates_in_both_directions(self):
        self.assertEqual(solutions.q08_rotate([1, 2, 3, 4, 5], 2), [3, 4, 5, 1, 2])
        self.assertEqual(solutions.q08_rotate([1, 2, 3, 4, 5], -1), [5, 1, 2, 3, 4])
        self.assertEqual(solutions.q08_rotate([1, 2, 3], 7), [2, 3, 1])
        self.assertEqual(solutions.q08_rotate([], 3), [])

    def test_q09_second_largest_distinct_value(self):
        self.assertEqual(solutions.q09_second_largest_unique([10, 5, 10, 8, 3]), 8)
        with self.assertRaises(ValueError):
            solutions.q09_second_largest_unique([4, 4])

    def test_q10_shallow_and_deep_copy_behavior(self):
        result = solutions.q10_copy_trap()
        self.assertEqual(result["shallow_original"][0][0], 99)
        self.assertEqual(result["shallow_copy"][0][0], 99)
        self.assertEqual(result["deep_original"][0][0], 1)
        self.assertEqual(result["deep_copy"][0][0], 99)


if __name__ == "__main__":
    unittest.main()
