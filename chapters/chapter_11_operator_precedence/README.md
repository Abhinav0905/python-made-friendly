# Operator Precedence

## Check Your Understanding

1. Exponentiation binds more tightly than unary minus, so `-2 ** 2` groups as `-(2 ** 2)` and gives `-4`. Parenthesizing the base as `(-2) ** 2` gives `4`.
2. Right-associative means a run of exponent operators groups from the right: `2 ** 3 ** 2` is `2 ** (3 ** 2)`, not `(2 ** 3) ** 2`.
3. Comparisons bind more tightly than boolean `and`, so Python groups the expression as `(age >= 18) and (score > 50)`.
4. Add parentheses when the grouping is not immediately clear to a reader, when mixing less familiar operators or whenever a different grouping would change the result.

## Try It Yourself

1. Evaluate the four precedence examples: `q01_precedence_results()`.
2. Verify unary-minus and exponent precedence: `q02_negative_square()`.
3. Make the grouping in `a + b * c - d / e` explicit: `q03_grouped_expression()`.
4. Compute an average with one grouped division and a parenthesis-free rewrite: `q04_average_forms()`.
5. Evaluate four mixed comparison and boolean examples: `q05_mixed_results()`.
6. Compare the actual grouping of `x or y and z` with the alternate grouping: `q06_compare_groupings()`.
7. Evaluate the longer arithmetic expression: `q07_evaluate_expression()`.
8. Evaluate two chained comparisons: `q08_chained_comparisons()`.

Exercise 5 is collapsed into fragments in the prompt. Its worked answer names
the intended four expressions, so `q05_mixed_results()` uses those four.
