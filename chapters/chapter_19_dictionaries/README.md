# Dictionaries

## Check Your Understanding

1. A dictionary is a mapping indexed by keys, so direct iteration and `in` use the same fast key lookup. Use `value in d.values()` when values are the intended search target.
2. `d[key]` returns the value or raises `KeyError`. `d.get(key)` returns the value or `None`, and it can accept another default.
3. `defaultdict(factory)` creates a missing value on first access, removing the repeated check-and-initialize code from grouping loops.
4. Lists can change, so they are unhashable. A dictionary key needs a stable hash for as long as it remains in the dictionary.

## Try It Yourself

1. Look up a chosen country's capital: `q01_capital_lookup`.
2. Format each dictionary pair as `key: value`: `q02_format_items`.
3. Update capitals and remove one country: `q03_update_and_remove`.
4. Count words in descending frequency order: `q04_word_frequencies`.
5. Look up a word in a glossary: `q05_glossary_lookup`.
6. Group names with both `setdefault` and `defaultdict`: `q06_group_with_setdefault` and `q06_group_with_defaultdict`.
7. Map students to average scores: `q07_student_averages`.
8. Merge dictionaries with the second one winning: `q08_merge_dictionaries`.
9. Invert a dictionary and group duplicate values: `q09_invert`.
10. Group person records by city: `q10_people_by_city`.
