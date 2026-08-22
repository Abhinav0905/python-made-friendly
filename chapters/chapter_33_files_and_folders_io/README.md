# Chapter 33: Files and Folders I/O

## Check Your Understanding

1. **Why use `with open(...) as f`?** The context manager closes the file when the block ends, including when an exception leaves the block. A manual `close()` can be skipped by an early return or error.
2. **How do `"w"` and `"a"` differ?** Write mode creates a file or truncates one that exists. Append mode creates a missing file but writes at the end of an existing file.
3. **Why is file iteration cheaper than `readlines()`?** Iteration supplies one buffered line at a time. `readlines()` builds a list containing every line, so its memory use grows with the whole file.
4. **What happens with the wrong encoding?** Decoding may raise `UnicodeDecodeError`, or it may succeed while producing the wrong characters. Use the encoding that wrote the bytes, normally stated explicitly as UTF-8 for new text files.

## Try It Yourself

1. Create, read and print `hello.txt`: `q01_create_read_print()`.
2. Format a user-named file with line numbers: `q02_numbered_lines()`.
3. Append the current date and time to `log.txt`: `q03_append_timestamp()`.
4. Copy a file with each line's characters reversed: `q04_reverse_lines()`.
5. Find the longest line and count blank lines: `q05_analyze_file()`.
6. Merge two files with alternating lines: `q06_merge_alternating()`.
7. Find the ten most common case-sensitive words: `q07_word_frequencies()`.
8. Read score CSV, calculate the average and add the classification column: `q08_process_scores()`.
9. Walk a directory and total bytes by extension: `q09_size_by_extension()`.
10. Follow appended log lines: `q10_tail_lines()`. Leave `stop_after_idle_polls=None` for normal `tail -f` behavior; the finite option exists for tests and short demonstrations.

## Manuscript corrections

- Exercise 7 says the count is case-sensitive. The printed answer calls `lower()` and is case-insensitive. This solution keeps `Python` and `python` separate.
- Exercise 8 says "above average", so a score equal to the average is marked `no`. The printed answer uses `>=`, which means "at or above average". It also uses `split(",")`, while the solution uses `csv` so quoted names such as `"Doe, Ada"` work.
- Question 5 alternates between `rstrip("\n")` and a description of `rstrip()` with no argument. This solution treats an empty or whitespace-only line as blank, while keeping a nonblank line's other spaces when comparing lengths.
- The explanation after Question 5 says the function returns a line and its length. The shown function and this solution return the longest line and the blank-line count.
- Several displayed newline literals were lost during typesetting. The working code uses explicit `"\n"` strings.

Run this chapter's tests from the repository root:

```bash
python3 -m unittest chapters.chapter_33_files_and_folders_io.test_solutions
```
