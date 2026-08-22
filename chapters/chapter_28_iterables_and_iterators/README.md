# Iterables and Iterators

## Check Your Understanding

1. An iterable can produce an iterator, normally through `__iter__`. An iterator tracks one traversal, returns itself from `__iter__` and produces values through `__next__` until `StopIteration`.
2. Each loop over a list asks it for a fresh iterator. A generator is already a one-pass iterator and remains exhausted after its values have been consumed.
3. `return` ends a function. `yield` emits one value, suspends the function with its local state intact and resumes it on the next request.
4. Use a generator expression when values are needed once, may be numerous or unbounded, or can feed a lazy consumer without storing a full list.

## Try It Yourself

1. Step through `"hello"` with `iter` and `next`: `q01_step_characters`.
2. Sum squares from 1 through 10 with a generator expression: `q02_sum_of_squares`.
3. Chain a list, tuple and string: `q03_chain_iterator`.
4. Yield even values through an inclusive limit: `q04_evens_up_to`.
5. Generate Fibonacci numbers forever: `q05_fibonacci`.
6. Yield cumulative sums: `q06_running_sum`.
7. Lazily read only log lines containing `ERROR`: `q07_error_lines`.
8. Produce the first 100 positive multiples of seven: `q08_first_hundred_multiples_of_seven`.
9. Yield fixed-size groups with a final partial group: `q09_group`.
10. Yield fixed-size sliding windows with `deque`: `q10_window`.
