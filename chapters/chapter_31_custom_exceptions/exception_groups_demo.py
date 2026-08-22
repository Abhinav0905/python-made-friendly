"""Exercise 10 for Chapter 31. Requires Python 3.11 or newer."""

from .solutions import ValidationError


def validate_all(records):
    errors = []
    for index, record in enumerate(records):
        if not record.get("name"):
            errors.append(ValidationError(f"records[{index}].name", "is required"))
        if record.get("age", 0) < 0:
            errors.append(ValidationError(f"records[{index}].age", "cannot be negative"))
    if errors:
        raise ExceptionGroup("record validation failed", errors)
    return True


def handled_fields(records):
    fields = []
    try:
        validate_all(records)
    except* ValidationError as group:
        fields.extend(error.field for error in group.exceptions)
    return fields


if __name__ == "__main__":
    print(handled_fields([{"name": "", "age": -1}]))
