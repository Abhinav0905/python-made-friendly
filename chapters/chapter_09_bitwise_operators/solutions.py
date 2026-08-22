"""Worked exercises for Chapter 9."""

from typing import Callable, Dict, List, Tuple


CLICK = 1 << 0
KEYPRESS = 1 << 1
SCROLL = 1 << 2
RESIZE = 1 << 3


def q01_binary_breakdown() -> Tuple[Dict[int, str], Tuple[int, ...]]:
    """Return binary strings and the powers of two that make up 100."""
    values = {10: bin(10), 20: bin(20), 100: bin(100)}
    powers_in_100 = (2 ** 6, 2 ** 5, 2 ** 2)
    return values, powers_in_100


def q02_bitwise_results() -> Tuple[int, int, int]:
    """Return AND, OR and XOR for 0b1100 and 0b1010."""
    left = 0b1100
    right = 0b1010
    return left & right, left | right, left ^ right


def q03_power_of_two(exponent: int = 10) -> int:
    """Return two raised to a non-negative integer exponent using a shift."""
    if not isinstance(exponent, int):
        raise TypeError("exponent must be an integer")
    if exponent < 0:
        raise ValueError("exponent must not be negative")
    return 1 << exponent


def q04_is_even(number: int) -> bool:
    """Return whether the integer's lowest bit is zero."""
    return (number & 1) == 0


def q05_count_bits(number: int) -> int:
    """Count the 1-bits in a non-negative integer with a loop."""
    if number < 0:
        raise ValueError("number must not be negative")
    count = 0
    while number:
        count += number & 1
        number >>= 1
    return count


def q06_xor_swap(first: int, second: int) -> Tuple[int, int]:
    """Swap two integer values through XOR operations."""
    first ^= second
    second ^= first
    first ^= second
    return first, second


def q07_handle(
    events: int,
    output: Callable[[str], None] = print,
) -> List[str]:
    """Print and return a message for every recognized event bit."""
    messages = []
    if events & CLICK:
        messages.append("Click detected")
        output("Click detected")
    if events & KEYPRESS:
        messages.append("Keypress detected")
        output("Keypress detected")
    if events & SCROLL:
        messages.append("Scroll detected")
        output("Scroll detected")
    if events & RESIZE:
        messages.append("Resize detected")
        output("Resize detected")
    if events == 0:
        messages.append("No events")
        output("No events")
    return messages


def _validate_bit_index(index: int) -> None:
    if not isinstance(index, int):
        raise TypeError("bit index must be an integer")
    if index < 0:
        raise ValueError("bit index must not be negative")


def q08_set_bit(number: int, index: int) -> int:
    """Return *number* with the indexed bit set."""
    _validate_bit_index(index)
    return number | (1 << index)


def q08_clear_bit(number: int, index: int) -> int:
    """Return *number* with the indexed bit cleared."""
    _validate_bit_index(index)
    return number & ~(1 << index)


def main() -> None:
    """Print a small demonstration."""
    print(q01_binary_breakdown())
    print(q02_bitwise_results())
    print(q03_power_of_two())
    print(q04_is_even(12), q05_count_bits(13), q06_xor_swap(5, 9))
    q07_handle(CLICK | SCROLL)
    print(q08_set_bit(0b1010, 0), q08_clear_bit(0b1010, 1))


if __name__ == "__main__":
    main()
