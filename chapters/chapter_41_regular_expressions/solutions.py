"""Worked exercises for Chapter 41: Regular Expressions."""

import re
from collections import Counter


def q01_find_numbers(text):
    """Exercise 1: return every run of one or more digits."""
    return re.findall(r"\d+", text)


def q02_capitalized_words(text):
    """Exercise 2: return words that start with one capital letter."""
    return re.findall(r"\b[A-Z][a-z]*\b", text)


def q03_collapse_whitespace(text):
    """Exercise 3: replace each whitespace run with one space."""
    return re.sub(r"\s+", " ", text)


def q04_is_valid_phone(text):
    """Exercise 4: validate exactly three digits, a hyphen, then four digits."""
    return re.fullmatch(r"\d{3}-\d{4}", text) is not None


def q05_extract_domain(email):
    """Exercise 5: return the domain of a simply shaped email or None."""
    match = re.fullmatch(r"[^@\s]+@(?P<domain>[^@\s]+)", email)
    return match.group("domain") if match else None


def q06_four_digit_numbers(text):
    """Exercise 6: return standalone four-digit numbers."""
    return re.findall(r"\b\d{4}\b", text)


def q07_redact_digits(text):
    """Exercise 7: replace every digit with X."""
    return re.sub(r"\d", "X", text)


_DATE_PATTERN = re.compile(
    r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
)


def q08_date_parts(text):
    """Exercise 8: return named date parts when the whole shape matches."""
    match = _DATE_PATTERN.fullmatch(text)
    return match.groupdict() if match else None


_LOG_PATTERN = re.compile(
    r"(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) "
    r'.*?"[A-Z]+\s+\S+\s+HTTP/\d(?:\.\d)?"\s+'
    r"(?P<status>\d{3})\b"
)


def q09_summarize_logs(lines):
    """Exercise 9: count matched log lines by IP and status code."""
    addresses = Counter()
    statuses = Counter()
    for line in lines:
        match = _LOG_PATTERN.search(line)
        if match:
            addresses[match.group("ip")] += 1
            statuses[match.group("status")] += 1
    return dict(addresses), dict(statuses)


_TOKEN_PATTERN = re.compile(r"\d+|[+\-*/()]")


def q10_tokenize(expression):
    """Exercise 10: tokenize integers, operators, and parentheses."""
    tokens = []
    position = 0
    for match in _TOKEN_PATTERN.finditer(expression):
        gap = expression[position:match.start()]
        if gap.strip():
            raise ValueError(f"unexpected text: {gap!r}")
        tokens.append(match.group())
        position = match.end()
    if expression[position:].strip():
        raise ValueError(f"unexpected text: {expression[position:]!r}")
    return tokens


def main():
    sample = "Alice and Bob went to Chicago in 2024."
    print("Numbers:", q01_find_numbers(sample))
    print("Capitalized words:", q02_capitalized_words(sample))
    print("Tokens:", q10_tokenize("3 + 4*(2-1)"))


if __name__ == "__main__":
    main()
