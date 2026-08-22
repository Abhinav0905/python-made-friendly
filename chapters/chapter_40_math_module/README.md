# The math Module

## Check Your Understanding

1. **Why does `math.sin(90)` not return 1?** Trigonometric functions take radians. Convert degrees with `math.radians(90)` first.
2. **How do `floor` and `trunc` differ?** `floor` moves toward negative infinity while `trunc` moves toward zero. For `-2.7`, they return `-3` and `-2`.
3. **Why compare floats with `math.isclose`?** Many decimal fractions cannot be represented exactly in binary, so calculations that should agree may differ by a tiny rounding error.
4. **When should you use `atan2`?** Use it when you have separate `y` and `x` coordinates. It preserves the quadrant and handles a zero `x` value.

## Try It Yourself

1. Inspect pi, e and tau: `q01_constants()`.
2. Calculate three common angles: `q02_special_angles()`.
3. Calculate `10!` and 10 choose 3: `q03_factorial_and_combination()`.
4. Analyze square roots and logarithms safely: `q04_number_summary()`.
5. Compare `hypot` with the distance formula: `q05_distance_comparison()`.
6. Return sine, cosine and tangent: `q06_trig_summary()`.
7. Wrap `math.isclose`: `q07_almost_equal()`.
8. Find square roots with Newton's method: `q08_newton_sqrt()`.
9. Compare three cities with the haversine formula: `q09_city_distances()`.
10. Approximate pi with the Leibniz series: `q10_leibniz_pi()`.

## Manuscript correction

Exercise 5 says `sqrt(3*3 + 4*4) / 2` should also be `5.0`. Division by two makes that expression `2.5`. The solution reports both the correct distance and the half-distance so readers can see the discrepancy.

The worked city example also prints incorrect latitudes for New York and Tokyo.
The companion uses `(40.7128, -74.0060)` for New York and
`(35.6762, 139.6503)` for Tokyo.

With 1,000 terms, `q10_leibniz_pi()` returns about `3.14059265`, so only the
first two decimal places agree with pi. The error shrinks on the order of
`1 / terms`; gaining another decimal digit needs roughly ten times as many
terms. That slow rate is why the series is useful for teaching loops, not for
computing pi in real numerical work.
