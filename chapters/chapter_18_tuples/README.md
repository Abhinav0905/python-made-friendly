# Tuples

## Check Your Understanding

1. Parentheses only group `42`; the comma creates a tuple, so the one-item form is `(42,)`.
2. A tuple is hashable when every item it contains is hashable, so its hash stays stable. Lists can change and are not hashable.
3. Python evaluates the entire right side first, packs those values, then unpacks them into the names on the left.
4. Choose a named tuple when positions alone do not explain a small, fixed record and readable field names such as `person.email` help.

## Try It Yourself

1. Inspect a tuple of the first five primes: `q01_prime_tuple_details`.
2. Unpack a person's name, age and job: `q02_unpack_person`.
3. Swap two values by unpacking: `q03_swap`.
4. Calculate minimum, maximum and average without the matching built-ins: `q04_manual_stats`.
5. Align name-score rows: `q05_format_scores`.
6. Define and inspect `Person` named tuples: `Person` and `q06_name_email_pairs`.
7. Sort scores descending with alphabetical tie-breaking: `q07_rank_scores`.
8. Use extended unpacking for two leading values, middle values and the last value: `q08_extended_unpack`.
9. Find the two farthest two-dimensional points: `q09_farthest_points`.
10. Model rectangles and calculate area and perimeter: `Rectangle`, `q10_rectangle_area`, and `q10_rectangle_perimeter`.
