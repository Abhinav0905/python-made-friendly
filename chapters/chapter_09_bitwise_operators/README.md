# Bitwise Operators

## Check Your Understanding

1. `&` combines the individual bits of integer operands. `and` tests truthiness, short-circuits and returns one of its original operands.
2. Python behaves as if negative integers have infinitely many leading `1` bits. Flipping every bit of `5` therefore produces the two's-complement value `-6`; in general, `~x == -x - 1`.
3. XOR removes itself: `(value ^ key) ^ key == value`. That property is useful in checksums, reversible graphics operations and low-level algorithms. A single-key XOR is not secure encryption.
4. A bit-flag integer stores independent on/off settings in separate power-of-two bits. Code combines flags with OR, checks them with AND and clears them with AND-NOT. File permissions and many operating-system APIs use this pattern.

## Try It Yourself

1. Inspect the binary form and set-bit powers of 10, 20 and 100: `q01_binary_breakdown()`.
2. Apply AND, OR and XOR to the two binary literals: `q02_bitwise_results()`.
3. Compute a power of two with left shift: `q03_power_of_two()`.
4. Test parity from the last bit: `q04_is_even()`.
5. Count set bits with a loop: `q05_count_bits()`.
6. Swap two integers with XOR: `q06_xor_swap()`.
7. Handle four combined event flags: `q07_handle()`.
8. Set or clear an indexed bit: `q08_set_bit()` and `q08_clear_bit()`.

`q05_count_bits()` rejects negative inputs. Without that check, Python's sign-preserving right shift would keep a negative value negative forever and the requested loop would not terminate.
