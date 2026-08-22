# Publication notes from the code pass

These notes came from running and testing the manuscript's examples. They are a short pre-press checklist, not a general copy edit. Check each item in the final laid-out proof before changing the book.

## Confirmed Python or mathematics corrections

- **Chapter 2:** `int(10.5)` returns `10`; it does not raise an error. `int()` accepts integers, floats and suitable strings.
- **Chapter 4:** `celsius_to_fahrenheit(0)` returns `32.0`, not `35.0`.
- **Chapter 8:** `(a + b) * h / 2` is the trapezoid-area formula in the stated exercise, not a parallelogram-area formula. Also, `-40 C` equals `-40 F`, not `-31 F`.
- **Chapter 19:** `Counter.most_common()` returns a list, not a view. Wrapping a list in a tuple does not make it hashable; every item inside the tuple must also be hashable.
- **Chapter 20:** The spell-check answer's `str.translate` table deletes punctuation, although the explanation says it replaces punctuation with spaces. Deletion can join words on opposite sides of punctuation.
- **Chapter 21:** Multiplying `array.array` by `2` repeats the array; it does not raise `TypeError` and it does not multiply each element. `array.fromfile()` mutates the existing `array.array` and returns `None`; it does not return a NumPy array. Exact `sys.getsizeof()` results depend on the Python build and operating system.
- **Chapter 33:** Exercise 7 asks for a case-sensitive word count, but the printed answer lowercases the text. Exercise 8 says "above average", while the answer uses `>=` and includes scores equal to the average.
- **Chapter 34:** Combine compound suffixes with `"".join(path.suffixes)`, not `path.join()`. Exercise 10 asks for SHA-1; its heading and explanation say SHA-256 even though the code calls `hashlib.sha1()`.
- **Chapter 36:** `circumference(5)` is about `31.416`, not `34.416`. Importing a module with a guarded demo still works; the guard only prevents the demo from running on import.
- **Chapter 37:** `print __name__` is Python 2 syntax. Python 3 requires `print(__name__)`. The temperature example also mixes `32 F` and `35 F`; `32 F` equals `0 C`.
- **Chapter 40:** `math.sqrt(3*3 + 4*4) / 2` is `2.5`, so it cannot join the two `5.0` distance results in Exercise 5.
- **Chapter 40:** The city dictionary prints New York's latitude as `31.7128` and Tokyo's as `39.6762`, while the stated distances use the expected values near `40.7128` and `35.6762`. The companion code uses those corrected coordinates.

## Exercise and answer-section conflicts

- **Chapter 12:** The month-length exercise specifies a non-leap year, while the worked answer says February has "28 or 29 days". The companion code follows the exercise and returns 28.
- **Chapter 14, Exercise 7:** The exercise asks for five-character multiplication-table fields; the worked answer uses four. The companion code follows the exercise.
- **Chapter 15, Exercise 1:** Ten values have no single middle item. The companion code follows the worked answer and chooses index 4, the lower middle.
- **Chapter 25, Exercise 5:** The phrase "before the value" excludes the split value, but the concrete example includes it in the first result. The companion code follows the example.
- **Chapter 26:** Exercise 2 alternates between "square numbers" and numbers divisible by three. Exercise 3 also conflicts over `any` versus `all`. The companion code follows the repeated instruction and worked answer.
- **Chapter 29, Exercise 6:** The exercise requires `a < b`; the worked answer checks only positional order. The companion code applies both conditions.
- **Chapter 32:** The answer section contains an extra "loop over indices" answer with no matching exercise. The companion chapter has the nine exercises that are actually assigned.
- **Chapter 33, Question 5:** The explanation says the function returns a line and its length, while the displayed function returns the longest line and a blank-line count. The text also switches between `rstrip("\n")` and bare `rstrip()`.
- **Chapter 34, Exercise 2:** The requested compound-path result and the printed answer differ. The companion code follows the exercise's stated output.
- **Chapter 35, Exercise 6:** The exercise asks to alias the `datetime` module. The answer aliases the `datetime` class. The companion code aliases the module as `dt`.
- **Chapter 36:** Exercise 1 mixes an `area.py` file with an `area()` function. Exercise 6 asks for `functions.py`, while the answer switches to `arithmetic.py`. The companion fixtures use the names stated in the exercises.
- **Chapter 37:** The prime explanation mentions a user-supplied upper limit, but the program accepts no such input and prints the first ten primes. The `__name__` guard's good and bad examples are also reversed in one pitfall box.
- **Chapter 38:** The answer section discusses `self`, attributes and ad-hoc attributes instead of answering the stated Circle and `BankAccount.transfer` exercises. The companion code answers the exercise block.

## Python-version and optional-package notes

- The early text supports Python 3.8, but Chapter 12 asks for `match` (Python 3.10), Chapter 23 asks for `match` and `StrEnum` (3.10 and 3.11), and Chapters 30-31 ask for exception groups and `except*` (3.11).
- The repo keeps its main modules importable on Python 3.8. Exact newer-language answers live in clearly named supplemental files and their tests skip on older interpreters.
- Chapters 21-22 contain NumPy exercises and Chapter 35 contains a `requests` exercise. Both packages remain optional. Tests use small stand-ins and make no network requests.

## Items to verify in the print proof

Some exercise text appeared incomplete when read from the Word file. The worked answers supplied enough information to build and test the companion code, but these spots should be checked visually in the final PDF:

- Chapter 3's indentation-error snippet
- Chapter 6's greeting string
- Chapter 7's `end=""` example
- Chapter 8's missing divisor, resolved as `7` from the answer
- Chapter 10's quoted string operands
- Chapter 11's collapsed Exercise 5
- Chapter 16's capitalization in the slicing exercise
