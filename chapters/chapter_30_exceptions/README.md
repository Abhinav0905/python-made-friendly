# Exceptions

## Check Your Understanding

1. **How do `except ValueError` and `except Exception` differ?** The first catches one expected failure. The second catches most ordinary program errors and can hide defects, so use it only at a boundary where you can report, clean up or retry an unknown failure.
2. **Why keep a `try` block small?** A small block makes it clear which operation is expected to fail and stops the handler from catching an unrelated bug.
3. **What does `else` do?** It runs only when the `try` block succeeds. It is useful for success work that should not sit inside the protected block.
4. **What if both `try` and `finally` return?** The `finally` return wins and discards the earlier value. Avoid returning from `finally`.
5. **Why use `raise ... from ...`?** It translates a low-level error into one that fits the caller while preserving the original error as `__cause__`.

## Try It Yourself

1. Keep asking until an integer is entered: `q01_read_integer()`.
2. Create `data.txt` if it is missing: `q02_ensure_data_file()`.
3. Demonstrate `try`, `except`, `else` and `finally`: `q03_four_clause_demo()`.
4. Divide safely with exception handling: `q04_safe_divide()`.
5. Parse an integer, then a float: `q05_robust_parse()`.
6. Sum valid integer lines and skip the rest: `q06_sum_valid_integers()`.
7. Find the first present dictionary key with EAFP: `q07_first_value()`.
8. Retry a failing callable: `q08_retry()`.
9. Time a block with a context manager: `q09_timer()`.
10. Raise and split an exception group: `exception_groups_demo.py` (Python 3.11+).
