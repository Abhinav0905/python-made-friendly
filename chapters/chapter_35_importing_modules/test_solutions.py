"""Tests for Chapter 35."""

import subprocess
import sys
import unittest
from datetime import datetime
from pathlib import Path

from . import solutions


EXAMPLES = Path(__file__).parent / "examples"


def run_python(arguments, cwd):
    return subprocess.run(
        [sys.executable] + list(arguments),
        cwd=str(cwd),
        check=True,
        text=True,
        capture_output=True,
    )


class ImportingModulesTests(unittest.TestCase):
    def test_q01_math_values(self):
        sqrt_two, pi, factorial_ten = solutions.q01_math_values()
        self.assertAlmostEqual(sqrt_two, 2 ** 0.5)
        self.assertAlmostEqual(pi, 3.141592653589793)
        self.assertEqual(factorial_ten, 3628800)

    def test_q02_directly_imported_choice(self):
        seen = []

        def choose_last(items):
            seen.append(items)
            return items[-1]

        foods = ["pizza", "sushi", "tacos"]
        self.assertEqual(solutions.q02_pick_food(foods, choose_last), "tacos")
        self.assertEqual(seen, [foods])

    def test_q03_neighboring_greetings_module(self):
        project = EXAMPLES / "q03_greetings"
        result = run_python(["main.py"], project)
        self.assertEqual(result.stdout, "Hello, Ada!\n")

    def test_q04_calculator_imports_and_all_operations(self):
        project = EXAMPLES / "q04_calculator"
        result = run_python(["main.py"], project)
        self.assertEqual(result.stdout.splitlines(), ["15", "5", "50", "2.0"])
        with self.assertRaises(ValueError):
            solutions.q04_divide(1, 0)

    def test_q05_guard_runs_demo_only_on_direct_execution(self):
        project = EXAMPLES / "q04_calculator"
        imported = run_python(["-c", "import calculator"], project)
        direct = run_python(["calculator.py"], project)
        self.assertEqual(imported.stdout, "")
        self.assertIn("Calculator Demo", direct.stdout)
        self.assertEqual(solutions.q05_calculator_demo()["multiply"], 50)

    def test_q06_datetime_module_alias(self):
        fixed = datetime(2026, 8, 22, 14, 5, 9)
        self.assertEqual(solutions.q06_current_time(lambda: fixed), "14:05:09")

    def test_q07_requests_style_demo_uses_only_injected_getter(self):
        calls = []

        class FakeResponse:
            status_code = 200
            text = "Python"
            headers = {"content-type": "text/html"}

            @staticmethod
            def raise_for_status():
                return None

        def fake_get(url, timeout):
            calls.append((url, timeout))
            return FakeResponse()

        self.assertEqual(
            solutions.q07_fetch_summary(fake_get),
            {"status_code": 200, "content_length": 6, "content_type": "text/html"},
        )
        self.assertEqual(calls, [("https://www.python.org", 10)])

    def test_q08_three_file_project(self):
        project = EXAMPLES / "q08_three_file_project"
        result = run_python(["main.py"], project)
        self.assertEqual(
            result.stdout.splitlines(),
            ["LOVELACE, Ada", "User('Ada', 'Lovelace')"],
        )

    def test_q09_sys_path_report_and_temporary_runtime_import(self):
        report = solutions.q09_sys_path_report(["", "/tmp/site-packages"])
        self.assertEqual(report[0][2], "current working directory")
        self.assertEqual(report[1][2], "installed third-party packages")

        module_name = "my_module"
        original_path = sys.path[:]
        previous = sys.modules.get(module_name)
        module = solutions.q09_import_from_directory(
            EXAMPLES / "q09_runtime_module", module_name
        )
        self.assertEqual(module.public_answer(), 42)
        self.assertEqual(sys.path, original_path)
        self.assertIs(sys.modules.get(module_name), previous)

    def test_q10_importlib_inspection(self):
        docstring, functions = solutions.q10_inspect_module(
            "chapters.chapter_35_importing_modules.solutions"
        )
        self.assertIn("Chapter 35", docstring)
        self.assertIn("q01_math_values", functions)
        self.assertNotIn("_private", functions)


if __name__ == "__main__":
    unittest.main()
