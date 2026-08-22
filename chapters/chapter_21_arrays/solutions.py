"""Solutions for the Chapter 21 exercises."""

import array
import math
import random
import sys
import time


def q01_integer_array():
    """Return an ``array('i')`` holding the integers 1 through 10."""
    return array.array("i", range(1, 11))


def q02_memory_comparison(count=1_000_000):
    """Return shallow list and array container sizes for *count* integers."""
    if count < 0:
        raise ValueError("count must not be negative")
    values_list = list(range(count))
    values_array = array.array("i", range(count))
    return {
        "list_bytes": sys.getsizeof(values_list),
        "array_bytes": sys.getsizeof(values_array),
    }


def q03_write_and_read_binary(path, values):
    """Write signed integers to *path*, read them back, and return an array."""
    written = array.array("i", values)
    with open(path, "wb") as output_file:
        written.tofile(output_file)
    restored = array.array("i")
    with open(path, "rb") as input_file:
        restored.fromfile(input_file, len(written))
    return restored


def q04_running_statistics(measurements):
    """Return one statistics snapshot after each incoming measurement."""
    stored = array.array("d")
    snapshots = []
    total = 0.0
    low = high = None
    for measurement in measurements:
        value = float(measurement)
        stored.append(value)
        total += value
        low = value if low is None or value < low else low
        high = value if high is None or value > high else high
        snapshots.append(
            {
                "count": len(stored),
                "sum": total,
                "average": total / len(stored),
                "min": low,
                "max": high,
            }
        )
    return snapshots


def q05_numpy_statistics(values):
    """Return statistics from a NumPy-compatible one-dimensional array."""
    if int(values.size) == 0:
        raise ValueError("values must not be empty")
    return {
        "count": int(values.size),
        "sum": float(values.sum()),
        "average": float(values.mean()),
        "min": float(values.min()),
        "max": float(values.max()),
    }


def q05_numpy_running_statistics(values):
    """Return a NumPy-style statistics snapshot for every input prefix."""
    return [q05_numpy_statistics(values[:end]) for end in range(1, int(values.size) + 1)]


def q06_compare_statistics(numpy_values, list_values, clock=time.perf_counter):
    """Time equivalent NumPy-style and standard-list statistics."""
    if int(numpy_values.size) == 0 or not list_values:
        raise ValueError("both inputs must contain values")

    start = clock()
    numpy_stats = {
        "mean": float(numpy_values.mean()),
        "standard_deviation": float(numpy_values.std()),
        "min": float(numpy_values.min()),
        "max": float(numpy_values.max()),
    }
    numpy_seconds = clock() - start

    start = clock()
    mean = math.fsum(list_values) / len(list_values)
    variance = math.fsum((value - mean) ** 2 for value in list_values) / len(list_values)
    list_stats = {
        "mean": mean,
        "standard_deviation": variance ** 0.5,
        "min": min(list_values),
        "max": max(list_values),
    }
    list_seconds = clock() - start
    return {
        "numpy": numpy_stats,
        "list": list_stats,
        "numpy_seconds": numpy_seconds,
        "list_seconds": list_seconds,
    }


def q06_generate_and_compare(numpy_module, count=100_000, seed=0, clock=time.perf_counter):
    """Generate one reproducible data set and benchmark two representations."""
    if count <= 0:
        raise ValueError("count must be positive")
    generator = random.Random(seed)
    list_values = [generator.random() for _ in range(count)]
    numpy_values = numpy_module.array(list_values)
    return q06_compare_statistics(numpy_values, list_values, clock=clock)


if __name__ == "__main__":
    integers = q01_integer_array()
    print(len(integers), integers[0], integers[-1], sum(integers))
    print(q04_running_statistics([1.5, 2.5, 4.0]))
