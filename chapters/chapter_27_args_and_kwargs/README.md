# *args and **kwargs

## Check Your Understanding

1. A regular parameter binds one argument at a defined position or name. `*args` collects every remaining positional argument into a tuple.
2. A bare `*` marks every following parameter as keyword-only without collecting extra positional arguments.
3. `**kwargs` in a definition collects unmatched keyword arguments into a dictionary. `**mapping` in a call spreads a mapping into individual keyword arguments.
4. A forwarding wrapper collects `*args` and `**kwargs`, does any surrounding work, then calls `fn(*args, **kwargs)`. It lets wrappers and decorators work with many function signatures.

## Try It Yourself

1. Average any number of values: `q01_average`.
2. Print arbitrary attributes as `name = value`: `q02_show`.
3. Unpack a three-item sequence into a call: `q03_max_from_sequence`.
4. Build an HTML-like opening tag: `q04_tag`.
5. Require keyword-only age and email fields: `q05_make_person`.
6. Join any number of items with formatting controls: `q06_summarize`.
7. Log a forwarded call and its result: `q07_log_and_call`.
8. Forward the same arguments to several functions: `q08_call_all`.
9. Time any decorated function: `q09_timing`.
