# Sets

## Check Your Understanding

1. Dictionaries used `{}` before sets entered Python, and changing the established syntax would have broken existing code. An empty set is `set()`.
2. `remove` raises `KeyError` when the item is absent. `discard` treats absence as normal and does nothing.
3. A set uses hashes for average constant-time membership checks; a list normally scans values one by one.
4. Use `frozenset` when the collection must itself be hashable, such as a dictionary key or an element of another set, or when it must not change.

## Try It Yourself

1. Count unique values: `q01_unique_count`.
2. Find letters shared by two words: `q02_common_letters`.
3. Calculate union, intersection and both differences: `q03_set_operations`.
4. Compare the words in two sentences: `q04_compare_sentences`.
5. Remove duplicate email addresses without reordering: `q05_deduplicate_ordered`.
6. Find courses needed by every student and by at least one: `q06_course_summary`.
7. Test for all five vowels: `q07_has_all_vowels`.
8. Find misspelled words while ignoring case and punctuation: `q08_spell_check`.
9. Find values present in exactly one of three sets: `q09_exactly_one`.
10. Add, look up and iterate course entries keyed by student groups: `q10_enrollment_actions`.
