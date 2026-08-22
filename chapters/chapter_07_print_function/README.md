# The Print Function

## Check Your Understanding

1. `sep` goes between values in one `print()` call. `end` comes after the last
   value and defaults to `"\n"`.
2. Use `flush=True` when output must appear at once, such as a live status line,
   prompt or progress indicator. Normal buffered output is faster.
3. F-strings put expressions beside their formatting rules, so new code is
   usually shorter and easier to read than equivalent `.format()` or `%` code.
4. `end=""` suppresses the usual newline. It lets several calls share a line and,
   with `"\r"`, lets a terminal status line overwrite itself.
5. `!r` formats a field with `repr()` instead of `str()`. Quotes, escape
   sequences and otherwise hidden whitespace then remain visible.

## Exercise Map

| No. | Try It Yourself | Solution |
| ---: | --- | --- |
| 1 | Print 1 through 10 on one comma-separated line | `q01_format_numbers_one_to_ten()` |
| 2 | Format `$1,234.56` with an f-string | `q02_format_money()` |
| 3 | Print and flush 40 timed dots | `q03_print_timed_dots()` |
| 4 | Display a self-overwriting progress bar | `q04_animate_progress_bar()` |

Run the visible demonstration or the tests from the repository root:

```bash
python -m chapters.chapter_07_print_function.solutions
python -m unittest chapters.chapter_07_print_function.test_solutions
```

The extracted exercise splits `end=""` across lines. The progress implementation
uses that argument together with a leading carriage return, matching the full
example in the chapter's Questions & Answers.
