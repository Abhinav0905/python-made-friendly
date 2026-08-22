"""Tests for Chapter 33."""

import csv
import tempfile
import unittest
from datetime import datetime
from pathlib import Path

from . import solutions


class FilesAndFoldersTests(unittest.TestCase):
    def test_q01_create_read_print(self):
        calls = []

        def capture(value, **kwargs):
            calls.append((value, kwargs))

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "hello.txt"
            result = solutions.q01_create_read_print(path, capture)
            self.assertEqual(result, "Hello, world\n")
            self.assertEqual(path.read_text(encoding="utf-8"), result)
            self.assertEqual(calls, [(result, {"end": ""})])

    def test_q02_numbered_lines(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "notes.txt"
            path.write_text("alpha\nbeta", encoding="utf-8")
            self.assertEqual(
                solutions.q02_numbered_lines(path),
                ["   1: alpha", "   2: beta"],
            )

    def test_q03_append_timestamp(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "log.txt"
            first = datetime(2026, 8, 22, 9, 30, 15)
            second = datetime(2026, 8, 22, 9, 31, 0)
            solutions.q03_append_timestamp(path, first)
            solutions.q03_append_timestamp(path, second)
            self.assertEqual(
                path.read_text(encoding="utf-8"),
                "[2026-08-22 09:30:15] executed\n"
                "[2026-08-22 09:31:00] executed\n",
            )

    def test_q04_reverse_lines_and_preserve_endings(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "input.txt"
            destination = Path(directory) / "output.txt"
            source.write_bytes(b"abc\r\ndef\nlast")
            solutions.q04_reverse_lines(source, destination)
            self.assertEqual(destination.read_bytes(), b"cba\r\nfed\ntsal")

    def test_q05_longest_and_blank_lines(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.txt"
            path.write_text("short\n   \na longer line\n\n", encoding="utf-8")
            self.assertEqual(solutions.q05_analyze_file(path), ("a longer line", 2))

    def test_q06_merge_alternating_and_drain(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first, second, output = root / "a", root / "b", root / "merged"
            first.write_text("a1\na2\na3\n", encoding="utf-8")
            second.write_text("b1\n", encoding="utf-8")
            solutions.q06_merge_alternating(first, second, output)
            self.assertEqual(output.read_text(encoding="utf-8"), "a1\nb1\na2\na3\n")

    def test_q07_word_counts_are_case_sensitive(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "words.txt"
            path.write_text("Python python Python code code", encoding="utf-8")
            self.assertEqual(
                solutions.q07_word_frequencies(path),
                [("Python", 2), ("code", 2), ("python", 1)],
            )

    def test_q08_csv_average_and_strictly_above(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, output = root / "scores.csv", root / "result.csv"
            source.write_text('"Doe, Ada",90\nBen,80\nCy,70\n', encoding="utf-8")
            self.assertEqual(solutions.q08_process_scores(source, output), 80.0)
            with output.open(encoding="utf-8", newline="") as result_file:
                self.assertEqual(
                    list(csv.reader(result_file)),
                    [["Doe, Ada", "90", "yes"], ["Ben", "80", "no"], ["Cy", "70", "no"]],
                )

    def test_q09_size_by_extension(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "nested").mkdir()
            (root / "a.TXT").write_bytes(b"123")
            (root / "nested" / "b.txt").write_bytes(b"12345")
            (root / "plain").write_bytes(b"12")
            self.assertEqual(
                solutions.q09_size_by_extension(root),
                {"(no extension)": 2, ".txt": 8},
            )

    def test_q10_tail_new_lines_without_waiting_forever(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "growing.log"
            path.write_text("old\n", encoding="utf-8")
            calls = []

            def append_on_first_sleep(_seconds):
                calls.append(1)
                if len(calls) == 1:
                    with path.open("a", encoding="utf-8") as output_file:
                        output_file.write("new\n")

            lines = list(
                solutions.q10_tail_lines(
                    path,
                    sleep_fn=append_on_first_sleep,
                    stop_after_idle_polls=2,
                )
            )
            self.assertEqual(lines, ["new\n"])


if __name__ == "__main__":
    unittest.main()
