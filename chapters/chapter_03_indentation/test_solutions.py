"""Tests for Chapter 3 exercises."""

import unittest

from chapters.chapter_03_indentation import solutions


class Chapter03Tests(unittest.TestCase):
    def test_q01_reports_and_fixes_missing_indentation(self):
        result = solutions.q01_missing_indentation_error()
        self.assertIn("IndentationError", result)
        self.assertIn("indented block", result)
        self.assertEqual(solutions.q01_fixed_conditional(), "yes")

    def test_q02_uses_two_nesting_levels(self):
        self.assertEqual(
            solutions.q02_describe_names(["Ada", "Grace"]),
            [
                "Processing Ada...",
                "  Ada is a short name",
                "  It has only 3 characters",
                "Processing Grace...",
                "  Grace is a long name",
                "  It has 5 characters",
                "Done.",
            ],
        )

    def test_q03_stub_then_completed_function(self):
        self.assertIsNone(solutions.q03_function_stub())
        self.assertEqual(solutions.q03_completed_function("Ada"), "Hello, Ada!")

    def test_q04_editor_settings(self):
        self.assertEqual(
            solutions.q04_whitespace_setting("VS Code"),
            '"editor.renderWhitespace": "all"',
        )
        self.assertEqual(solutions.q04_whitespace_setting("Vim"), ":set list")
        with self.assertRaises(ValueError):
            solutions.q04_whitespace_setting("Unknown")


if __name__ == "__main__":
    unittest.main()
