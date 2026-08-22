# Enumerations

## Check Your Understanding

1. An enum rejects arbitrary status values and gives each valid value a readable name and a shared type.
2. `Enum` members are distinct from their stored integers. `IntEnum` members also behave as integers, which helps with older APIs but gives up that strict separation.
3. `auto()` asks the enum class to generate member values. Use it when uniqueness matters but the particular stored values do not.
4. A regular `Enum` represents one member at a time. `Flag` assigns combinable bit values, so several options such as read and write can live in one value.

## Try It Yourself

1. Define and inspect seven weekdays: `Weekday` and `q01_weekday_members`.
2. Detect weekend days: `q02_is_weekend`.
3. Look up Friday by name and value: `q03_lookup_friday`.
4. Model card suits and detect red suits: `Suit` and `q04_is_red`.
5. Describe order statuses: `Status`, `q05_describe_status`, and the literal `match` answer `modern_examples.q05_describe_status_match`.
6. Model string-compatible log levels: `LogLevel`, `q06_log`, and the literal `StrEnum` answer `modern_examples.LogLevel` with `modern_examples.q06_log_strenum`.
7. Set, clear and test file-permission flags: `Permission`, `q07_set_permission`, `q07_clear_permission`, and `q07_has_permission`.
8. Compare `@unique` rejection with normal enum aliases: `q08_unique_and_alias_demo`.
9. Store movement vectors in direction members: `Direction`, `q09_direction_values`, and `q09_move`.

The manuscript asks for `match` and `StrEnum`, introduced in Python 3.10 and 3.11. To keep this package importable on Python 3.8, `solutions.py` uses explicit enum dispatch and the established `str, Enum` mixin form. `modern_examples.py` contains the literal `match` and `StrEnum` answers for Python 3.11 and newer.
