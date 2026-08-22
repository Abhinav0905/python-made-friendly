# Date and Time

## Check Your Understanding

1. `timedelta` does not support months or years because their lengths vary. A
   month can contain 28, 29, 30 or 31 days, while a year can contain 365 or 366.
2. A naive `datetime` has no UTC offset or time-zone information. An aware
   `datetime` has a `tzinfo` value and identifies a point on the global timeline.
3. UTC gives stored timestamps one consistent reference. Local time can be
   ambiguous or nonexistent around daylight-saving changes, and local rules can
   change. Convert UTC to a user's local zone only for display.
4. `timedelta.seconds` is the seconds left after whole days are removed, so it
   stays between 0 and 86,399. `timedelta.total_seconds()` returns the complete
   duration, including days and microseconds, as a `float`.
5. A `date` contains no clock time or UTC offset. Adding calendar days to it
   therefore cannot cross a 23-hour or 25-hour daylight-saving day.

## Exercise Map

| No. | Try It Yourself | Solution |
| ---: | --- | --- |
| 1 | Format the current date | `q01_format_current_date()` |
| 2 | Count days until the next January 1 | `q02_days_until_next_january_first()` |
| 3 | Parse and reformat `2024-07-04 09:30` | `q03_parse_and_format_datetime()` |
| 4 | Time a loop that sums 1 through 1,000,000 | `q04_sum_integers_with_timing()` |

All implementations are in `solutions.py`. Run the examples and tests from the
repository root:

```bash
python -m chapters.chapter_05_date_and_time.solutions
python -m unittest chapters.chapter_05_date_and_time.test_solutions
```

The date formatter avoids the platform-specific `%-d` and `%#d` flags. The
timing exercise uses `time.perf_counter()`, the standard-library clock intended
for measuring elapsed time.
