"""Tests for Chapter 37 and its direct/import execution examples."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from . import solutions


EXAMPLES = Path(__file__).parent / "examples"


def run_python(arguments, cwd):
    return subprocess.run(
        [sys.executable] + [str(argument) for argument in arguments],
        cwd=str(cwd),
        check=True,
        text=True,
        capture_output=True,
    )


class NameSpecialVariableTests(unittest.TestCase):
    def test_q01_mymod_exists_and_prints_name(self):
        path = solutions.q01_mymod_path()
        self.assertTrue(path.is_file())
        self.assertIn("__name__", path.read_text(encoding="utf-8"))

    def test_q02_direct_and_imported_names(self):
        direct, imported = solutions.q02_observe_name_modes()
        self.assertEqual(direct, "__name__ is: __main__")
        self.assertEqual(imported, "__name__ is: mymod")

    def test_q03_prime_module_import_and_direct_modes(self):
        self.assertFalse(solutions.q03_is_prime(1))
        self.assertTrue(solutions.q03_is_prime(29))
        self.assertFalse(solutions.q03_is_prime(49))
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(solutions.q03_first_primes(), expected)
        imported = run_python(["-c", "import primes"], EXAMPLES)
        direct = run_python([EXAMPLES / "primes.py"], EXAMPLES)
        self.assertEqual(imported.stdout, "")
        self.assertEqual(direct.stdout, f"First 10 primes: {expected}\n")

    def test_q04_guard_delegates_to_testable_main(self):
        output = []
        expected = solutions.q04_primes_main(output.append)
        self.assertEqual(expected, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        self.assertEqual(output, [f"First 10 primes: {expected}"])
        source = (EXAMPLES / "primes.py").read_text(encoding="utf-8")
        self.assertIn('if __name__ == "__main__":\n    main()', source)

    def test_q05_calculator_library_and_cli(self):
        self.assertEqual(solutions.q05_calculate_expression("3 + 5"), 8.0)
        self.assertEqual(solutions.q05_calculate_expression(["9", "*", "7"]), 63.0)
        imported = run_python(["-c", "import calculator"], EXAMPLES)
        direct = run_python([EXAMPLES / "calculator.py", "3", "+", "5"], EXAMPLES)
        self.assertEqual(imported.stdout, "")
        self.assertEqual(direct.stdout, "3 + 5 = 8\n")

    def test_q06_temperature_library_and_cli(self):
        self.assertEqual(solutions.q06_celsius_to_fahrenheit(100), 212)
        self.assertEqual(solutions.q06_fahrenheit_to_celsius(32), 0)
        self.assertEqual(solutions.q06_convert(32, "f"), (0.0, "C"))
        result = run_python([EXAMPLES / "tempconvert.py", "32", "F"], EXAMPLES)
        self.assertEqual(result.stdout, "32.0 F = 0.0 C\n")

    def test_q07_statistics_library_and_cli(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "numbers.txt"
            path.write_text("1\n2\n3\n4\n", encoding="utf-8")
            mean, median, stdev = solutions.q07_file_stats(path)
            self.assertEqual((mean, median), (2.5, 2.5))
            self.assertAlmostEqual(stdev, 1.2909944487358056)
            result = run_python([EXAMPLES / "stats.py", path], Path(directory))
            self.assertEqual(
                result.stdout.splitlines(),
                ["Mean: 2.5000", "Median: 2.5000", "Stdev: 1.2910"],
            )

    def test_q08_logreader_import_and_cli_are_independent(self):
        line = (
            '192.168.1.42 - - [19/Apr/2026:14:30:45 +0000] '
            '"GET /home HTTP/1.1" 200 1234'
        )
        parsed = solutions.q08_parse_line(line)
        self.assertEqual(parsed["method"], "GET")
        with tempfile.TemporaryDirectory() as directory:
            log = Path(directory) / "access.log"
            log.write_text(line + "\n" + line.replace("200", "404") + "\n", encoding="utf-8")
            ips, statuses = solutions.q08_summarize_log(log)
            self.assertEqual(ips["192.168.1.42"], 2)
            self.assertEqual(statuses, {"200": 1, "404": 1})
            imported = run_python(["-c", "import logreader"], EXAMPLES)
            direct = run_python([EXAMPLES / "logreader.py", log], Path(directory))
            separate_test = run_python([EXAMPLES / "test_logreader.py"], EXAMPLES)
            self.assertEqual(imported.stdout, "")
            self.assertIn("192.168.1.42: 2", direct.stdout)
            self.assertEqual(separate_test.stdout, "parse_line: OK\n")

    def test_q09_file_locates_neighboring_data_from_another_cwd(self):
        reader = EXAMPLES / "data_reader.py"
        expected_path = EXAMPLES / "data.txt"
        self.assertEqual(solutions.q09_data_path("data.txt", reader), expected_path)
        self.assertEqual(
            solutions.q09_read_adjacent_data("data.txt", reader),
            "Data found beside data_reader.py.\n",
        )
        with tempfile.TemporaryDirectory() as directory:
            result = run_python([reader], Path(directory))
        self.assertEqual(result.stdout, "Data found beside data_reader.py.\n")

    def test_q10_earlier_module_is_now_dual_purpose(self):
        self.assertTrue(solutions.q10_is_palindrome("A man, a plan, a canal: Panama"))
        self.assertEqual(
            solutions.q10_find_palindromes(["level", "python", "Rotor"]),
            ["level", "Rotor"],
        )
        imported = run_python(["-c", "import palindrome"], EXAMPLES)
        direct = run_python(
            [EXAMPLES / "palindrome.py", "level", "python"], EXAMPLES
        )
        self.assertEqual(imported.stdout, "")
        self.assertEqual(direct.stdout.splitlines(), ["yes: level", "no: python"])


if __name__ == "__main__":
    unittest.main()
