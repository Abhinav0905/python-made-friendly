"""Tests for Chapter 30."""

import importlib
import sys
import tempfile
import unittest
from pathlib import Path

from . import solutions


class ExceptionTests(unittest.TestCase):
    def test_integer_input_retries(self):
        answers = iter(["no", "4.2", "17"])
        messages = []
        value = solutions.q01_read_integer(
            input_fn=lambda prompt: next(answers),
            output_fn=messages.append,
        )
        self.assertEqual(value, 17)
        self.assertEqual(len(messages), 2)

    def test_data_file_is_only_created_once(self):
        with tempfile.TemporaryDirectory() as directory:
            first_path, first_created = solutions.q02_ensure_data_file(
                Path(directory), output_fn=lambda message: None
            )
            second_path, second_created = solutions.q02_ensure_data_file(
                Path(directory), output_fn=lambda message: None
            )
            self.assertEqual(first_path, second_path)
            self.assertTrue(first_created)
            self.assertFalse(second_created)
            self.assertEqual(first_path.read_text(encoding="utf-8"), "")

    def test_four_clause_demo(self):
        self.assertEqual(
            solutions.q03_four_clause_demo("8", output_fn=lambda message: None),
            (8, ["try", "else", "finally"]),
        )
        self.assertEqual(
            solutions.q03_four_clause_demo("bad", output_fn=lambda message: None),
            (None, ["try", "except", "finally"]),
        )

    def test_safe_divide(self):
        self.assertEqual(solutions.q04_safe_divide(9, 3), 3)
        self.assertIsNone(solutions.q04_safe_divide(9, 0))

    def test_robust_parse(self):
        self.assertEqual(solutions.q05_robust_parse("10"), 10)
        self.assertEqual(solutions.q05_robust_parse("10.5"), 10.5)
        with self.assertRaises(ValueError):
            solutions.q05_robust_parse("ten")

    def test_sum_valid_integers(self):
        self.assertEqual(solutions.q06_sum_valid_integers(["1", "bad", "3"]), 4)

    def test_first_value(self):
        data = {"second": None, "third": 3}
        self.assertIsNone(solutions.q07_first_value(data, "first", "second", "third"))
        self.assertEqual(solutions.q07_first_value(data, "first", "third"), 3)

    def test_retry_succeeds_after_failures(self):
        calls = []
        delays = []

        def flaky():
            calls.append(1)
            if len(calls) < 3:
                raise RuntimeError("not yet")
            return "done"

        self.assertEqual(
            solutions.q08_retry(flaky, attempts=3, delay=0.25, sleep_fn=delays.append),
            "done",
        )
        self.assertEqual(len(calls), 3)
        self.assertEqual(delays, [0.25, 0.25])

    def test_retry_reraises_final_error(self):
        with self.assertRaisesRegex(RuntimeError, "always"):
            solutions.q08_retry(
                lambda: (_ for _ in ()).throw(RuntimeError("always")),
                attempts=2,
                delay=0,
                sleep_fn=lambda delay: None,
            )

    def test_timer_uses_finally(self):
        readings = iter([10.0, 10.125])
        messages = []
        with solutions.q09_timer(messages.append, lambda: next(readings)):
            pass
        self.assertEqual(messages, ["Elapsed: 0.125000 seconds"])

        failure_readings = iter([20.0, 20.25])
        failure_messages = []
        with self.assertRaisesRegex(RuntimeError, "inside block"):
            with solutions.q09_timer(
                failure_messages.append,
                lambda: next(failure_readings),
            ):
                raise RuntimeError("inside block")
        self.assertEqual(failure_messages, ["Elapsed: 0.250000 seconds"])

    @unittest.skipIf(sys.version_info < (3, 11), "exception groups require Python 3.11")
    def test_exception_group_demo(self):
        module = importlib.import_module(
            "chapters.chapter_30_exceptions.exception_groups_demo"
        )
        self.assertEqual(module.handle_group(), ["ValueError", "TypeError"])


if __name__ == "__main__":
    unittest.main()
