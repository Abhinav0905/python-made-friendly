# Basic Input and Output

## Check Your Understanding

1. `input()` returns text because the terminal supplies characters, not Python
   values. The program must choose whether that text represents an `int`, a
   `float`, a date or something else.
2. `sep` is inserted between values passed to one `print()` call. `end` is
   appended after the final value; its default is a newline.
3. Shell redirection connects a program's standard input or output to a file or
   another process. A script can process stored or piped data without changing
   its calls to `input()` and `print()`.
4. `input()` reads one line, removes its final newline, can display a prompt and
   raises `EOFError` at end-of-file. Iterating over `sys.stdin` yields lines that
   still contain their newlines and simply ends when the stream is exhausted.

## Exercise Map

| No. | Try It Yourself | Solution |
| ---: | --- | --- |
| 1 | Read first and last names and print a greeting | `q01_build_greeting()` |
| 2 | Calculate BMI and report its category | `q02_bmi_with_category()` |
| 3 | Read three numbers from one line and average them | `q03_average_of_three()` |
| 4 | Observe a short redirected file reaching EOF | `q04_read_redirected_profile()` |

Run the interactive examples or the unit tests from the repository root:

```bash
python -m chapters.chapter_06_basic_input_and_output.solutions
python -m unittest chapters.chapter_06_basic_input_and_output.test_solutions
```

The exercise text's greeting lost characters during extraction. The solution
uses the complete greeting supplied in the chapter's Questions & Answers:
`Hello, First Last! Nice to meet you.` The BMI categories are the exact cutoffs
given there and are intended only as a programming exercise.
