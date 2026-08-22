"""Solutions for the Chapter 19 exercises."""

from collections import Counter, defaultdict


def q01_capital_lookup(capitals, country):
    """Return a country's capital or ``"not found"``."""
    return capitals.get(country, "not found")


def q02_format_items(mapping):
    """Return one ``key: value`` line per dictionary item."""
    return ["{}: {}".format(key, value) for key, value in mapping.items()]


def q03_update_and_remove(capitals, updates, country_to_remove):
    """Return an updated copy after assigning updates and removing one key."""
    result = dict(capitals)
    for country, capital in updates.items():
        result[country] = capital
    result.pop(country_to_remove, None)
    return result


def q04_word_frequencies(sentence):
    """Return lowercase word counts in descending frequency order."""
    return Counter(sentence.lower().split()).most_common()


def q05_glossary_lookup(glossary, word):
    """Return a definition or a clear unknown-word message."""
    return glossary.get(word, "Unknown word: {}".format(word))


def q06_group_with_setdefault(names):
    """Group non-empty names by first character using ``setdefault``."""
    groups = {}
    for name in names:
        if name:
            groups.setdefault(name[0], []).append(name)
    return groups


def q06_group_with_defaultdict(names):
    """Group non-empty names by first character using ``defaultdict``."""
    groups = defaultdict(list)
    for name in names:
        if name:
            groups[name[0]].append(name)
    return dict(groups)


def q07_student_averages(scores):
    """Return each student's arithmetic mean score."""
    averages = {}
    for name, marks in scores.items():
        if not marks:
            raise ValueError("each student must have at least one score")
        averages[name] = sum(marks) / len(marks)
    return averages


def q08_merge_dictionaries(first, second):
    """Return a merged dictionary in which values from *second* win."""
    return {**first, **second}


def q09_invert(mapping):
    """Swap keys and values, collecting keys that shared a value."""
    inverted = {}
    for key, value in mapping.items():
        inverted.setdefault(value, []).append(key)
    return inverted


def q10_people_by_city(people):
    """Group copies of person dictionaries under their city names."""
    cities = defaultdict(list)
    for person in people:
        if "city" not in person:
            raise ValueError("each person must include a city")
        cities[person["city"]].append(dict(person))
    return dict(cities)


if __name__ == "__main__":
    capitals = {"France": "Paris", "Japan": "Tokyo", "Brazil": "Brasilia"}
    print(q01_capital_lookup(capitals, "Japan"))
    print(q04_word_frequencies("to be or not to be"))
