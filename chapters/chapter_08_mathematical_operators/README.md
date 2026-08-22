# Simple Mathematical Operators

## Check Your Understanding

1. `/` always returns a `float` so its result type does not change according to
   whether a particular pair of integers happens to divide evenly. Use `//`
   when the floor quotient is the value you need.
2. `-7 // 2` is `-4` because floor division rounds toward negative infinity.
   `int(-7 / 2)` is `-3` because `int()` truncates a float toward zero.
3. Python uses round-half-to-even. Since 2 is the even neighbor of 2.5,
   `round(2.5)` returns `2`; this rule avoids a persistent upward tie bias.
4. `pow(a, b, m)` is better when `b` is large and only the remainder is needed.
   It reduces intermediate values during exponentiation instead of first
   building the full value of `a ** b`.

## Exercise Map

| No. | Level | Try It Yourself | Solution |
| ---: | --- | --- | --- |
| 1 | Easy | Compute `100 // 7`, `100 % 7` and verify the invariant | `q01_floor_division_and_modulus()` |
| 2 | Easy | Calculate a trapezoid's area | `q02_trapezoid_area()` |
| 3 | Easy | Find the largest absolute value | `q03_maximum_absolute_value()` |
| 4 | Medium | Split seconds into hours, minutes and seconds | `q04_seconds_to_hms()` |
| 5 | Medium | Split a three-digit integer without converting it to text | `q05_three_digit_digits()` |
| 6 | Medium | Calculate and format a discount | `q06_discount_details()` |
| 7 | Hard | Convert Celsius to Fahrenheit, Kelvin and Rankine | `q07_temperature_conversions()` |
| 8 | Hard | Sum the digits of a positive integer | `q08_sum_digits()` |
| 9 | Hard | Time two forms of modular exponentiation | `q09_compare_modular_exponentiation()` |

Run the demonstrations and tests from the repository root:

```bash
python -m chapters.chapter_08_mathematical_operators.solutions
python -m unittest chapters.chapter_08_mathematical_operators.test_solutions
```

The divisor disappeared from exercise 1 during extraction; its Q&A identifies
it as 7. Two statements in that Q&A are corrected here: the area formula is for
a trapezoid, not a parallelogram, and -40 °C equals -40 °F, not -31 °F.
Timing results are reported as observations. The tests do not assume which form
wins for this small exponent because that depends on the runtime and machine.
