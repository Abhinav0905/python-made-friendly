# Comparisons

## Check Your Understanding

1. `==` asks whether values compare equal. `is` asks whether two names refer to the exact same object; its usual use is checking a singleton such as `None`.
2. Strings compare by Unicode code point. Uppercase `B` has a lower code point than lowercase `a`, so `"Banana"` sorts before `"apple"`.
3. `1 < 2 < 3` means `(1 < 2) and (2 < 3)`, with the shared middle expression evaluated once.
4. Membership in a dictionary tests keys. To test its values, use the dictionary's `values()` view.

## Try It Yourself

1. Evaluate four cross-type equalities: `q01_equality_results()`.
2. Test an inclusive range with one comparison chain: `q02_between_1_and_100()`.
3. Test weekday abbreviation membership: `q03_is_weekday()`.
4. Count values in the inclusive range 50–100: `q04_count_in_range()`.
5. Compare two strings without case distinctions: `q05_case_insensitive_equal()`.
6. Check a phrase for palindrome form after cleaning it: `q06_is_phrase_palindrome()`.
7. Evaluate four chained comparisons: `q07_chained_results()`.
8. Search registered users without case distinctions: `q08_is_registered()`.
9. Find the vowels present in a sentence, alphabetically: `q09_vowels_present()`.
