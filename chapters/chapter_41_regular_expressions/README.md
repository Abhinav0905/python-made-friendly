# Regular Expressions

## Check Your Understanding

1. **How do `re.search` and `re.match` differ?** `search` scans for a match anywhere. `match` only tries at the start; use `fullmatch` when the entire string must fit.
2. **What does `?` mean?** After an item it means zero or one. After `*` or `+` it changes a greedy quantifier into a lazy one.
3. **Why can `findall` return tuples?** Capturing groups ask it to return the captured pieces. With several groups, each match becomes a tuple of those pieces.
4. **When should you use a parser?** Use the format's parser for nested or escaped formats such as HTML, JSON and XML. Regex is a good fit for small, regular text patterns.

## Try It Yourself

1. Find every run of digits: `q01_find_numbers()`.
2. Find capitalized words: `q02_capitalized_words()`.
3. Collapse runs of whitespace: `q03_collapse_whitespace()`.
4. Validate a `555-1234` phone number: `q04_is_valid_phone()`.
5. Extract an email domain: `q05_extract_domain()`.
6. Find standalone four-digit numbers: `q06_four_digit_numbers()`.
7. Replace every digit with `X`: `q07_redact_digits()`.
8. Capture ISO date parts with named groups: `q08_date_parts()`.
9. Count Apache-style logs by IP and status: `q09_summarize_logs()`.
10. Tokenize a basic arithmetic expression: `q10_tokenize()`.
