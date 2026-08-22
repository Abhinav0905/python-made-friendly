"""Check that every book chapter has the required companion files."""

from pathlib import Path
import sys


EXPECTED_CHAPTERS = (
    "chapter_01_getting_started",
    "chapter_02_data_types",
    "chapter_03_indentation",
    "chapter_04_comments_and_documentation",
    "chapter_05_date_and_time",
    "chapter_06_basic_input_and_output",
    "chapter_07_print_function",
    "chapter_08_mathematical_operators",
    "chapter_09_bitwise_operators",
    "chapter_10_boolean_operators",
    "chapter_11_operator_precedence",
    "chapter_12_conditionals",
    "chapter_13_comparisons",
    "chapter_14_loops",
    "chapter_15_lists",
    "chapter_16_list_slicing",
    "chapter_17_list_comprehensions",
    "chapter_18_tuples",
    "chapter_19_dictionaries",
    "chapter_20_sets",
    "chapter_21_arrays",
    "chapter_22_multidimensional_arrays",
    "chapter_23_enumerations",
    "chapter_24_functions",
    "chapter_25_functions_with_list_arguments",
    "chapter_26_functional_programming",
    "chapter_27_args_and_kwargs",
    "chapter_28_iterables_and_iterators",
    "chapter_29_loops_within_functions",
    "chapter_30_exceptions",
    "chapter_31_custom_exceptions",
    "chapter_32_common_exceptions",
    "chapter_33_files_and_folders_io",
    "chapter_34_os_path_and_pathlib",
    "chapter_35_importing_modules",
    "chapter_36_modules_and_packages",
    "chapter_37_name_special_variable",
    "chapter_38_classes_and_objects",
    "chapter_39_metaclasses",
    "chapter_40_math_module",
    "chapter_41_regular_expressions",
)

REQUIRED_FILES = ("__init__.py", "README.md", "solutions.py", "test_solutions.py")


def check_repository(root):
    """Return a list of structural problems below *root*."""
    problems = []
    chapters_root = root / "chapters"
    actual = {path.name for path in chapters_root.glob("chapter_*") if path.is_dir()}
    expected = set(EXPECTED_CHAPTERS)

    for name in sorted(expected - actual):
        problems.append(f"missing chapter folder: {name}")
    for name in sorted(actual - expected):
        problems.append(f"unexpected chapter folder: {name}")

    for name in EXPECTED_CHAPTERS:
        folder = chapters_root / name
        if not folder.is_dir():
            continue
        for filename in REQUIRED_FILES:
            if not (folder / filename).is_file():
                problems.append(f"{name}: missing {filename}")

        readme = folder / "README.md"
        if readme.is_file():
            text = readme.read_text(encoding="utf-8")
            if "Check Your Understanding" not in text:
                problems.append(f"{name}: README has no conceptual-answer section")
            if "Try It Yourself" not in text and "Exercise Map" not in text:
                problems.append(f"{name}: README has no exercise map")

        for filename in ("__init__.py", "solutions.py", "test_solutions.py"):
            path = folder / filename
            if path.is_file():
                try:
                    compile(path.read_text(encoding="utf-8"), str(path), "exec")
                except SyntaxError as error:
                    problems.append(f"{name}/{filename}:{error.lineno}: {error.msg}")
    return problems


def main():
    root = Path(__file__).resolve().parents[1]
    problems = check_repository(root)
    if problems:
        for problem in problems:
            print(f"ERROR: {problem}")
        return 1
    print(f"OK: {len(EXPECTED_CHAPTERS)} chapter folders passed structural checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
