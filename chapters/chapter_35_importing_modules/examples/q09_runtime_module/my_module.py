"""A module loaded after its directory is added to sys.path."""

ANSWER = 42


def public_answer():
    return ANSWER
