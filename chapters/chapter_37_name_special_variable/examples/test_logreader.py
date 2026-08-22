"""A separate import-mode smoke test for logreader.py."""

from logreader import parse_line


LINE = (
    '192.168.1.42 - - [19/Apr/2026:14:30:45 +0000] '
    '"GET /home HTTP/1.1" 200 1234'
)
parsed = parse_line(LINE)
assert parsed["ip"] == "192.168.1.42"
assert parsed["method"] == "GET"
assert parsed["status"] == "200"
print("parse_line: OK")
