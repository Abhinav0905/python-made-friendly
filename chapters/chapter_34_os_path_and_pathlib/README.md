# Chapter 34: os.path and pathlib

## Check Your Understanding

1. **Why is `Path("data") / "reports"` better than string concatenation?** `Path` inserts the platform's separator, retains path structure and gives the result path methods. A hard-coded slash is an operating-system assumption hidden in a string.
2. **How do `suffix` and `suffixes` differ?** `Path("file.tar.gz").suffix` is `".gz"`; `.suffixes` is `[".tar", ".gz"]`.
3. **How do you safely create a directory that may exist?** Call `path.mkdir(parents=True, exist_ok=True)`. It creates missing parents and accepts an existing target directory.
4. **When does `os.path` still make sense?** Use it while maintaining string-based older code or working with an API that explicitly needs strings. Prefer `pathlib` for new application code.

## Try It Yourself

1. Report CWD, home and an absolute `notes.txt` path: `q01_path_locations()`.
2. Produce the requested compound-path fields: `q02_decompose_compound_path()`.
3. List one directory's files by name: `q03_list_files()`.
4. Recursively list Python files and byte sizes: `q04_python_file_sizes()`.
5. Reject paths that escape a parent, including escapes through symlinks: `q05_safe_path()`.
6. Lowercase mixed-case file extensions: `q06_lowercase_extensions()`.
7. Compare two folders by file name: `q07_files_only_in()`.
8. Organize files safely on repeated runs and number collisions: `q08_organize_idempotent()`.
9. Group equal file names found at different paths: `q09_find_name_collisions()`.
10. Hash large files in chunks and group equal SHA-1 values: `q10_sha1_file()` and `q10_duplicate_hashes()`.

## Manuscript corrections

- Exercise 2 explicitly asks for `file`, `tar.gz` and `["/a/b/c", "file.tar.gz"]`. The printed answer instead reports the ordinary `stem`, final `suffix`, full `suffixes` and `Path.parts`. `q02_decompose_compound_path()` follows the requested output.
- To combine all suffixes, use `"".join(path.suffixes)`, not `path.join()` as stated in the text.
- Exercise 10 asks for SHA-1. Its answer heading says SHA-256 and the explanation mentions SHA-256, but the shown code actually calls `hashlib.sha1()`. This companion answer follows the exercise and names SHA-1 plainly. SHA-256 is the better choice when collision resistance matters.
- The organizer answer's `samefile()` discussion suggests the source may already be in its target directory, but the loop only considers files directly inside the root. This version simply skips directories on a second run, which makes that run a no-op.

Run this chapter's tests from the repository root:

```bash
python3 -m unittest chapters.chapter_34_os_path_and_pathlib.test_solutions
```
