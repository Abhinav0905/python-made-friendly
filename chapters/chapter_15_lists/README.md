# Lists

## Check Your Understanding

1. `append(x)` adds `x` as one new element. `extend(iterable)` adds each item yielded by the iterable as a separate element.
2. `list.sort()` changes the list in place and intentionally returns `None`. Assigning that return value replaces the variable with `None`; use `sorted(list)` when a new list is needed.
3. A shallow copy creates a new outer container but shares its nested objects. A deep copy recursively copies nested mutable objects too.
4. A list stores its current length, so `len()` reads one value in constant time. Membership may scan every element until it finds a match or reaches the end, so it is linear time.

## Try It Yourself

1. Create the first ten positive integers and index the first, lower-middle and last: `q01_first_middle_last()`.
2. Sort the supplied names without changing their original order: `q02_sorted_names()`.
3. Append, insert and remove while retaining each state: `q03_modify_list()`.
4. Validate ten positive integers and calculate four statistics: `q04_number_statistics()`.
5. Keep words longer than five characters: `q05_long_words()`.
6. Sort words longest first, breaking ties alphabetically: `q06_sort_words()`.
7. Remove duplicate values while preserving order and without a set: `q07_remove_duplicates()`.
8. Return a left-rotated copy, with negative rotation moving right: `q08_rotate()`.
9. Find the second-largest distinct number: `q09_second_largest_unique()`.
10. Demonstrate shallow-copy sharing and the `deepcopy` fix: `q10_copy_trap()`.

For ten values there is no single middle element. Exercise 1 follows the manuscript's worked answer and chooses the lower-middle value at index 4.
