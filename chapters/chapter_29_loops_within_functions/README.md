# Loops within Functions

## Check Your Understanding

1. An early return says that a successful search is finished at the exact point it succeeds. It avoids a separate flag, `break` and post-loop check.
2. Use a generator when results are consumed once, are large or unbounded, or should flow lazily through a pipeline. Return a list when callers need indexing, length or repeated passes.
3. A nested helper stays private to the operation that needs it and can read values from the enclosing scope without extra parameters.
4. Use a comprehension for a short transform or filter with no side effects. Keep a loop for branching, state changes, side effects or early exits.

## Try It Yourself

1. Return the first negative value early: `q01_first_negative`.
2. Detect duplicates without a set: `q02_contains_duplicates`.
3. Count vowels with `sum` and a generator expression: `q03_count_vowels`.
4. Find the first index of the maximum value: `q04_index_of_max`.
5. Find every index of a target: `q05_find_all`.
6. Yield increasing-value pairs that sum to a target: `q06_pairs_summing_to`.
7. Group consecutive equal values: `q07_group_consecutive`.
8. Recursively flatten nested lists: `q08_flatten`.
9. Return the longest contiguous strictly increasing run: `q09_longest_increasing_run`.
10. Yield deque-based moving averages: `q10_moving_average`.

Exercise 6 explicitly requires `a < b`. The worked answer checks only that `a` occurs earlier than `b`; this implementation also applies the stated value comparison.
