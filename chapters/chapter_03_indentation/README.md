# Indentation

## Check Your Understanding

1. Indentation already communicates block structure to readers. Python makes that visual structure part of its syntax, removing a second set of block markers that could disagree with it.
2. A block header ends with a colon and its body contains at least one statement indented more deeply. The block ends when the next statement returns to a shallower indentation level.
3. `IndentationError` covers indentation that cannot form valid block structure. `TabError`, a more specific indentation error, reports an inconsistent mix of tabs and spaces.
4. Write `pass` when syntax requires a statement but a block is intentionally empty, often while drafting a function, class or branch.
5. Blank and comment-only lines do not establish or change block structure. Their indentation is ignored for that purpose.

## Try It Yourself

1. Reproduce the missing-indentation error: `q01_missing_indentation_error()`; see the fixed behavior in `q01_fixed_conditional()`.
2. Run a loop containing an `if`, with two statements at each nested level: `q02_describe_names()`.
3. Compare a stub that uses `pass` with its completed form: `q03_function_stub()` and `q03_completed_function()`.
4. Look up the editor setting that displays whitespace: `q04_whitespace_setting()`.

Exercise 1's extracted prompt omits the code and asks why `print(yes)` "get
indented." The chapter's worked answer supplies the intended unindented
`print("yes")` example, which `q01_missing_indentation_error()` reproduces.
