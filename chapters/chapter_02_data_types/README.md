# Data Types

## Check Your Understanding

1. Most decimal fractions, including `0.1` and `0.2`, have no exact finite binary representation. Python stores nearby floating-point values, so their sum is `0.30000000000000004` rather than exactly `0.3`.
2. `/` performs true division and always returns a float. `//` performs floor division, returning the quotient rounded down to a whole-number boundary.
3. A string cannot be changed in place. Immutability lets code safely share strings, permits strings to be dictionary keys and gives the interpreter more room for internal optimizations.
4. `None` is a single sentinel object. `is None` checks that identity directly, while `== None` can invoke equality behavior defined by another object.

## Try It Yourself

1. Inspect the types of four literals: `q01_literal_types()`.
2. Compute a large integer: `q02_large_integer()`.
3. Compare floats exactly and by tolerance: `q03_float_comparisons()`.
4. Convert `"100"`, add 25 and return the result: `q04_convert_and_add()`.
5. Demonstrate why `bool("False")` is true: `q05_nonempty_string_is_truthy()`.

The chapter's Question 4 commentary says `int(10.5)` raises an error and that
`int()` expects a string. Python actually accepts integers, floats and suitable
strings; `int(10.5)` returns `10`. The exercise itself converts `"100"`, so
`q04_convert_and_add()` keeps that text-to-integer path and rejects malformed
integer text.
