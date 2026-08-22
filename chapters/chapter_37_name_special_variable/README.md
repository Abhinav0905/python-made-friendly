# Chapter 37: The __name__ Special Variable

## Check Your Understanding

1. **What value does `__name__` have?** A directly executed entry point gets `"__main__"`. An imported module gets its import name, such as `tools.parser`, not always just its filename stem.
2. **Why put entry-point work in `main()`?** Tests and other code can import and call `main()` with controlled inputs. The guard stays a tiny switch instead of hiding untestable logic.
3. **If `a.py` imports `b.py` and you run `a.py`, what is `b.__name__`?** It is `"b"`. Only the entry-point module receives `"__main__"`.
4. **What is `__file__` for?** It identifies where a module was loaded from. Resolve its parent to find data shipped beside the module, independent of the process's current directory.

## Try It Yourself

1. Create a module that prints its name: `examples/mymod.py` and `q01_mymod_path()`.
2. Compare direct execution with import: `q02_observe_name_modes()`.
3. Build an importable prime checker with a guarded demo: `examples/primes.py`, `q03_is_prime()` and `q03_first_primes()`.
4. Delegate the primes guard to `main()`: `examples/primes.py` and `q04_primes_main()`.
5. Build a dual-purpose calculator: `examples/calculator.py`, `q05_calculate_expression()` and the `q05_*` operations.
6. Build a dual-purpose temperature converter: `examples/tempconvert.py`, `q06_convert()` and both `q06_*` conversion functions.
7. Build a statistics module and file CLI: `examples/stats.py` and the `q07_*` functions.
8. Parse and summarize logs without import side effects: `examples/logreader.py`, `test_logreader.py`, `q08_parse_line()` and `q08_summarize_log()`.
9. Find data beside a module from any working directory: `examples/data_reader.py`, `data.txt`, `q09_data_path()` and `q09_read_adjacent_data()`.
10. Convert an earlier palindrome module to library-plus-script form: `examples/palindrome.py`, `q10_is_palindrome()` and `q10_find_palindromes()`.

## Manuscript corrections

- Exercise 1 uses the Python 2 statement `print __name__`. In Python 3 it must be `print(__name__)`; the example fixture uses the function form.
- An imported submodule's name may be qualified, such as `geometry.circle`. It is not always only the filename without `.py`.
- The "missing quotes" pitfall displays its good and bad examples backwards. The valid guard compares with the string literal: `if __name__ == "__main__":`.
- `__package__` is usually an empty string for an imported top-level module and can be `None` for a directly run file. It is not uniformly empty.
- The printed temperature example for `32 F` labels its input as `35 F`. The correct result is `32.0 F = 0.0 C`.
- The prime-answer explanation says it prints primes "up to the given input", but the program has no such input. It prints the first ten primes.
- File-reading examples omitted `encoding="utf-8"`. The working examples state the encoding.

Run this chapter's tests from the repository root:

```bash
python3 -m unittest chapters.chapter_37_name_special_variable.test_solutions
```
