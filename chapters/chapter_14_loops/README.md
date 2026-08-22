# Loops

## Check Your Understanding

1. Use `while` when repetition continues until a changing condition is false and the number of passes is not known beforehand. Use `for` to visit items in an iterable or run a known range.
2. `enumerate` yields each item together with its index. It reads directly as an item loop, removes manual index bookkeeping and avoids common off-by-one mistakes.
3. `break` leaves the innermost loop immediately. `continue` skips the rest of the current pass and starts the next one.
4. Removing elements shifts later positions while the iterator's position keeps advancing, so elements can be skipped. Iterate over a copy or build a new filtered list.

## Try It Yourself

1. Produce the integers 1–20 with a `for` loop: `q01_numbers_1_to_20()`.
2. Sum even integers from 2 through 100 with a loop: `q02_sum_even_numbers()`.
3. Produce powers of two below 1000 with `while`: `q03_powers_of_two()`.
4. Find values through `n` divisible by 3 or 5: `q04_multiples_of_three_or_five()`.
5. Calculate score statistics manually and with built-ins: `q05_score_statistics()`.
6. Stop on the right password or lock after three failures: `q06_password_result()`.
7. Build a 10×10 table with five-character numeric fields: `q07_multiplication_table()`.
8. Find primes through `n` with nested loops: `q08_primes_up_to()`.
9. Number a list of words with `enumerate`: `q09_numbered_words()`.
10. Play a deterministic or random ten-attempt guessing game: `q10_guessing_game()`.

The worked answer for Exercise 7 uses four-character fields, but the exercise itself asks for five. This implementation follows the exercise and tests five-character alignment.
