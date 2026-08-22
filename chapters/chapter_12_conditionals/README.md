# Conditionals

## Check Your Understanding

1. An `if`/`elif` chain runs only the first matching branch. Broad conditions placed too early can consume values meant for more specific branches.
2. Use a conditional expression for one short choice that produces a value. Use an `if` statement when branches take actions or when nesting would hurt readability.
3. A simple `match` can replace repeated equality checks, but its patterns can also destructure values, bind names and use guards. An `elif` chain can test unrelated conditions.
4. The colon tells Python that an indented suite follows the condition or fallback header.

## Try It Yourself

1. Classify a number by sign with `if`/`elif`/`else`: `q01_number_sign()`.
2. Classify a leap year with ordered branches: `q02_is_leap_year()`.
3. Classify a number by sign with a conditional expression: `q03_number_sign_expression()`.
4. Validate and classify three triangle sides: `q04_triangle_type()`.
5. Calculate and categorize BMI: `q05_bmi_category()`.
6. Return a non-leap-year month's day count: `q06_days_in_month()`.
7. Judge two rock-paper-scissors choices: `q07_rock_paper_scissors()`.
8. Return four independent integer labels: `q08_integer_labels()`.
9. Calculate tax across the three marginal brackets: `q09_income_tax()`.

Exercise 6 asks for `match`, which requires Python 3.10. The main
`q06_days_in_month()` function expresses the same cases with Python
3.8-compatible `if` statements. The exact `match` solution is in
`modern_examples.py` and runs on Python 3.10 or newer. The exercise specifies a
non-leap year, so both functions return 28 for February; the worked answer's
"28 or 29 days" conflicts with that requirement.
