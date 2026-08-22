"""Solutions for the Chapter 20 exercises."""

import string


def q01_unique_count(values):
    """Return the number of distinct values."""
    return len(set(values))


def q02_common_letters(first, second):
    """Return distinct letters found in both strings."""
    return set(first) & set(second)


def q03_set_operations(first, second):
    """Return the main two-set operation results."""
    return {
        "union": first | second,
        "intersection": first & second,
        "first_only": first - second,
        "second_only": second - first,
    }


def q04_compare_sentences(first, second):
    """Return shared words and the words unique to either sentence."""
    first_words = set(first.lower().split())
    second_words = set(second.lower().split())
    return first_words & second_words, first_words - second_words, second_words - first_words


def q05_deduplicate_ordered(items):
    """Return distinct hashable items in first-seen order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def q06_course_summary(students):
    """Return courses common to all students and courses needed by any."""
    course_sets = list(students.values())
    if not course_sets:
        return set(), set()
    common = set.intersection(*course_sets)
    needed = set.union(*course_sets)
    return common, needed


def q07_has_all_vowels(text):
    """Return whether *text* contains a, e, i, o, and u, ignoring case."""
    return set("aeiou").issubset(set(text.lower()))


def q08_spell_check(dictionary, text):
    """Return lowercase words absent from *dictionary*, ignoring punctuation."""
    translation = str.maketrans({character: " " for character in string.punctuation})
    words = text.lower().translate(translation).split()
    known_words = {word.lower() for word in dictionary}
    return {word for word in words if word not in known_words}


def q09_exactly_one(first, second, third):
    """Return elements present in exactly one of three sets."""
    return (first - second - third) | (second - first - third) | (third - first - second)


def q10_enrollment_actions(enrollments, new_group, new_course, lookup_group):
    """Add an entry to a copy, perform a lookup, and return sorted rows."""
    result = dict(enrollments)
    result[frozenset(new_group)] = new_course
    course = result[frozenset(lookup_group)]
    rows = [(tuple(sorted(group)), value) for group, value in result.items()]
    rows.sort(key=lambda row: row[0])
    return result, course, rows


if __name__ == "__main__":
    values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(q01_unique_count(values))
    print(q02_common_letters("programming", "language"))
