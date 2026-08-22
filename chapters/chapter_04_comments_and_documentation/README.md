# Comments and Documentation

## Check Your Understanding

1. A comment is source-only text for someone reading nearby code. A docstring is the first string in a module, class or function body and remains attached to that object at runtime for tools such as `help()`.
2. Comments usually explain a local choice or constraint. Docstrings describe an object's public purpose, inputs, output and errors for people who use it.
3. A docstring must be the first statement in the module, class or function body. A string placed later is only an ordinary string expression.
4. A `#` inside a quoted string is an ordinary character. It starts a comment only outside a string.
5. Commented-out code should normally be removed. Version control retains its history, while a dead copy in the active file can become stale and distract readers.

## Try It Yourself

1. Convert Celsius to Fahrenheit with a multi-line docstring: `q01_celsius_to_fahrenheit()`.
2. Inspect that function through `help()`: `q02_help_for_temperature_function()`.
3. Read an unfamiliar standard-library docstring and try its behavior: `q03_combinations_docstring()` and `q03_combinations()`.
4. Collect comments from a source file for a why-versus-what audit: `q04_collect_comments()`.

The manuscript's worked example says `celsius_to_fahrenheit(0)` returns `35.0`. The formula printed directly below it returns `32.0`, the correct freezing point, so this companion code uses `32.0`.
