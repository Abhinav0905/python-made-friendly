"""Read data stored beside this module, not beneath the current directory."""

from pathlib import Path


def get_data_path(filename="data.txt"):
    return Path(__file__).resolve().parent / filename


def read_data(filename="data.txt"):
    return get_data_path(filename).read_text(encoding="utf-8")


def main():
    print(read_data(), end="")


if __name__ == "__main__":
    main()
