"""Tests for Chapter 19."""

import unittest

from chapters.chapter_19_dictionaries import solutions


class DictionaryTests(unittest.TestCase):
    def test_easy_exercises(self):
        capitals = {"France": "Paris", "Japan": "Tokyo"}
        self.assertEqual(solutions.q01_capital_lookup(capitals, "Japan"), "Tokyo")
        self.assertEqual(solutions.q01_capital_lookup(capitals, "Canada"), "not found")
        self.assertEqual(solutions.q02_format_items({"a": 1, "b": 2}), ["a: 1", "b: 2"])
        self.assertEqual(
            solutions.q03_update_and_remove(capitals, {"France": "Lyon", "Canada": "Ottawa"}, "Japan"),
            {"France": "Lyon", "Canada": "Ottawa"},
        )
        self.assertEqual(capitals, {"France": "Paris", "Japan": "Tokyo"})

    def test_medium_exercises(self):
        self.assertEqual(
            solutions.q04_word_frequencies("Red blue red GREEN red blue"),
            [("red", 3), ("blue", 2), ("green", 1)],
        )
        self.assertEqual(solutions.q05_glossary_lookup({"loop": "repeat"}, "loop"), "repeat")
        self.assertEqual(solutions.q05_glossary_lookup({}, "tuple"), "Unknown word: tuple")
        names = ["Alice", "Bob", "Anna", "", "Ben"]
        expected = {"A": ["Alice", "Anna"], "B": ["Bob", "Ben"]}
        self.assertEqual(solutions.q06_group_with_setdefault(names), expected)
        self.assertEqual(solutions.q06_group_with_defaultdict(names), expected)
        self.assertEqual(
            solutions.q07_student_averages({"Ada": [80, 100], "Linus": [75, 75]}),
            {"Ada": 90.0, "Linus": 75.0},
        )
        with self.assertRaises(ValueError):
            solutions.q07_student_averages({"Ada": []})

    def test_hard_exercises(self):
        self.assertEqual(
            solutions.q08_merge_dictionaries({"a": 1, "b": 2}, {"b": 20, "c": 3}),
            {"a": 1, "b": 20, "c": 3},
        )
        self.assertEqual(
            solutions.q09_invert({"a": 1, "b": 2, "c": 1}),
            {1: ["a", "c"], 2: ["b"]},
        )
        people = [
            {"name": "Ada", "age": 37, "city": "London"},
            {"name": "Grace", "age": 45, "city": "New York"},
            {"name": "Alan", "age": 41, "city": "London"},
            {"name": "Linus", "age": 54, "city": "New York"},
            {"name": "Guido", "age": 69, "city": "Amsterdam"},
            {"name": "Edsger", "age": 72, "city": "Amsterdam"},
        ]
        grouped = solutions.q10_people_by_city(people)
        self.assertEqual(set(grouped), {"London", "New York", "Amsterdam"})
        self.assertEqual([person["name"] for person in grouped["London"]], ["Ada", "Alan"])
        self.assertEqual([person["name"] for person in grouped["New York"]], ["Grace", "Linus"])
        self.assertEqual([person["name"] for person in grouped["Amsterdam"]], ["Guido", "Edsger"])
        people[0]["name"] = "changed"
        self.assertEqual(grouped["London"][0]["name"], "Ada")


if __name__ == "__main__":
    unittest.main()
