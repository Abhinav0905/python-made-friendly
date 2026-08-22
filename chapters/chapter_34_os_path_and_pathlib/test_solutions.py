"""Tests for Chapter 34."""

import hashlib
import os
import tempfile
import unittest
from pathlib import Path

from . import solutions


class PathTests(unittest.TestCase):
    def test_q01_locations(self):
        original_cwd = Path.cwd()
        with tempfile.TemporaryDirectory() as directory:
            try:
                os.chdir(directory)
                cwd, home, notes = solutions.q01_path_locations()
                self.assertEqual(cwd, Path(directory).resolve())
                self.assertEqual(home, Path.home())
                self.assertEqual(notes, Path(directory).resolve() / "notes.txt")
            finally:
                os.chdir(original_cwd)

    def test_q02_compound_path_parts(self):
        self.assertEqual(
            solutions.q02_decompose_compound_path("/a/b/c/file.tar.gz"),
            (
                Path("/a/b/c"),
                "file.tar.gz",
                "file",
                "tar.gz",
                ["/a/b/c", "file.tar.gz"],
            ),
        )

    def test_q03_sorted_files_only(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "z.txt").write_text("z", encoding="utf-8")
            (root / "a.txt").write_text("a", encoding="utf-8")
            (root / "folder").mkdir()
            self.assertEqual(solutions.q03_list_files(root), ["a.txt", "z.txt"])

    def test_q04_recursive_python_file_sizes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "nested").mkdir()
            (root / "a.py").write_bytes(b"123")
            (root / "nested" / "b.py").write_bytes(b"12345")
            (root / "nested" / "skip.txt").write_bytes(b"x")
            sizes = {path.relative_to(root).as_posix(): size for path, size in solutions.q04_python_file_sizes(root)}
            self.assertEqual(sizes, {"a.py": 3, "nested/b.py": 5})

    def test_q05_safe_path_blocks_traversal_and_symlinks(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            parent = root / "public"
            outside = root / "private"
            parent.mkdir()
            outside.mkdir()
            self.assertEqual(
                solutions.q05_safe_path(parent, "reports/today.txt"),
                (parent / "reports" / "today.txt").resolve(),
            )
            self.assertIsNone(solutions.q05_safe_path(parent, "../private/key.txt"))
            link = parent / "jump"
            try:
                link.symlink_to(outside, target_is_directory=True)
            except (OSError, NotImplementedError):
                return
            self.assertIsNone(solutions.q05_safe_path(parent, "jump/key.txt"))

    def test_q06_lowercase_extensions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            original = root / "REPORT.TxT"
            original.write_text("report", encoding="utf-8")
            self.assertEqual(
                solutions.q06_lowercase_extensions(root),
                [("REPORT.TxT", "REPORT.txt")],
            )
            self.assertEqual((root / "REPORT.txt").read_text(encoding="utf-8"), "report")

    def test_q07_names_only_in_first_folder(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first, second = root / "first", root / "second"
            first.mkdir()
            second.mkdir()
            for name in ("only.txt", "shared.txt"):
                (first / name).write_text(name, encoding="utf-8")
            (second / "shared.txt").write_text("different", encoding="utf-8")
            self.assertEqual(solutions.q07_files_only_in(first, second), ["only.txt"])

    def test_q08_organizer_is_idempotent_and_numbers_collisions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "txt").mkdir()
            (root / "txt" / "report.txt").write_text("old", encoding="utf-8")
            (root / "report.txt").write_text("new", encoding="utf-8")
            (root / "photo.JPG").write_bytes(b"jpg")
            first_moves = solutions.q08_organize_idempotent(root)
            self.assertEqual(len(first_moves), 2)
            self.assertEqual((root / "txt" / "report_1.txt").read_text(encoding="utf-8"), "new")
            self.assertEqual((root / "jpg" / "photo.JPG").read_bytes(), b"jpg")
            self.assertEqual(solutions.q08_organize_idempotent(root), [])

    def test_q09_name_collisions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for folder in (root / "a", root / "b"):
                folder.mkdir()
                (folder / "same.txt").write_text("x", encoding="utf-8")
            (root / "unique.txt").write_text("x", encoding="utf-8")
            groups = solutions.q09_find_name_collisions(root)
            self.assertEqual(list(groups), ["same.txt"])
            self.assertEqual(len(groups["same.txt"]), 2)

    def test_q10_sha1_duplicates_are_chunked(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "a.bin").write_bytes(b"abcdef")
            (root / "nested").mkdir()
            (root / "nested" / "b.bin").write_bytes(b"abcdef")
            (root / "different.bin").write_bytes(b"abcdeg")
            expected = hashlib.sha1(b"abcdef").hexdigest()
            self.assertEqual(solutions.q10_sha1_file(root / "a.bin", 2), expected)
            groups = solutions.q10_duplicate_hashes(root, chunk_size=2)
            self.assertEqual(list(groups), [expected])
            self.assertEqual(len(groups[expected]), 2)


if __name__ == "__main__":
    unittest.main()
