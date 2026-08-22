"""Parse web logs as a library or summarize one from the command line."""

import re
import sys
from collections import Counter


LOG_LINE = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s+\S+\s+\S+\s+'
    r'\[[^]]+\]\s+"(?P<method>[A-Z]+)\s+'
    r'(?P<path>\S+)\s+[^\"]+"\s+(?P<status>\d{3})\b'
)


def parse_line(line):
    match = LOG_LINE.search(line)
    return match.groupdict() if match else None


def summarize(path):
    ips = Counter()
    statuses = Counter()
    with open(path, "r", encoding="utf-8") as input_file:
        for line in input_file:
            parsed = parse_line(line)
            if parsed:
                ips[parsed["ip"]] += 1
                statuses[parsed["status"]] += 1
    return ips, statuses


def main(arguments=None):
    arguments = sys.argv[1:] if arguments is None else arguments
    if len(arguments) != 1:
        print("Usage: logreader.py LOG", file=sys.stderr)
        return 2
    ips, statuses = summarize(arguments[0])
    print("Requests per IP:")
    for ip, count in ips.most_common():
        print(f"  {ip}: {count}")
    print("Requests per status:")
    for status, count in statuses.most_common():
        print(f"  {status}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
