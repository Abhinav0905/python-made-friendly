# Functional Programming in Python

## Check Your Understanding

1. `map` is a good fit when a named function already expresses the transformation, when several iterables feed one function or when its lazy iterator is useful. A comprehension is usually clearer than `map` with a lambda.
2. `filter(None, iterable)` drops every falsy item, not just `None`; that includes valid data such as `0`, `False`, empty strings and empty containers.
3. `sum` names the operation directly, handles an empty iterable and is easier to read than a general reduction with an addition lambda.
4. A pure function's result depends only on its arguments and it causes no observable side effects. That makes calls predictable, easy to test and safe to compose.

## Try It Yourself

1. Square 1 through 10 with `map` and a comprehension: `q01_square_versions`.
2. Keep numbers from 1 through 50 divisible by three: `q02_divisible_by_three_versions`.
3. Check for a word longer than ten letters and whether all words have at least three: `q03_word_checks`.
4. Convert strings, filter evens and sum the result: `q04_even_integer_sum`.
5. Find the longest string with `reduce`: `q05_longest_with_reduce`.
6. Build and filter scores through both `dict(zip(...))` and a dictionary comprehension: `q06_score_pipeline`.
7. Compose two one-argument functions: `q07_compose`.
8. Purely deduplicate, threshold-filter and sum integers: `q08_process_numbers`.
9. Count words through a flattened iterator: `q09_word_frequencies`.
10. Apply chained discounts and create category-specific functions: `q10_apply_discounts`, `q10_student_discount`, and `q10_vip_discount`.

Exercise 2 calls the output "square numbers" once, while the surrounding instruction and worked answer say numbers divisible by three. The implementation follows the repeated divisible-by-three requirement. Exercise 3's second "any" conflicts with its worked answer; this repo uses `all` for the at-least-three check, matching that answer.
