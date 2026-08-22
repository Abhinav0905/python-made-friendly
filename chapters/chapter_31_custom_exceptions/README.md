# Raising Custom Exceptions

## Check Your Understanding

1. **Why define a custom exception?** Give callers a distinct, catchable name for a problem in your application and attach fields they can inspect without parsing a message.
2. **Why inherit from a specific built-in?** Existing code can still catch the broader built-in. An invalid age fits `ValueError`, so `InvalidAgeError(ValueError)` works with both specific and general handlers.
3. **Why call `super().__init__()`?** It initializes the base exception's arguments and normal string representation.
4. **What does `raise ... from ...` add?** It records an explicit cause, so a traceback shows both the low-level failure and the higher-level error raised for the caller.

## Try It Yourself

1. Validate ages with `InvalidAgeError`: `q01_validate_age()`.
2. Build and handle a library exception hierarchy: `LibraryError`, `BookNotFoundError`, `q02_checkout()` and `q02_checkout_message()`.
3. Reject temperatures below absolute zero: `q03_validate_temperature()`.
4. Carry, catch and print a field and reason in `ValidationError`: `q04_validate_product()` and `q04_validation_message()`.
5. Translate `FileNotFoundError` into `ConfigMissing`: `q05_load_config()`.
6. Model account failures: `Account` and its exception hierarchy.
7. Carry die details in `DiceRollError`: `q07_validate_roll()`.
8. Validate records with specific schema errors: `q08_validate_record()`.
9. Translate `urllib` failures: `q09_fetch_url()`.
10. Collect batch failures in an exception group: `exception_groups_demo.py` (Python 3.11+).
