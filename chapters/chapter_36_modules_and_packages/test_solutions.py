"""Tests for Chapter 36 and its example package trees."""

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from . import solutions


EXAMPLES = Path(__file__).parent / "examples"


def run_python(arguments, cwd, pythonpath=None):
    environment = os.environ.copy()
    if pythonpath is not None:
        prior = environment.get("PYTHONPATH")
        environment["PYTHONPATH"] = str(pythonpath) + (os.pathsep + prior if prior else "")
    return subprocess.run(
        [sys.executable] + list(arguments),
        cwd=str(cwd),
        env=environment,
        check=True,
        text=True,
        capture_output=True,
    )


class ModulesAndPackagesTests(unittest.TestCase):
    def test_q01_geometry_modules(self):
        project = EXAMPLES / "geometry_project"
        result = run_python(["main.py"], project, project / "src")
        self.assertEqual(result.stdout.splitlines(), ["78.5398", "12"])
        self.assertAlmostEqual(solutions.q01_circle_area(5), 78.53981633974483)
        self.assertEqual(solutions.q01_rectangle_area(3, 4), 12)

    def test_q02_geometry_friendly_reexports(self):
        project = EXAMPLES / "geometry_project"
        code = "from geometry import circle_area, rectangle_area; print(round(circle_area(2), 5), rectangle_area(3, 4))"
        result = run_python(["-c", code], project, project / "src")
        self.assertEqual(result.stdout, "12.56637 12\n")
        self.assertEqual(solutions.q02_friendly_geometry_areas(1, 2, 3)[1], 6)

    def test_q03_circle_guarded_demo(self):
        project = EXAMPLES / "geometry_project"
        circle = project / "src" / "geometry" / "circle.py"
        imported = run_python(["-c", "import geometry.circle"], project, project / "src")
        direct = run_python([str(circle)], project)
        self.assertEqual(imported.stdout, "")
        self.assertIn("Circle Demo", direct.stdout)
        self.assertIn("Circumference: 31.42", direct.stdout)

    def test_q04_shapes_3d_and_top_level_exports(self):
        project = EXAMPLES / "geometry_project"
        code = "from geometry import sphere_volume, cube_volume; print(round(sphere_volume(3), 3), cube_volume(3))"
        result = run_python(["-c", code], project, project / "src")
        self.assertEqual(result.stdout, "113.097 27\n")
        self.assertAlmostEqual(solutions.q04_sphere_volume(3), 113.09733552923254)

    def test_q05_all_excludes_private_helper(self):
        project = EXAMPLES / "geometry_project"
        code = "from geometry.circle import *; print(sorted(name for name in globals() if name in {'area', 'circumference', '_diameter'}))"
        result = run_python(["-c", code], project, project / "src")
        self.assertEqual(result.stdout, "['area', 'circumference']\n")
        self.assertEqual(solutions.q05_public_circle_names(), ("area", "circumference"))

    def test_q06_calculator_flat_package_imports(self):
        project = EXAMPLES / "calculator_project"
        code = "from calculator import add, subtract, multiply, divide; print(add(3, 4), subtract(7, 2), multiply(3, 5), divide(8, 2))"
        result = run_python(["-c", code], project, project / "src")
        self.assertEqual(result.stdout, "7 5 15 4.0\n")
        self.assertEqual(solutions.q06_calculator_operations(10, 5), (15, 5, 50, 2.0))

    def test_q07_package_main(self):
        project = EXAMPLES / "calculator_project"
        result = run_python(["-m", "calculator"], project, project / "src")
        self.assertIn("Calculator Package Demo", result.stdout)
        self.assertIn("multiply(10, 5) = 50", result.stdout)

    def test_q08_src_layout_and_live_source_change(self):
        project = EXAMPLES / "calculator_project"
        for relative_path in solutions.q08_project_layout():
            self.assertTrue((project / relative_path).is_file(), relative_path)
        manifest = (project / "pyproject.toml").read_text(encoding="utf-8")
        self.assertIn('where = ["src"]', manifest)

        with tempfile.TemporaryDirectory() as directory:
            copy = Path(directory) / "calculator_project"
            shutil.copytree(project, copy)
            before = run_python(
                ["-c", "from calculator import add; print(add(10, 20))"],
                copy,
                copy / "src",
            )
            functions = copy / "src" / "calculator" / "functions.py"
            source = functions.read_text(encoding="utf-8")
            functions.write_text(
                source.replace("return a + b\n", "return a + b + 1\n", 1),
                encoding="utf-8",
            )
            after = run_python(
                ["-c", "from calculator import add; print(add(10, 20))"],
                copy,
                copy / "src",
            )
            self.assertEqual((before.stdout, after.stdout), ("30\n", "31\n"))

    def test_q09_console_script_target_and_behavior(self):
        project = EXAMPLES / "calculator_project"
        manifest = (project / "pyproject.toml").read_text(encoding="utf-8")
        self.assertIn('mycalc = "calculator.cli:main"', manifest)
        result = run_python(
            ["-m", "calculator.cli", "2", "+", "3"],
            project,
            project / "src",
        )
        self.assertEqual(result.stdout, "5\n")
        self.assertEqual(solutions.q09_cli_calculate("2", "+", "3"), 5.0)

    def test_q10_same_module_name_in_two_packages(self):
        project = EXAMPLES / "side_by_side_project"
        result = run_python(["main.py"], project)
        self.assertEqual(
            result.stdout.splitlines(), ["from package A", "from package B"]
        )
        self.assertEqual(
            solutions.q10_config_values(), ("from package A", "from package B")
        )


if __name__ == "__main__":
    unittest.main()
