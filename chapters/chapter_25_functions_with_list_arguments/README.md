# Functions with List Arguments

## Check Your Understanding

1. `lst = [1, 2, 3]` only rebinds the function's local name. It does not modify the list object still held by the caller.
2. `lst[:] = [1, 2, 3]` replaces the contents of the existing list, so every reference to that object sees the change.
3. `list.sort()` follows the in-place method convention and returns `None`; `sorted(list)` leaves its input alone and returns a new list.
4. Make a defensive copy when a function needs to reorder or edit its working data but promises not to change the caller's object, or when accepting any iterable is useful.

## Try It Yourself

1. Double list values in place: `q01_double_in_place`.
2. Return a separate doubled list: `q02_doubled`.
3. Compare the mutation and copy behaviors: `q03_compare_doubling`.
4. Remove duplicates in place without changing order: `q04_remove_duplicates_in_place`.
5. Split through the first matching value: `q05_split_at`.
6. Return minimum, maximum, sum and average: `q06_stats`.
7. Partition items with a predicate: `q07_partition`.
8. Merge two sorted lists without `sort` or `sorted`: `q08_merge_sorted`.
9. Shuffle in place with Fisher-Yates: `q09_shuffle_in_place`.

Exercise 5 says "before" the matching value, but its concrete example includes the value in the first result. This solution follows the example: `[1, 2, 3, 4, 5]` split at `3` becomes `([1, 2, 3], [4, 5])`.
