"""Tests for Chapter 40."""

import math
import unittest

from . import solutions


class MathModuleTests(unittest.TestCase):
    def test_constants(self):
        pi, e, tau, identity = solutions.q01_constants()
        self.assertEqual((pi, e, tau), (math.pi, math.e, math.tau))
        self.assertTrue(identity)

    def test_special_angles(self):
        self.assertEqual(solutions.q02_special_angles(), (0.5, 0.5, 1.0))

    def test_factorial_and_combination(self):
        self.assertEqual(solutions.q03_factorial_and_combination(), (3628800, 120))

    def test_number_summary(self):
        positive = solutions.q04_number_summary(100)
        self.assertEqual(positive["square_root"], 10)
        self.assertEqual(positive["log_base_10"], 2)
        zero = solutions.q04_number_summary(0)
        self.assertEqual(zero["square_root"], 0)
        self.assertIsNone(zero["natural_log"])
        negative = solutions.q04_number_summary(-1)
        self.assertEqual(len(negative["messages"]), 2)
        numeric_text = solutions.q04_number_summary("100")
        self.assertEqual(numeric_text["square_root"], 10)
        not_numeric = solutions.q04_number_summary("one hundred")
        self.assertEqual(not_numeric["messages"], ["input is not a number"])
        non_finite = solutions.q04_number_summary(float("inf"))
        self.assertEqual(non_finite["messages"], ["input must be finite"])

    def test_distance_correction(self):
        hypot, formula, half, equal = solutions.q05_distance_comparison()
        self.assertEqual((hypot, formula, half), (5.0, 5.0, 2.5))
        self.assertTrue(equal)

    def test_trig_summary(self):
        sine, cosine, tangent = solutions.q06_trig_summary(45)
        self.assertAlmostEqual(sine, math.sqrt(2) / 2)
        self.assertAlmostEqual(cosine, math.sqrt(2) / 2)
        self.assertAlmostEqual(tangent, 1)

    def test_almost_equal(self):
        self.assertTrue(solutions.q07_almost_equal(0.1 + 0.2, 0.3))
        self.assertFalse(solutions.q07_almost_equal(1.0, 1.1))

    def test_newton_sqrt(self):
        self.assertAlmostEqual(solutions.q08_newton_sqrt(2), math.sqrt(2), places=12)
        self.assertEqual(solutions.q08_newton_sqrt(0), 0)
        with self.assertRaises(ValueError):
            solutions.q08_newton_sqrt(-1)
        with self.assertRaises(ValueError):
            solutions.q08_newton_sqrt(2, tolerance=0)
        with self.assertRaises(ValueError):
            solutions.q08_newton_sqrt(float("inf"))

    def test_haversine_city_pairs(self):
        distances, farthest = solutions.q09_city_distances()
        self.assertEqual(len(distances), 3)
        self.assertEqual(farthest, ("New York", "Tokyo"))
        self.assertGreater(distances[farthest], 10000)

    def test_leibniz_series(self):
        estimate = solutions.q10_leibniz_pi(1000)
        self.assertLess(abs(estimate - math.pi), 0.002)
        with self.assertRaises(ValueError):
            solutions.q10_leibniz_pi(0)


if __name__ == "__main__":
    unittest.main()
