# Common Exceptions

## Check Your Understanding

1. **How do `ValueError` and `TypeError` differ?** `ValueError` means the type is acceptable but the value is not, as in `int("hello")`. `TypeError` means the operation does not accept that kind of object, as in `"3" + 3`.
2. **Why does `except Exception` leave `KeyboardInterrupt` alone?** `KeyboardInterrupt` inherits directly from `BaseException`. A broad ordinary handler therefore still lets a person stop the program.
3. **When is `dict.get` better than catching `KeyError`?** Use it when a missing key is normal and one default value is enough. Catch `KeyError` when absence needs separate work or when several dictionary operations belong together.
4. **How do `ImportError` and `ModuleNotFoundError` differ?** `ModuleNotFoundError` is the specific case where Python cannot find the requested module. `ImportError` also covers failures to import a requested name from a module.

## Try It Yourself

1. Trigger and catch five common exceptions: `q01_common_exception_messages()`.
2. Retrieve list items with LBYL and EAFP: `q02_get_item_lbyl()` and `q02_get_item_eafp()`.
3. Keep asking until input is an integer: `q03_read_integer()`.
4. Write a file with specific error messages: `q04_write_user_file()`.
5. Catch type and zero-division failures: `q05_safe_divide()`.
6. Read JSON configuration safely: `q06_read_config()`.
7. Trigger and report `RecursionError`: `q07_recursion_report()`.
8. Read with UTF-8 and Latin-1 fallbacks: `q08_resilient_read()`.
9. Summarize readable files and errors in a directory: `q09_summarize_directory()`.

The manuscript's answer section contains an extra "loop over indices" answer that has no matching exercise. It is not numbered as a tenth exercise here.
