"""Tests for Chapter 41."""

import unittest

from . import solutions


class RegularExpressionTests(unittest.TestCase):
    def test_find_numbers(self):
        self.assertEqual(
            solutions.q01_find_numbers("abc 42 def 99 ghi 123"),
            ["42", "99", "123"],
        )

    def test_capitalized_words(self):
        self.assertEqual(
            solutions.q02_capitalized_words("Alice and Bob went to Chicago."),
            ["Alice", "Bob", "Chicago"],
        )

    def test_collapse_whitespace(self):
        self.assertEqual(solutions.q03_collapse_whitespace("a\t b\n c"), "a b c")
        self.assertEqual(solutions.q03_collapse_whitespace("  a  "), " a ")

    def test_phone_validation(self):
        self.assertTrue(solutions.q04_is_valid_phone("555-1234"))
        self.assertFalse(solutions.q04_is_valid_phone("55-1234"))
        self.assertFalse(solutions.q04_is_valid_phone("555-12345"))

    def test_domain_extraction(self):
        self.assertEqual(solutions.q05_extract_domain("ada@example.com"), "example.com")
        self.assertEqual(
            solutions.q05_extract_domain("user@mail.example.org"),
            "mail.example.org",
        )
        self.assertIsNone(solutions.q05_extract_domain("missing-at-sign"))

    def test_four_digit_numbers(self):
        text = "1999, 2000, and 2024 count; 12345 does not."
        self.assertEqual(solutions.q06_four_digit_numbers(text), ["1999", "2000", "2024"])

    def test_digit_redaction(self):
        self.assertEqual(
            solutions.q07_redact_digits("My number is 555-1234"),
            "My number is XXX-XXXX",
        )

    def test_named_date_groups(self):
        self.assertEqual(
            solutions.q08_date_parts("2026-04-19"),
            {"year": "2026", "month": "04", "day": "19"},
        )
        self.assertIsNone(solutions.q08_date_parts("19/04/2026"))

    def test_log_summary(self):
        lines = [
            '192.168.1.42 - - [date] "GET /home HTTP/1.1" 200 1234',
            '10.0.0.5 - - [date] "POST /login HTTP/1.1" 302 0',
            '192.168.1.42 - - [date] "GET /about HTTP/1.1" 200 567',
            "not a log line",
        ]
        addresses, statuses = solutions.q09_summarize_logs(lines)
        self.assertEqual(addresses, {"192.168.1.42": 2, "10.0.0.5": 1})
        self.assertEqual(statuses, {"200": 2, "302": 1})

    def test_tokenizer(self):
        self.assertEqual(
            solutions.q10_tokenize("3 + 4*(2-1)"),
            ["3", "+", "4", "*", "(", "2", "-", "1", ")"],
        )
        with self.assertRaises(ValueError):
            solutions.q10_tokenize("2 + name")


if __name__ == "__main__":
    unittest.main()
