"""A flat public interface backed by the functions submodule."""

from .functions import add, divide, multiply, subtract

__all__ = ["add", "subtract", "multiply", "divide"]
