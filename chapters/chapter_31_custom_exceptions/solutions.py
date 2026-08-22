"""Worked exercises for Chapter 31: Raising Custom Exceptions."""

import json
import socket
import urllib.error
import urllib.request


class InvalidAgeError(ValueError):
    """An age has the right general type but an invalid value."""


def q01_validate_age(age):
    """Exercise 1: validate an integer age from 0 through 150."""
    if isinstance(age, bool) or not isinstance(age, int):
        raise InvalidAgeError("age must be an integer")
    if not 0 <= age <= 150:
        raise InvalidAgeError(f"age out of range: {age}")
    return age


class LibraryError(Exception):
    """Base class for library operations."""


class BookNotFoundError(LibraryError):
    """A requested book is not in the catalog."""


def q02_checkout(catalog, isbn):
    """Exercise 2: remove and return a book, or raise a specific error."""
    try:
        return catalog.pop(isbn)
    except KeyError as error:
        raise BookNotFoundError(f"no book with ISBN {isbn}") from error


def q02_checkout_message(catalog, isbn):
    """Exercise 2: handle the specific error before its library base class."""
    try:
        book = q02_checkout(catalog, isbn)
    except BookNotFoundError:
        return "Not found. Search instead?"
    except LibraryError:
        return "A library error occurred."
    return f"Checked out: {book}"


class TemperatureOutOfRange(ValueError):
    """A temperature is below the physical lower bound."""


def q03_validate_temperature(celsius):
    """Exercise 3: allow absolute zero but reject values below it."""
    if celsius < -273.15:
        raise TemperatureOutOfRange(f"{celsius} C is below absolute zero")
    return celsius


class ValidationError(Exception):
    """A field failed a named validation rule."""

    def __init__(self, field, reason):
        super().__init__(f"{field}: {reason}")
        self.field = field
        self.reason = reason


def q04_validate_product(product):
    """Exercise 4: raise a structured validation error for product data."""
    name = product.get("name")
    if not isinstance(name, str) or not name.strip():
        raise ValidationError("name", "must be a non-empty string")
    price = product.get("price")
    if not isinstance(price, (int, float)) or price < 0:
        raise ValidationError("price", "must be a non-negative number")
    return product


def q04_validation_message(product, output_fn=print):
    """Exercise 4: catch a structured error and print its field and reason."""
    try:
        q04_validate_product(product)
    except ValidationError as error:
        message = f"Failed on {error.field}: {error.reason}"
        output_fn(message)
        return message
    return None


class ConfigMissing(Exception):
    """A required configuration file cannot be found."""


def q05_load_config(path):
    """Exercise 5: translate a missing-file error while keeping its cause."""
    try:
        with open(path, encoding="utf-8") as config_file:
            return config_file.read()
    except FileNotFoundError as error:
        raise ConfigMissing(f"config not found: {path}") from error


class AccountError(Exception):
    """Base class for account failures."""


class InsufficientFunds(AccountError):
    def __init__(self, balance, amount):
        super().__init__(f"balance {balance:.2f} cannot cover {amount:.2f}")
        self.balance = balance
        self.amount = amount


class AccountFrozen(AccountError):
    """An account is present but cannot make transactions."""


class AccountNotFound(AccountError):
    """An account identifier is absent from a collection."""


class Account:
    """Exercise 6: an account whose methods raise domain errors."""

    def __init__(self, account_id, balance=0, frozen=False):
        self.account_id = account_id
        self.balance = balance
        self.frozen = frozen

    @classmethod
    def require(cls, accounts, account_id):
        try:
            return accounts[account_id]
        except KeyError as error:
            raise AccountNotFound(f"account not found: {account_id}") from error

    def withdraw(self, amount):
        if self.frozen:
            raise AccountFrozen(f"account is frozen: {self.account_id}")
        if amount > self.balance:
            raise InsufficientFunds(self.balance, amount)
        self.balance -= amount
        return amount


class DiceRollError(ValueError):
    def __init__(self, sides, value):
        super().__init__(f"invalid roll for d{sides}: {value!r}")
        self.sides = sides
        self.value = value


def q07_validate_roll(sides, value):
    """Exercise 7: validate a supplied result for a die."""
    if not isinstance(sides, int) or sides < 1:
        raise DiceRollError(sides, value)
    if not isinstance(value, int) or not 1 <= value <= sides:
        raise DiceRollError(sides, value)
    return value


class SchemaError(Exception):
    """Base class for record-schema errors."""


class MissingField(SchemaError):
    def __init__(self, field):
        super().__init__(f"missing required field: {field}")
        self.field = field


class TypeMismatch(SchemaError):
    def __init__(self, field, expected, actual):
        super().__init__(
            f"{field}: expected {expected.__name__}, got {type(actual).__name__}"
        )
        self.field = field
        self.expected = expected
        self.actual = actual


class ValueOutOfRange(SchemaError):
    def __init__(self, field, value, minimum=None, maximum=None):
        super().__init__(f"{field}: {value!r} is outside the allowed range")
        self.field = field
        self.value = value
        self.minimum = minimum
        self.maximum = maximum


DEFAULT_SCHEMA = {
    "name": {"required": True, "type": str},
    "age": {"required": True, "type": int, "minimum": 0, "maximum": 150},
}


def q08_validate_record(record, schema=DEFAULT_SCHEMA):
    """Exercise 8: raise the most specific error for a bad record."""
    if not isinstance(record, dict):
        raise TypeMismatch("record", dict, record)
    for field, rules in schema.items():
        if rules.get("required") and field not in record:
            raise MissingField(field)
        if field not in record:
            continue
        value = record[field]
        expected = rules.get("type")
        if expected is not None and not isinstance(value, expected):
            raise TypeMismatch(field, expected, value)
        minimum = rules.get("minimum")
        maximum = rules.get("maximum")
        if minimum is not None and value < minimum:
            raise ValueOutOfRange(field, value, minimum, maximum)
        if maximum is not None and value > maximum:
            raise ValueOutOfRange(field, value, minimum, maximum)
    return True


class NetworkError(Exception):
    """Base class for translated network failures."""


class NotFoundError(NetworkError):
    """The server returned HTTP 404."""


class ServerError(NetworkError):
    """The server returned a 5xx status."""


class RequestTimedOut(NetworkError):
    """The request did not finish before its deadline."""


def q09_fetch_url(url, timeout=10, opener=None):
    """Exercise 9: translate urllib failures into application errors."""
    if opener is None:
        opener = urllib.request.urlopen
    try:
        with opener(url, timeout=timeout) as response:
            return response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        if error.code == 404:
            raise NotFoundError(f"not found: {url}") from error
        if error.code >= 500:
            raise ServerError(f"server returned HTTP {error.code}") from error
        raise NetworkError(f"server returned HTTP {error.code}") from error
    except (socket.timeout, TimeoutError) as error:
        raise RequestTimedOut(f"request timed out: {url}") from error
    except urllib.error.URLError as error:
        if isinstance(error.reason, (socket.timeout, TimeoutError)):
            raise RequestTimedOut(f"request timed out: {url}") from error
        raise NetworkError(f"cannot reach {url}") from error


def main():
    print("Valid age:", q01_validate_age(42))
    print("Absolute zero:", q03_validate_temperature(-273.15))
    print("Valid record:", q08_validate_record({"name": "Ada", "age": 36}))
    print("JSON exporter check:", json.dumps({"status": "ok"}))


if __name__ == "__main__":
    main()
