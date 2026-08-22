"""Solutions for the Chapter 23 exercises, compatible with Python 3.8."""

from enum import Enum, Flag, auto, unique


class Weekday(Enum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()


class Suit(Enum):
    HEARTS = auto()
    DIAMONDS = auto()
    CLUBS = auto()
    SPADES = auto()


class Status(Enum):
    PENDING = auto()
    PAID = auto()
    SHIPPED = auto()
    DELIVERED = auto()


class LogLevel(str, Enum):
    """Python 3.8-compatible string enum."""

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()


class Direction(Enum):
    NORTH = (0, -1)
    SOUTH = (0, 1)
    EAST = (1, 0)
    WEST = (-1, 0)


def q01_weekday_members():
    """Return every weekday's name and generated value."""
    return [(day.name, day.value) for day in Weekday]


def q02_is_weekend(day):
    """Return whether *day* is Saturday or Sunday."""
    return day in (Weekday.SATURDAY, Weekday.SUNDAY)


def q03_lookup_friday():
    """Return Friday looked up once by name and once by value."""
    return Weekday["FRIDAY"], Weekday(Weekday.FRIDAY.value)


def q04_is_red(suit):
    """Return whether a card suit is red."""
    return suit in (Suit.HEARTS, Suit.DIAMONDS)


def q05_describe_status(status):
    """Return a message for one order status using Python 3.8 dispatch."""
    descriptions = {
        Status.PENDING: "Waiting for payment",
        Status.PAID: "Payment received; preparing to ship",
        Status.SHIPPED: "On the way",
        Status.DELIVERED: "Delivered",
    }
    try:
        return descriptions[status]
    except KeyError:
        raise ValueError("unknown order status")


def q06_log(level, message):
    """Return a formatted log line."""
    if not isinstance(level, LogLevel):
        raise TypeError("level must be a LogLevel")
    return "[{}] {}".format(level.value, message)


def q07_set_permission(permissions, permission):
    """Return *permissions* with *permission* enabled."""
    return permissions | permission


def q07_clear_permission(permissions, permission):
    """Return *permissions* with *permission* disabled."""
    return permissions & ~permission


def q07_has_permission(permissions, permission):
    """Return whether all bits in *permission* are enabled."""
    return permissions & permission == permission


def q08_unique_and_alias_demo():
    """Return the duplicate error plus normal alias behavior."""
    duplicate_members = [("PENDING", 1), ("PAID", 2), ("SHIPPED", 2), ("DELIVERED", 3)]
    try:
        unique(Enum("UniqueStatus", duplicate_members))
    except ValueError as error:
        unique_error = str(error)
    else:
        unique_error = ""
    alias_status = Enum("AliasStatus", duplicate_members)
    is_alias = alias_status.SHIPPED is alias_status.PAID
    iterated_names = [member.name for member in alias_status]
    return unique_error, is_alias, iterated_names


def q09_direction_values():
    """Return a mapping from each direction name to its movement tuple."""
    return {direction.name: direction.value for direction in Direction}


def q09_move(x, y, direction):
    """Move an ``(x, y)`` point by a direction's stored vector."""
    dx, dy = direction.value
    return x + dx, y + dy


if __name__ == "__main__":
    print(q01_weekday_members())
    print(q05_describe_status(Status.PAID))
    print(q06_log(LogLevel.WARNING, "Disk space low"))
