"""Tests for Chapter 20."""

import unittest

from chapters.chapter_20_sets import solutions


class SetTests(unittest.TestCase):
    def test_easy_exercises(self):
        values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.assertEqual(solutions.q01_unique_count(values), 7)
        self.assertEqual(solutions.q02_common_letters("programming", "language"), {"a", "g", "n"})
        self.assertEqual(
            solutions.q03_set_operations({1, 2, 3}, {3, 4}),
            {
                "union": {1, 2, 3, 4},
                "intersection": {3},
                "first_only": {1, 2},
                "second_only": {4},
            },
        )

    def test_medium_exercises(self):
        self.assertEqual(
            solutions.q04_compare_sentences("The cat sat", "the dog sat"),
            ({"the", "sat"}, {"cat"}, {"dog"}),
        )
        self.assertEqual(
            solutions.q05_deduplicate_ordered(["a@x", "b@x", "a@x"]),
            ["a@x", "b@x"],
        )
        common, needed = solutions.q06_course_summary(
            {"Ada": {"math", "art"}, "Linus": {"math", "computing"}}
        )
        self.assertEqual(common, {"math"})
        self.assertEqual(needed, {"math", "art", "computing"})
        self.assertEqual(solutions.q06_course_summary({}), (set(), set()))
        self.assertTrue(solutions.q07_has_all_vowels("Education"))
        self.assertFalse(solutions.q07_has_all_vowels("Python"))

    def test_hard_exercises(self):
        dictionary = {"the", "quick", "brown", "fox"}
        self.assertEqual(
            solutions.q08_spell_check(dictionary, "The quikc,brown fox!"),
            {"quikc"},
        )
        self.assertEqual(
            solutions.q09_exactly_one({1, 2, 3}, {3, 4, 5}, {3, 5, 6}),
            {1, 2, 4, 6},
        )
        original = {frozenset({"Ada", "Linus"}): "Python"}
        updated, course, rows = solutions.q10_enrollment_actions(
            original, {"Grace", "Alan"}, "Math", {"Linus", "Ada"}
        )
        self.assertEqual(course, "Python")
        self.assertEqual(updated[frozenset({"Grace", "Alan"})], "Math")
        self.assertEqual(
            rows,
            [(('Ada', 'Linus'), 'Python'), (('Alan', 'Grace'), 'Math')],
        )
        self.assertEqual(len(original), 1)


if __name__ == "__main__":
    unittest.main()
