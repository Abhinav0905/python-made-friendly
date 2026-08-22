# Arrays

## Check Your Understanding

1. `array.array` packs raw values of one C type together. A list stores pointers to separate Python objects, which costs more memory.
2. Type code `'d'` means a double-precision floating-point value.
3. A NumPy array adds vectorized arithmetic, multidimensional operations and numerical methods. `array.array` is mainly compact storage and binary I/O.
4. Choose `array.array` when you need compact homogeneous numeric storage, a fixed C-compatible representation or binary I/O without installing another package.

## Try It Yourself

1. Build and inspect an integer array: `q01_integer_array`.
2. Compare shallow container sizes: `q02_memory_comparison`.
3. Write and read raw binary integers: `q03_write_and_read_binary`.
4. Produce running statistics for floating-point measurements: `q04_running_statistics`.
5. Calculate running statistics through the NumPy array protocol: `q05_numpy_running_statistics`.
6. Generate one random data set and compare NumPy-style and list timing: `q06_generate_and_compare`.

Exercises 5 and 6 accept a NumPy array or module when NumPy is installed, but this companion repo does not make a third-party package mandatory. The tests use tiny protocol-compatible stand-ins. Exercise 6 gives both implementations the same random values, making the timing comparison fair.

The manuscript's Question 3 explanation calls the value filled by `array.fromfile` a NumPy array. It is an `array.array`; the solution uses that standard-library type. Exact `getsizeof` results in Exercise 2 also depend on the Python build and operating system, so the function reports measured sizes instead of fixed byte counts.
