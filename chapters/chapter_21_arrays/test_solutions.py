"""Tests for Chapter 21."""

import math
import tempfile
import unittest
from pathlib import Path

from chapters.chapter_21_arrays import solutions


class FakeNumericArray:
    """Small NumPy-like object used without a third-party dependency."""

    def __init__(self, values):
        self.values = list(values)
        self.size = len(self.values)

    def sum(self):
        return sum(self.values)

    def mean(self):
        return sum(self.values) / len(self.values)

    def min(self):
        return min(self.values)

    def max(self):
        return max(self.values)

    def std(self):
        mean = self.mean()
        return math.sqrt(sum((value - mean) ** 2 for value in self.values) / len(self.values))

    def __getitem__(self, key):
        selected = self.values[key]
        if isinstance(key, slice):
            return FakeNumericArray(selected)
        return selected


class FakeNumpy:
    @staticmethod
    def array(values):
        return FakeNumericArray(values)


class ArrayTests(unittest.TestCase):
    def test_integer_array(self):
        values = solutions.q01_integer_array()
        self.assertEqual(values.typecode, "i")
        self.assertEqual(list(values), list(range(1, 11)))
        self.assertEqual((len(values), values[0], values[-1], sum(values)), (10, 1, 10, 55))

    def test_memory_comparison(self):
        sizes = solutions.q02_memory_comparison(10_000)
        self.assertLess(sizes["array_bytes"], sizes["list_bytes"])
        with self.assertRaises(ValueError):
            solutions.q02_memory_comparison(-1)

    def test_binary_round_trip(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "integers.bin"
            restored = solutions.q03_write_and_read_binary(path, [10, -20, 30])
            self.assertEqual(restored.typecode, "i")
            self.assertEqual(list(restored), [10, -20, 30])

    def test_running_statistics(self):
        snapshots = solutions.q04_running_statistics([2, 4, -3])
        self.assertEqual(snapshots[0], {"count": 1, "sum": 2.0, "average": 2.0, "min": 2.0, "max": 2.0})
        self.assertEqual(snapshots[-1]["count"], 3)
        self.assertAlmostEqual(snapshots[-1]["average"], 1.0)
        self.assertEqual((snapshots[-1]["min"], snapshots[-1]["max"]), (-3.0, 4.0))

    def test_numpy_protocol_statistics(self):
        values = FakeNumericArray([1.0, 2.0, 3.0, 4.0])
        self.assertEqual(
            solutions.q05_numpy_statistics(values),
            {"count": 4, "sum": 10.0, "average": 2.5, "min": 1.0, "max": 4.0},
        )
        with self.assertRaises(ValueError):
            solutions.q05_numpy_statistics(FakeNumericArray([]))
        self.assertEqual(
            solutions.q05_numpy_running_statistics(FakeNumericArray([2.0, 4.0, -3.0])),
            [
                {"count": 1, "sum": 2.0, "average": 2.0, "min": 2.0, "max": 2.0},
                {"count": 2, "sum": 6.0, "average": 3.0, "min": 2.0, "max": 4.0},
                {"count": 3, "sum": 3.0, "average": 1.0, "min": -3.0, "max": 4.0},
            ],
        )

    def test_statistics_comparison(self):
        times = iter([10.0, 10.25, 20.0, 20.75])
        result = solutions.q06_compare_statistics(
            FakeNumericArray([1.0, 2.0, 3.0]), [1.0, 2.0, 3.0], clock=lambda: next(times)
        )
        self.assertEqual(result["numpy_seconds"], 0.25)
        self.assertEqual(result["list_seconds"], 0.75)
        self.assertEqual(result["numpy"], result["list"])
        times = iter([30.0, 30.1, 40.0, 40.2])
        generated = solutions.q06_generate_and_compare(
            FakeNumpy, count=10, seed=7, clock=lambda: next(times)
        )
        self.assertAlmostEqual(generated["numpy_seconds"], 0.1)
        self.assertAlmostEqual(generated["list_seconds"], 0.2)
        self.assertEqual(generated["numpy"], generated["list"])
        with self.assertRaises(ValueError):
            solutions.q06_generate_and_compare(FakeNumpy, count=0)


if __name__ == "__main__":
    unittest.main()
