"""Three statistics plus a guarded one-number-per-line CLI."""

import math
import sys


def mean(data):
    return sum(data) / len(data)


def median(data):
    ordered = sorted(data)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def stdev(data):
    if len(data) < 2:
        raise ValueError("need at least two values")
    average = mean(data)
    return math.sqrt(sum((value - average) ** 2 for value in data) / (len(data) - 1))


def main(arguments=None):
    arguments = sys.argv[1:] if arguments is None else arguments
    if len(arguments) != 1:
        print("Usage: stats.py FILE", file=sys.stderr)
        return 2
    try:
        with open(arguments[0], "r", encoding="utf-8") as input_file:
            values = [float(line) for line in input_file if line.strip()]
        average, middle, deviation = mean(values), median(values), stdev(values)
    except (OSError, ValueError, ZeroDivisionError) as error:
        print(error, file=sys.stderr)
        return 2
    print(f"Mean: {average:.4f}")
    print(f"Median: {middle:.4f}")
    print(f"Stdev: {deviation:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
