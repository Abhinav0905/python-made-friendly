# Chapter 35: Importing Modules

## Check Your Understanding

1. **How do `import math` and `from math import sqrt` differ?** The first binds the module and calls the function as `math.sqrt()`, which keeps its origin visible. The second binds `sqrt` directly in the current namespace.
2. **Why avoid star imports?** They add an unknown set of names, hide each name's source and can overwrite existing names when the imported module changes.
3. **Where does Python look for `foo`?** It first checks the import cache and built-in/frozen modules, then asks import finders to search locations such as those in `sys.path`. The exact first path depends on whether Python started a script, `-m`, `-c`, or an interactive session.
4. **What does the `if __name__ == "__main__":` guard do?** It runs entry-point code only when that file is the program's entry point. Importing the file still defines its reusable names without running the guarded demo or CLI.

## Try It Yourself

1. Calculate three values through `math`: `q01_math_values()`.
2. Pick a favorite food with `from random import choice`: `q02_pick_food()`.
3. Import a neighboring greeting module: `examples/q03_greetings/greetings.py`, `main.py`, and `q03_hello()`.
4. Import and call four calculator functions: `examples/q04_calculator/calculator.py`, `main.py`, and the `q04_*` functions.
5. Run the calculator's guarded demo directly: `examples/q04_calculator/calculator.py` and `q05_calculator_demo()`.
6. Alias the `datetime` module as `dt`: `q06_current_time()`.
7. Demonstrate a requests-style fetch through an injected getter: `q07_fetch_summary()`.
8. Run the three-file project: `examples/q08_three_file_project/main.py`, `helpers.py`, `models.py`, and `q08_format_name()`.
9. Explain `sys.path`, temporarily add a directory and import from it: `q09_sys_path_report()`, `q09_import_from_directory()`, and `examples/q09_runtime_module/my_module.py`.
10. Load and inspect a named module: `q10_inspect_module()`.

## Optional `requests` recipe

`requests` is intentionally optional. The repository's tests do not install it and never contact a server. To try the exercise yourself in an isolated environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install requests
python3 - <<'PY'
import requests
from chapters.chapter_35_importing_modules.solutions import q07_fetch_summary

print(q07_fetch_summary(requests.get))
PY
deactivate
```

That final command makes the live request only when you choose to run it.

## Manuscript corrections

- Exercise 6 asks to alias the `datetime` **module**. Its printed answer aliases the `datetime` class instead. This solution uses `import datetime as dt` and `dt.datetime.now()`.
- Importing a candidate name is not a reliable test for a standard-library collision. It may find a local file or installed package, and some standard-library names are absent on a given platform. Check Python's module index and avoid well-known package names.
- `sys.path[0]` is not always a script directory. It can be an empty current-directory entry or another value under `-m`, `-c`, embedded interpreters and test runners.
- Catching every `ModuleNotFoundError` around `import_module()` can mislabel a missing dependency *inside* a module as if the requested module were absent. `q10_inspect_module()` leaves that useful traceback intact.

Run this chapter's tests from the repository root:

```bash
python3 -m unittest chapters.chapter_35_importing_modules.test_solutions
```
