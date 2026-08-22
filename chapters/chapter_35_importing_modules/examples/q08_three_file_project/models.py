"""Data models for the three-file example."""


class User:
    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email

    def __repr__(self):
        return f"User({self.first!r}, {self.last!r})"
