# Functions

## Check Your Understanding

1. A parameter is a name in a function definition. An argument is the value supplied for that parameter in a call.
2. Default expressions run once when the function is defined, so `x=[]` shares one list across calls. Use `None` and create a fresh list inside the function.
3. A function that reaches the end without `return`, or executes bare `return`, returns `None`.
4. After a keyword binds a named parameter, a following positional argument would make binding ambiguous. Python rejects that call as a syntax error.

## Try It Yourself

1. Calculate rectangle area: `q01_area_of_rectangle`.
2. Test whether an integer is even: `q02_is_even`.
3. Build a greeting with a default: `q03_greet`.
4. Count whitespace-separated words: `q04_word_count`.
5. Find the largest of three values without `max`: `q05_max_of_three`.
6. Divide safely when the denominator may be zero: `q06_safe_divide`.
7. Reproduce and fix the mutable-default bug: `q07_buggy_add_student` and `q07_add_student`.
8. Return the first `n` Fibonacci numbers with documented input rules: `q08_fibonacci`.
9. Test positive primality with type hints: `q09_is_prime`.
10. Apply a function repeatedly: `q10_apply_n_times`.
