"""Worked exercises for Chapter 3."""

from typing import Iterable, List, Optional


def q01_missing_indentation_error() -> str:
    """Compile the broken example and return its error description."""
    source = 'if 5 > 3:\nprint("yes")\n'
    try:
        compile(source, "exercise_1.py", "exec")
    except IndentationError as error:
        return "{}: {}".format(type(error).__name__, error.msg)
    raise AssertionError("the intentionally invalid example unexpectedly compiled")


def q01_fixed_conditional() -> Optional[str]:
    """Return what the correctly indented conditional would print."""
    if 5 > 3:
        return "yes"
    return None


def q02_describe_names(names: Iterable[str]) -> List[str]:
    """Use a loop containing a conditional to describe each name."""
    lines = []
    for name in names:
        lines.append("Processing {}...".format(name))
        if len(name) > 4:
            lines.append("  {} is a long name".format(name))
            lines.append("  It has {} characters".format(len(name)))
        else:
            lines.append("  {} is a short name".format(name))
            lines.append("  It has only {} characters".format(len(name)))
    lines.append("Done.")
    return lines


def q03_function_stub() -> None:
    """Act as the initial, deliberately empty function body."""
    pass


def q03_completed_function(name: str) -> str:
    """Return useful behavior after replacing the stub body."""
    return "Hello, {}!".format(name)


def q04_whitespace_setting(editor: str) -> str:
    """Return the chapter's whitespace-display setting for a known editor."""
    settings = {
        "vscode": '"editor.renderWhitespace": "all"',
        "pycharm": "View > Active Editor > Show Whitespace",
        "sublime": '"draw_white_space": "all"',
        "vim": ":set list",
    }
    key = editor.strip().lower().replace(" ", "")
    aliases = {"visualstudiocode": "vscode", "vs-code": "vscode"}
    key = aliases.get(key, key)
    if key not in settings:
        raise ValueError("unknown editor: {}".format(editor))
    return settings[key]


def main() -> None:
    """Print a small demonstration."""
    print(q01_missing_indentation_error())
    print(q01_fixed_conditional())
    for line in q02_describe_names(["Ada", "Guido"]):
        print(line)
    print(q03_completed_function("Ada"))
    print(q04_whitespace_setting("VS Code"))


if __name__ == "__main__":
    main()
