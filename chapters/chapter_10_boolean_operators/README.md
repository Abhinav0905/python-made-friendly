# Boolean Operators

## Check Your Understanding

1. `0 or "default"` returns `"default"`. `0` is falsy, so `or` evaluates and returns its second operand.
2. In `value or default`, a truthy `value` settles the result and Python never evaluates the default expression. An expensive fallback therefore runs only when needed.
3. Truthiness and equality are separate questions. `"hello"` is non-empty and therefore truthy, but it is a string rather than the boolean object `True`, so the equality comparison is false.
4. `&` and `|` operate on corresponding integer bits. `and` and `or` use whole-value truthiness, short-circuit and return an operand.

## Try It Yourself

1. Evaluate four boolean expressions: `q01_truth_table_checks()`.
2. Test whether an integer is strictly between 0 and 100: `q02_is_between_zero_and_100()`.
3. Evaluate a chain of falsy values ending in `"last"`: `q03_last_truthy_value()`.
4. Accept a log-on only when both stripped fields are non-empty: `q04_log_on()`.
5. Decide entry from ticket, ID and minor status: `q05_may_enter()`.
6. Apply the Gregorian leap-year rule: `q06_is_leap_year()`.
7. Evaluate the six operand-return examples: `q07_operand_results()`.
8. Select a display name with the default-value idiom: `q08_display_name()`.

Quotation marks disappeared from several string literals in Exercise 7 during
text extraction. `q07_operand_results()` follows the complete expressions in
the chapter's Questions & Answers section.
