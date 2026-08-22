# List Comprehensions

## Check Your Understanding

1. A trailing `if` filters items out. A leading conditional expression, `x if condition else y`, keeps one output per input and chooses its value.
2. Use a generator expression for a single pass over a large or potentially unbounded sequence, especially when a consumer such as `sum` can process values lazily.
3. Multiple `for` clauses nest from left to right. The first clause is the outer loop and each later clause is nested inside it.
4. `[print(n) for n in range(10)]` builds and discards a list of ten `None` values. A normal `for` loop states the side-effecting intent directly.

## Try It Yourself

1. Cubes from 1 through 20: `q01_cubes`.
2. Uppercase each string: `q02_uppercase`.
3. Multiples of seven from 1 through 100: `q03_divisible_by_seven`.
4. Pair each word with its length: `q04_word_lengths`.
5. Replace non-positive integers with zero: `q05_non_positive_to_zero`.
6. Build a 5 by 5 multiplication table: `q06_multiplication_table`.
7. Flatten the words from several sentences: `q07_words_from_sentences`.
8. Form cross-list pairs where `x < y`: `q08_pairs_less_than`.
9. Map words of length four or more to their lengths: `q09_long_word_lengths`.
10. Compute exclusive running sums: `q10_exclusive_running_sums`.
