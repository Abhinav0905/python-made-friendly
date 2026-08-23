# Python, Made Friendly: companion code

This repository contains the worked exercises for all 41 chapters of *Python, Made Friendly*: 345 programming exercises and 170 conceptual checks. It is arranged in the same order as the book, so a reader can move straight from an exercise to its answer.

Each chapter folder contains:

- `README.md`: answers to "Check Your Understanding" and a map of the programming exercises
- `solutions.py`: runnable, numbered solutions
- `test_solutions.py`: automated checks for the chapter code

The solutions favor clear beginner code. Functions accept arguments and return values where that makes an answer easy to test. Exercises about console input, files, modules or packages also include a small runnable demonstration.

## Requirements

- Python 3.8 or newer
- No mandatory third-party packages

A few exercises demonstrate features added after Python 3.8. Those files state the required version and their tests skip cleanly on older interpreters.

The NumPy exercises in Chapters 21-22 accept NumPy-compatible objects without making NumPy a project dependency. Chapter 35 includes an optional `requests` recipe. The automated tests install neither package and never contact the network.

## Run the examples

Open a chapter folder and read its README first. You can then run its solution module from the repository root:

```bash
python -m chapters.chapter_01_getting_started.solutions
```

On macOS or Linux, use `python3` if `python` does not point to Python 3.

## Run the tests

Run every chapter test with the standard library's `unittest` runner:

```bash
python -m unittest discover -s chapters -t . -p "test_*.py"
```

Run one chapter on its own:

```bash
python -m unittest chapters.chapter_01_getting_started.test_solutions
```

Check that all 41 chapter folders and required files are present:

```bash
python tools/check_repository.py
```

## Chapter index

### Part I: Python Basics

1. [Getting Started with Python](chapters/chapter_01_getting_started)
2. [Data Types](chapters/chapter_02_data_types)
3. [Indentation](chapters/chapter_03_indentation)
4. [Comments and Documentation](chapters/chapter_04_comments_and_documentation)
5. [Date and Time](chapters/chapter_05_date_and_time)
6. [Basic Input and Output](chapters/chapter_06_basic_input_and_output)
7. [The Print Function](chapters/chapter_07_print_function)

### Part II: Operators and Control Flow

8. [Simple Mathematical Operators](chapters/chapter_08_mathematical_operators)
9. [Bitwise Operators](chapters/chapter_09_bitwise_operators)
10. [Boolean Operators](chapters/chapter_10_boolean_operators)
11. [Operator Precedence](chapters/chapter_11_operator_precedence)
12. [Conditionals](chapters/chapter_12_conditionals)
13. [Comparisons](chapters/chapter_13_comparisons)
14. [Loops](chapters/chapter_14_loops)

### Part III: Collections

15. [Lists](chapters/chapter_15_lists)
16. [List Slicing](chapters/chapter_16_list_slicing)
17. [List Comprehensions](chapters/chapter_17_list_comprehensions)
18. [Tuples](chapters/chapter_18_tuples)
19. [Dictionaries](chapters/chapter_19_dictionaries)
20. [Sets](chapters/chapter_20_sets)
21. [Arrays](chapters/chapter_21_arrays)
22. [Multidimensional Arrays](chapters/chapter_22_multidimensional_arrays)
23. [Enumerations](chapters/chapter_23_enumerations)

### Part IV: Functions

24. [Functions](chapters/chapter_24_functions)
25. [Functions with List Arguments](chapters/chapter_25_functions_with_list_arguments)
26. [Functional Programming in Python](chapters/chapter_26_functional_programming)
27. [`*args` and `**kwargs`](chapters/chapter_27_args_and_kwargs)
28. [Iterables and Iterators](chapters/chapter_28_iterables_and_iterators)
29. [Loops within Functions](chapters/chapter_29_loops_within_functions)

### Part V: Exceptions

30. [Exceptions](chapters/chapter_30_exceptions)
31. [Raising Custom Exceptions](chapters/chapter_31_custom_exceptions)
32. [Common Exceptions](chapters/chapter_32_common_exceptions)

### Part VI: Files, Modules and Packages

33. [Files and Folders I/O](chapters/chapter_33_files_and_folders_io)
34. [`os.path` and `pathlib`](chapters/chapter_34_os_path_and_pathlib)
35. [Importing Modules](chapters/chapter_35_importing_modules)
36. [Modules and Packages](chapters/chapter_36_modules_and_packages)
37. [The `__name__` Special Variable](chapters/chapter_37_name_special_variable)

### Part VII: Object-Oriented Python

38. [Classes and Objects](chapters/chapter_38_classes_and_objects)
39. [Metaclasses](chapters/chapter_39_metaclasses)

### Part VIII: Standard Library Tools

40. [The `math` Module](chapters/chapter_40_math_module)
41. [Regular Expressions](chapters/chapter_41_regular_expressions)

## About the manuscript

The Word manuscript is intentionally ignored by Git. This keeps the repository small and prevents the unpublished book file from being distributed with the companion code.

The code pass found a small set of factual errors, exercise-answer conflicts and version requirements that should be checked before printing. See [Publication notes](PUBLICATION_NOTES.md).

## License

This companion repository is released under the [MIT License](LICENSE).
