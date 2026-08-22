"""Tests for the Chapter 6 solutions."""

import unittest

from chapters.chapter_06_basic_input_and_output.solutions import (
    BmiResult,
    average_of_three,
    bmi_with_category,
    build_greeting,
    format_bmi,
    format_profile,
    greeting_from_input,
    read_redirected_profile,
)


class ChapterSixTests(unittest.TestCase):
    """Check all four input and output exercises."""

    def test_exercise_1_builds_greeting(self) -> None:
        self.assertEqual(
            build_greeting("Ada", "Lovelace"),
            "Hello, Ada Lovelace! Nice to meet you.",
        )

    def test_exercise_1_reads_names_on_separate_lines(self) -> None:
        answers = iter(("Grace", "Hopper"))
        prompts = []

        def fake_input(prompt: str) -> str:
            prompts.append(prompt)
            return next(answers)

        self.assertEqual(
            greeting_from_input(fake_input),
            "Hello, Grace Hopper! Nice to meet you.",
        )
        self.assertEqual(prompts, ["First name? ", "Last name? "])

    def test_exercise_1_rejects_blank_name(self) -> None:
        with self.assertRaises(ValueError):
            build_greeting(" ", "Lovelace")

    def test_exercise_2_calculates_bmi_and_category(self) -> None:
        result = bmi_with_category(68.0, 1.75)
        self.assertAlmostEqual(result.value, 22.2040816327)
        self.assertEqual(result.category, "normal weight")
        self.assertEqual(
            format_bmi(result),
            "Your BMI is 22.2\nCategory: normal weight",
        )

    def test_exercise_2_category_boundaries(self) -> None:
        self.assertEqual(bmi_with_category(18.49, 1).category, "underweight")
        self.assertEqual(bmi_with_category(18.5, 1).category, "normal weight")
        self.assertEqual(bmi_with_category(25, 1).category, "overweight")
        self.assertEqual(bmi_with_category(30, 1).category, "obese")

    def test_exercise_2_rejects_impossible_height(self) -> None:
        with self.assertRaises(ValueError):
            bmi_with_category(70, 0)

    def test_exercise_3_averages_three_numbers(self) -> None:
        self.assertAlmostEqual(average_of_three("1 2.5 4"), 2.5)

    def test_exercise_3_accepts_general_whitespace(self) -> None:
        self.assertEqual(average_of_three("3\t6   9"), 6.0)

    def test_exercise_3_requires_exactly_three_numbers(self) -> None:
        with self.assertRaisesRegex(ValueError, "exactly three"):
            average_of_three("1 2")
        with self.assertRaisesRegex(ValueError, "exactly three"):
            average_of_three("1 2 3 4")

    def test_exercise_3_rejects_non_numeric_value(self) -> None:
        with self.assertRaises(ValueError):
            average_of_three("1 two 3")

    def test_exercise_4_reads_three_redirected_lines(self) -> None:
        answers = iter(("Alice", "25", "London"))
        profile = read_redirected_profile(lambda _prompt: next(answers))
        self.assertEqual(profile, ("Alice", "25", "London"))
        self.assertEqual(format_profile(profile), "Alice is 25 and lives in London.")

    def test_exercise_4_short_input_raises_eoferror(self) -> None:
        answers = iter(("Alice", "25"))

        def redirected_input(_prompt: str) -> str:
            try:
                return next(answers)
            except StopIteration:
                raise EOFError("EOF when reading a line")

        with self.assertRaises(EOFError):
            read_redirected_profile(redirected_input)

    def test_bmi_result_is_named(self) -> None:
        self.assertEqual(BmiResult(20.0, "normal weight").category, "normal weight")


if __name__ == "__main__":
    unittest.main()
