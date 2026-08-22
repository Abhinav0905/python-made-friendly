"""Literal Chapter 23 solutions that require Python 3.11 or newer."""

from enum import StrEnum

from .solutions import Status


def q05_describe_status_match(status):
    """Describe an order status with structural pattern matching."""
    match status:
        case Status.PENDING:
            return "Waiting for payment"
        case Status.PAID:
            return "Payment received; preparing to ship"
        case Status.SHIPPED:
            return "On the way"
        case Status.DELIVERED:
            return "Delivered"
        case _:
            raise ValueError("unknown order status")


class LogLevel(StrEnum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


def q06_log_strenum(level, message):
    """Return a log line built with a real ``StrEnum`` member."""
    if not isinstance(level, LogLevel):
        raise TypeError("level must be a LogLevel")
    return "[{}] {}".format(level, message)
