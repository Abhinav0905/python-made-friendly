# List Slicing

## Check Your Understanding

1. Exclusive stops make a slice's length `stop - start`, let adjacent slices meet without overlap and match the convention used by `range`.
2. `lst[::-1]` creates a reversed shallow copy. Omitted bounds cover the sequence and the `-1` step walks from its end toward its beginning.
3. An extended slice with a step other than one requires the replacement iterable to have exactly as many elements as the selected positions. A plain slice can grow or shrink.
4. One index must identify exactly one element, so a missing position is an error. A slice describes a bounded region and can sensibly return the portion that exists, including an empty result.

## Try It Yourself

1. Produce four requested views of `[10, 20, 30, 40, 50]`: `q01_slice_views()`.
2. Extract `gram`, `prog` and `gni` from `programming`: `q02_string_segments()`.
3. Reverse a list with slicing: `q03_reverse_list()`.
4. Join the first `n` and last `n` elements: `q04_first_n_last_n()`.
5. Remove odd-indexed elements with one deletion: `q05_remove_every_other()`.
6. Divide a list into consecutive chunks: `q06_chunk()`.
7. Interleave equal-length lists with slice assignment: `q07_interleave()`.
8. Check string or list palindromes with slicing: `q08_is_palindrome()`.
9. Reverse word order in a string: `q09_reverse_words()`.

Exercise 2 capitalizes `Programming` while requesting lowercase results.
`q02_string_segments()` defaults to lowercase `programming`, matching the three
requested strings. Exercise 4's direct `lst[:n] + lst[-n:]` form breaks at
`n == 0` because `-0` is `0`; the solution returns an empty list for that case.
