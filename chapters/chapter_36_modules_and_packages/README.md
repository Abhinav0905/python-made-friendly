# Chapter 36: Modules and Packages

## Check Your Understanding

1. **How do a module and package differ?** A module is one importable unit, commonly one `.py` file. A regular package is an importable directory that contains modules and an `__init__.py`; Python also supports namespace packages without that file.
2. **What does `__init__.py` do?** It marks a regular package, runs when that package is first imported and can define or re-export its public interface. Keep import-time work small and predictable.
3. **Why use relative imports inside a package?** A form such as `from .functions import add` states that the dependency belongs to the current package and keeps working if the package's top-level name changes.
4. **What does `__all__` do?** It controls which names a star import takes from a module or package. It also gives readers and documentation tools a clear declaration of the intended public names, though ordinary explicit imports can still request other names.

## Try It Yourself

1. Build and use `circle` and `rectangle` modules: `examples/geometry_project/src/geometry/`, `main.py`, `q01_circle_area()` and `q01_rectangle_area()`.
2. Re-export friendly area names: `examples/geometry_project/src/geometry/__init__.py` and `q02_friendly_geometry_areas()`.
3. Add a guarded circle demo: `examples/geometry_project/src/geometry/circle.py` and `q03_circle_demo()`.
4. Add `shapes_3d` without breaking top-level imports: `examples/geometry_project/src/geometry/shapes_3d/`, the top-level `__init__.py`, and the `q04_*_volume()` functions.
5. Declare the circle module's public names: `geometry/circle.py` and `q05_public_circle_names()`.
6. Re-export arithmetic from a `functions` submodule: `examples/calculator_project/src/calculator/functions.py`, `__init__.py`, and `q06_calculator_operations()`.
7. Run the calculator package with `-m`: `calculator/__main__.py` and `q07_calculator_demo()`.
8. Inspect a complete src-layout project: `examples/calculator_project/` and `q08_project_layout()`.
9. Define and exercise the `mycalc` console target: `calculator/cli.py`, `pyproject.toml`, and `q09_cli_calculate()`.
10. Import two `config.py` modules side by side: `examples/side_by_side_project/` and `q10_config_values()`.

## Editable-install recipe

No test in this repository runs `pip` or changes your Python environment. To try Exercises 8 and 9 yourself:

```bash
cd chapters/chapter_36_modules_and_packages/examples/calculator_project
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e .
python3 -m unittest discover -s tests
mycalc 2 + 3
deactivate
```

## Manuscript corrections

- Exercise 1's phrase "in each submodule create a file called area.py (but actually just a function)" mixes files and functions. The consistent layout is `circle.py` and `rectangle.py`, each defining `area()`.
- The explanation for Question 3 says importing `geometry.circle` "will not work". Importing works; it simply skips the guarded demo. Running a module that has relative imports should use `python -m package.module`.
- Question 5 prints `circumference(5)` as about `34.416`. The correct value is about `31.416`.
- Exercise 5 names a private helper `X` without defining it. The fixture uses `_diameter()` as the concrete private helper and omits it from `__all__`.
- Exercise 6 asks for a submodule named `functions`; its printed answer switches to `arithmetic.py` and adds unrelated geometry functions. The fixture keeps the requested `functions.py` interface.
- The distribution section refers to `setup.py develop`, but the command and manifest shown describe modern editable installation with `python -m pip install -e .`.
- `__all__` mechanically governs star imports. Calling it a public-API declaration for every kind of import is a useful convention, not an access restriction.

Run this chapter's tests from the repository root:

```bash
python3 -m unittest chapters.chapter_36_modules_and_packages.test_solutions
```
