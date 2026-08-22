"""Worked exercises for Chapter 33: Files and Folders I/O."""

import csv
import os
import re
import time
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


def q01_create_read_print(path="hello.txt", output_fn=print):
    """Create ``hello.txt``, read it back, print it, and return its text."""
    path = Path(path)
    path.write_text("Hello, world\n", encoding="utf-8")
    content = path.read_text(encoding="utf-8")
    output_fn(content, end="")
    return content


def q02_numbered_lines(path):
    """Return a file's lines prefixed with right-aligned line numbers."""
    numbered = []
    with open(path, "r", encoding="utf-8") as input_file:
        for number, line in enumerate(input_file, start=1):
            numbered.append(f"{number:>4}: {line.rstrip(chr(10) + chr(13))}")
    return numbered


def q03_append_timestamp(path="log.txt", when=None):
    """Append one timestamped execution record and return the record."""
    if when is None:
        when = datetime.now()
    timestamp = when.isoformat(sep=" ", timespec="seconds")
    record = f"[{timestamp}] executed\n"
    with open(path, "a", encoding="utf-8") as output_file:
        output_file.write(record)
    return record


def q04_reverse_lines(source, destination):
    """Reverse each line's characters while preserving its line ending."""
    with open(source, "r", encoding="utf-8", newline="") as input_file, open(
        destination, "w", encoding="utf-8", newline=""
    ) as output_file:
        for line in input_file:
            if line.endswith("\r\n"):
                body, ending = line[:-2], "\r\n"
            elif line.endswith(("\n", "\r")):
                body, ending = line[:-1], line[-1]
            else:
                body, ending = line, ""
            output_file.write(body[::-1] + ending)


def q05_analyze_file(path):
    """Return the first longest nonblank line and the blank-line count."""
    longest = ""
    blank_count = 0
    with open(path, "r", encoding="utf-8") as input_file:
        for line in input_file:
            body = line.rstrip("\r\n")
            if not body.strip():
                blank_count += 1
            elif len(body) > len(longest):
                longest = body
    return longest, blank_count


def q06_merge_alternating(first_path, second_path, output_path):
    """Merge two files by alternating lines, then drain the longer file."""
    with open(first_path, "r", encoding="utf-8") as first_file, open(
        second_path, "r", encoding="utf-8"
    ) as second_file, open(output_path, "w", encoding="utf-8") as output_file:
        while True:
            first_line = first_file.readline()
            second_line = second_file.readline()
            if not first_line and not second_line:
                break
            if first_line:
                output_file.write(first_line)
            if second_line:
                output_file.write(second_line)


_WORD = re.compile(r"\b\w+\b", re.UNICODE)


def q07_word_frequencies(path, limit=10):
    """Return the most common case-sensitive words in first-seen tie order."""
    counts = Counter()
    with open(path, "r", encoding="utf-8") as input_file:
        for line in input_file:
            counts.update(_WORD.findall(line))
    return counts.most_common(limit)


def q08_process_scores(input_path, output_path):
    """Write ``name,score,yes/no`` rows and return the class average.

    ``yes`` means strictly above the arithmetic mean, as the exercise says.
    The :mod:`csv` module keeps quoted names and embedded commas valid.
    """
    records = []
    with open(input_path, "r", encoding="utf-8", newline="") as input_file:
        for row_number, row in enumerate(csv.reader(input_file), start=1):
            if not row or all(not value.strip() for value in row):
                continue
            if len(row) != 2:
                raise ValueError(f"row {row_number} must contain name and score")
            name, score_text = (value.strip() for value in row)
            records.append((name, score_text, float(score_text)))

    average = sum(score for _, _, score in records) / len(records) if records else 0.0
    with open(output_path, "w", encoding="utf-8", newline="") as output_file:
        writer = csv.writer(output_file, lineterminator="\n")
        for name, score_text, score in records:
            writer.writerow([name, score_text, "yes" if score > average else "no"])
    return average


def q09_size_by_extension(root_dir):
    """Return total file bytes by lowercase extension using ``os.walk``."""
    totals = defaultdict(int)
    for dirpath, _dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            try:
                size = os.path.getsize(path)
            except OSError:
                continue
            extension = os.path.splitext(filename)[1].lower() or "(no extension)"
            totals[extension] += size
    return dict(sorted(totals.items()))


def q10_tail_lines(
    path,
    poll_interval=0.1,
    sleep_fn=time.sleep,
    stop_after_idle_polls=None,
):
    """Yield lines appended after opening ``path``.

    Normal ``tail -f`` use leaves ``stop_after_idle_polls`` as ``None``. Tests
    and finite callers can set it to stop without a signal.
    """
    idle_polls = 0
    with open(path, "r", encoding="utf-8") as input_file:
        input_file.seek(0, os.SEEK_END)
        while True:
            line = input_file.readline()
            if line:
                idle_polls = 0
                yield line
                continue
            idle_polls += 1
            if (
                stop_after_idle_polls is not None
                and idle_polls >= stop_after_idle_polls
            ):
                return
            sleep_fn(poll_interval)


def main():
    print("Import this module and call a qNN_* function for each exercise.")


if __name__ == "__main__":
    main()
