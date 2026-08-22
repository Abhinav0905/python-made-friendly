"""Tests for Chapter 31."""

import importlib
import socket
import sys
import tempfile
import unittest
import urllib.error
from pathlib import Path

from . import solutions


class _Response:
    def __init__(self, body):
        self.body = body

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return False

    def read(self):
        return self.body


class CustomExceptionTests(unittest.TestCase):
    def test_age_error_is_also_value_error(self):
        self.assertEqual(solutions.q01_validate_age(40), 40)
        with self.assertRaises(ValueError):
            solutions.q01_validate_age(-1)
        with self.assertRaises(solutions.InvalidAgeError):
            solutions.q01_validate_age(True)

    def test_library_hierarchy(self):
        catalog = {"123": "Python"}
        self.assertEqual(solutions.q02_checkout(catalog, "123"), "Python")
        with self.assertRaises(solutions.LibraryError):
            solutions.q02_checkout(catalog, "missing")
        self.assertEqual(
            solutions.q02_checkout_message({}, "missing"),
            "Not found. Search instead?",
        )

        class BrokenCatalog:
            def pop(self, isbn):
                raise solutions.LibraryError("catalog unavailable")

        self.assertEqual(
            solutions.q02_checkout_message(BrokenCatalog(), "123"),
            "A library error occurred.",
        )

    def test_absolute_zero(self):
        self.assertEqual(solutions.q03_validate_temperature(-273.15), -273.15)
        with self.assertRaises(solutions.TemperatureOutOfRange):
            solutions.q03_validate_temperature(-273.16)

    def test_structured_validation_error(self):
        with self.assertRaises(solutions.ValidationError) as caught:
            solutions.q04_validate_product({"name": "", "price": 5})
        self.assertEqual(caught.exception.field, "name")
        self.assertEqual(caught.exception.reason, "must be a non-empty string")
        with self.assertRaises(solutions.ValidationError) as caught:
            solutions.q04_validate_product({"name": "Book", "price": -1})
        self.assertEqual(caught.exception.field, "price")
        messages = []
        rendered = solutions.q04_validation_message(
            {"name": "", "price": 5},
            output_fn=messages.append,
        )
        self.assertEqual(rendered, "Failed on name: must be a non-empty string")
        self.assertEqual(messages, [rendered])

    def test_config_error_preserves_cause(self):
        with tempfile.TemporaryDirectory() as directory:
            present = Path(directory) / "settings.ini"
            present.write_text("debug=true", encoding="utf-8")
            self.assertEqual(solutions.q05_load_config(present), "debug=true")
            missing = Path(directory) / "missing.ini"
            with self.assertRaises(solutions.ConfigMissing) as caught:
                solutions.q05_load_config(missing)
            self.assertIsInstance(caught.exception.__cause__, FileNotFoundError)

    def test_account_errors(self):
        account = solutions.Account("A-1", balance=20)
        self.assertEqual(account.withdraw(5), 5)
        with self.assertRaises(solutions.InsufficientFunds):
            account.withdraw(100)
        frozen = solutions.Account("A-2", balance=20, frozen=True)
        with self.assertRaises(solutions.AccountFrozen):
            frozen.withdraw(1)
        with self.assertRaises(solutions.AccountNotFound):
            solutions.Account.require({}, "missing")

    def test_dice_roll_error_carries_values(self):
        self.assertEqual(solutions.q07_validate_roll(6, 4), 4)
        with self.assertRaises(solutions.DiceRollError) as caught:
            solutions.q07_validate_roll(6, 7)
        self.assertEqual((caught.exception.sides, caught.exception.value), (6, 7))
        self.assertIn("d6", str(caught.exception))

    def test_schema_error_types(self):
        with self.assertRaises(solutions.MissingField):
            solutions.q08_validate_record({"age": 10})
        with self.assertRaises(solutions.TypeMismatch):
            solutions.q08_validate_record({"name": "Ada", "age": "ten"})
        with self.assertRaises(solutions.ValueOutOfRange):
            solutions.q08_validate_record({"name": "Ada", "age": -1})
        self.assertTrue(solutions.q08_validate_record({"name": "Ada", "age": 36}))

    def test_url_wrapper_success_and_translation(self):
        self.assertEqual(
            solutions.q09_fetch_url(
                "https://example.test", opener=lambda url, timeout: _Response(b"ok")
            ),
            "ok",
        )

        def missing(url, timeout):
            raise urllib.error.HTTPError(url, 404, "missing", {}, None)

        with self.assertRaises(solutions.NotFoundError) as caught:
            solutions.q09_fetch_url("https://example.test/missing", opener=missing)
        self.assertIsInstance(caught.exception.__cause__, urllib.error.HTTPError)
        caught.exception.__cause__.close()

        def server_error(url, timeout):
            raise urllib.error.HTTPError(url, 503, "unavailable", {}, None)

        with self.assertRaises(solutions.ServerError) as caught:
            solutions.q09_fetch_url("https://example.test", opener=server_error)
        self.assertIsInstance(caught.exception.__cause__, urllib.error.HTTPError)
        caught.exception.__cause__.close()

        def timed_out(url, timeout):
            raise socket.timeout("slow")

        with self.assertRaises(solutions.RequestTimedOut) as caught:
            solutions.q09_fetch_url("https://example.test", opener=timed_out)
        self.assertIsInstance(caught.exception.__cause__, socket.timeout)

        def unreachable(url, timeout):
            raise urllib.error.URLError("offline")

        with self.assertRaises(solutions.NetworkError) as caught:
            solutions.q09_fetch_url("https://example.test", opener=unreachable)
        self.assertIsInstance(caught.exception.__cause__, urllib.error.URLError)

        def wrapped_timeout(url, timeout):
            raise urllib.error.URLError(socket.timeout("slow"))

        with self.assertRaises(solutions.RequestTimedOut) as caught:
            solutions.q09_fetch_url("https://example.test", opener=wrapped_timeout)
        self.assertIsInstance(caught.exception.__cause__, urllib.error.URLError)

    @unittest.skipIf(sys.version_info < (3, 11), "exception groups require Python 3.11")
    def test_batch_validation_group(self):
        module = importlib.import_module(
            "chapters.chapter_31_custom_exceptions.exception_groups_demo"
        )
        fields = module.handled_fields([{"name": "", "age": -1}, {"age": 3}])
        self.assertEqual(
            fields,
            ["records[0].name", "records[0].age", "records[1].name"],
        )


if __name__ == "__main__":
    unittest.main()
