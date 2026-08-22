"""Palindrome utilities with a guarded command-line mode."""

import sys


def is_palindrome(text):
    cleaned = "".join(character.lower() for character in text if character.isalnum())
    return cleaned == cleaned[::-1]


def find_palindromes(words):
    return [word for word in words if is_palindrome(word)]


def main(arguments=None):
    arguments = sys.argv[1:] if arguments is None else arguments
    if not arguments:
        print("Usage: palindrome.py TEXT [TEXT ...]", file=sys.stderr)
        return 2
    for text in arguments:
        print(f"{'yes' if is_palindrome(text) else 'no'}: {text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
