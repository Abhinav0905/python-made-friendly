"""Worked exercises for Chapter 34: os.path and pathlib."""

import hashlib
import shutil
from collections import defaultdict
from pathlib import Path


def q01_path_locations(filename="notes.txt"):
    """Return the current directory, home directory, and an absolute file path."""
    return Path.cwd(), Path.home(), Path(filename).absolute()


def q02_decompose_compound_path(path):
    """Return the five values requested for a compound-extension path."""
    path = Path(path)
    suffix_text = "".join(path.suffixes)
    base_name = path.name[: -len(suffix_text)] if suffix_text else path.name
    compound_extension = suffix_text.lstrip(".")
    return (
        path.parent,
        path.name,
        base_name,
        compound_extension,
        [str(path.parent), path.name],
    )


def q03_list_files(folder="."):
    """Return one-level regular-file names sorted lexically."""
    return sorted(entry.name for entry in Path(folder).iterdir() if entry.is_file())


def q04_python_file_sizes(folder="."):
    """Return recursive ``.py`` file paths and byte sizes in path order."""
    paths = (path for path in Path(folder).rglob("*.py") if path.is_file())
    return [(path, path.stat().st_size) for path in sorted(paths)]


def q05_safe_path(parent, name):
    """Resolve ``name`` below ``parent``, or return ``None`` if it escapes."""
    parent = Path(parent).resolve()
    target = (parent / name).resolve()
    try:
        target.relative_to(parent)
    except ValueError:
        return None
    return target


def q06_lowercase_extensions(folder):
    """Lowercase final file extensions without overwriting another file."""
    renamed = []
    for entry in sorted(Path(folder).iterdir(), key=lambda item: item.name):
        if not entry.is_file() or entry.suffix == entry.suffix.lower():
            continue
        target = entry.with_suffix(entry.suffix.lower())
        if target.exists():
            try:
                if not target.samefile(entry):
                    continue
            except OSError:
                continue
        old_name = entry.name
        entry.rename(target)
        renamed.append((old_name, target.name))
    return renamed


def q07_files_only_in(first_folder, second_folder):
    """Return file names present in the first folder but not the second."""
    first_names = {
        entry.name for entry in Path(first_folder).iterdir() if entry.is_file()
    }
    second_names = {
        entry.name for entry in Path(second_folder).iterdir() if entry.is_file()
    }
    return sorted(first_names - second_names)


def _unused_destination(target):
    if not target.exists():
        return target
    counter = 1
    while True:
        candidate = target.with_name(f"{target.stem}_{counter}{target.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def q08_organize_idempotent(folder):
    """Move root files into extension folders, numbering name collisions."""
    folder = Path(folder)
    moves = []
    for entry in sorted(folder.iterdir(), key=lambda item: item.name):
        if not entry.is_file():
            continue
        extension = entry.suffix.lstrip(".").lower() or "no_extension"
        target_directory = folder / extension
        target_directory.mkdir(exist_ok=True)
        target = _unused_destination(target_directory / entry.name)
        shutil.move(str(entry), str(target))
        moves.append((entry, target))
    return moves


def q09_find_name_collisions(root):
    """Group recursive files that have the same name at different paths."""
    groups = defaultdict(list)
    for path in sorted(Path(root).rglob("*")):
        if path.is_file():
            groups[path.name].append(path)
    return {
        name: paths
        for name, paths in sorted(groups.items())
        if len(paths) > 1
    }


def q10_sha1_file(path, chunk_size=64 * 1024):
    """Return a file's SHA-1 digest while reading bounded chunks."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    digest = hashlib.sha1()
    with open(path, "rb") as input_file:
        while True:
            chunk = input_file.read(chunk_size)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def q10_duplicate_hashes(root, chunk_size=64 * 1024):
    """Group recursive files that share a SHA-1 digest."""
    groups = defaultdict(list)
    for path in sorted(Path(root).rglob("*")):
        if not path.is_file():
            continue
        try:
            groups[q10_sha1_file(path, chunk_size)].append(path)
        except OSError:
            continue
    return {
        digest: paths
        for digest, paths in sorted(groups.items())
        if len(paths) > 1
    }


def main():
    cwd, home, notes = q01_path_locations()
    print("Current directory:", cwd)
    print("Home directory:", home)
    print("Absolute notes path:", notes)


if __name__ == "__main__":
    main()
