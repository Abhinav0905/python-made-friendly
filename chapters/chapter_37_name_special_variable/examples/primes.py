"""Prime-number functions with a guarded demo."""

import math


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, math.isqrt(number) + 1):
        if number % divisor == 0:
            return False
    return True


def first_primes(count):
    primes = []
    candidate = 2
    while len(primes) < count:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes


def main():
    print("First 10 primes:", first_primes(10))


if __name__ == "__main__":
    main()
