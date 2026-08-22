"""Tests for Chapter 38."""

import unittest

from .solutions import BankAccount, Circle, q02_independent_circles, q03_pi_values


class ClassesAndObjectsTests(unittest.TestCase):
    def test_circle_area_and_growth(self):
        circle = Circle(3)
        self.assertAlmostEqual(circle.area(), 3.14159 * 9)
        self.assertEqual(circle.grow(), 6)

    def test_circles_are_independent(self):
        self.assertEqual(q02_independent_circles(2, 5), (4, 5))

    def test_pi_is_available_on_class_and_instance(self):
        self.assertEqual(q03_pi_values(), (3.14159, 3.14159))

    def test_transfer_changes_both_accounts(self):
        source = BankAccount("Source", 100)
        target = BankAccount("Target", 10)
        self.assertTrue(source.transfer(35, target))
        self.assertEqual((source.balance, target.balance), (65, 45))

    def test_failed_transfer_changes_neither_account(self):
        source = BankAccount("Source", 5)
        target = BankAccount("Target", 10)
        self.assertFalse(source.transfer(6, target))
        self.assertEqual((source.balance, target.balance), (5, 10))


if __name__ == "__main__":
    unittest.main()
