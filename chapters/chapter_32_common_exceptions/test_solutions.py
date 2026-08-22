"""Tests for Chapter 32."""

import tempfile
import unittest
from pathlib import Path

from . import solutions


class CommonExceptionTests(unittest.TestCase):
    def test_five_exception_types(self):
        captured = solutions.q01_common_exception_messages()
        names = [name for name, message in captured]
        self.assertEqual(
            names,
            ["ValueError", "TypeError", "IndexError", "KeyError", "ZeroDivisionError"],
        )
        self.assertTrue(all(message for name, message in captured))

    def test_lbyl_and_eafp_items(self):
        items = ["a", "b", "c"]
        for function in (solutions.q02_get_item_lbyl, solutions.q02_get_item_eafp):
            self.assertEqual(function(items, 1), "b")
            self.assertEqual(function(items, -1), "c")
            self.assertEqual(function(items, 9, "missing"), "missing")

    def test_integer_reader(self):
        answers = iter(["bad", "7"])
        messages = []
        self.assertEqual(
            solutions.q03_read_integer(
                input_fn=lambda prompt: next(answers), output_fn=messages.append
            ),
            7,
        )
        self.assertEqual(len(messages), 1)

    def test_file_writer_success_and_errors(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "answer.txt"
            self.assertIn("Wrote 5", solutions.q04_write_user_file(path, "hello"))
            self.assertEqual(path.read_text(encoding="utf-8"), "hello")
            self.assertIn("directory", solutions.q04_write_user_file(Path(directory), "x"))
            missing_parent = Path(directory) / "missing" / "answer.txt"
            self.assertIn(
                "Parent folder not found",
                solutions.q04_write_user_file(missing_parent, "x"),
            )

        def denied(*args, **kwargs):
            raise PermissionError("no")

        self.assertIn("Permission denied", solutions.q04_write_user_file("x", "y", denied))

    def test_safe_divide(self):
        self.assertEqual(solutions.q05_safe_divide(8, 2), 4)
        self.assertIsNone(solutions.q05_safe_divide(8, 0))
        self.assertIsNone(solutions.q05_safe_divide("8", 2))

    def test_json_config(self):
        with tempfile.TemporaryDirectory() as directory:
            good = Path(directory) / "good.json"
            good.write_text('{"active": true}', encoding="utf-8")
            bad = Path(directory) / "bad.json"
            bad.write_text("not json", encoding="utf-8")
            self.assertEqual(solutions.q06_read_config(good), {"active": True})
            self.assertIsNone(solutions.q06_read_config(bad))
            self.assertIsNone(solutions.q06_read_config(Path(directory) / "missing.json"))

    def test_recursion_report(self):
        limit, name, message = solutions.q07_recursion_report()
        self.assertGreater(limit, 100)
        self.assertEqual(name, "RecursionError")
        self.assertTrue(message)

    def test_encoding_fallback_and_wrapped_error(self):
        with tempfile.TemporaryDirectory() as directory:
            latin = Path(directory) / "latin.txt"
            latin.write_bytes("caf\xe9".encode("latin-1"))
            self.assertEqual(solutions.q08_resilient_read(latin), "caf\xe9")
            missing = Path(directory) / "missing.txt"
            with self.assertRaises(solutions.FileReadError) as caught:
                solutions.q08_resilient_read(missing)
            self.assertIsInstance(caught.exception.original_error, FileNotFoundError)

    def test_directory_summary(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "two.txt").write_text("one\ntwo\n", encoding="utf-8")
            (root / "bad.bin").write_bytes(b"\xff")
            (root / "folder").mkdir()
            summary = solutions.q09_summarize_directory(root)
            self.assertIn(("two.txt", 2), summary["ok"])
            self.assertEqual(summary["errors"][0][0], "bad.bin")
            self.assertEqual(summary["skipped"], ["folder"])


if __name__ == "__main__":
    unittest.main()
