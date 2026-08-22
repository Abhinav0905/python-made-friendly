# Multidimensional Arrays

## Check Your Understanding

1. The outer `* 3` repeats references to one inner list instead of constructing three independent rows.
2. Extract column `c` with `[row[c] for row in matrix]` after checking that each row contains that position.
3. `zip(*matrix)` unpacks the rows and groups values at matching column positions, producing the transpose as tuples.
4. Choose NumPy for large numerical grids, vectorized arithmetic, multidimensional slicing, matrix algebra or numerical speed. Lists of lists fit small boards and general Python objects.

## Try It Yourself

1. Build a 4 by 4 corner-marked grid: `q01_corner_grid`.
2. Extract the second column and transpose a matrix: `q02_column_and_transpose`.
3. Demonstrate the shared-row multiplication trap: `q03_shared_row_trap`.
4. Sum every matrix value: `q04_matrix_sum`.
5. Add same-shaped matrices element by element: `q05_elementwise_sum`.
6. Rotate a square matrix clockwise: `q06_rotate_clockwise`.
7. Check a tic-tac-toe winner: `q07_tic_tac_toe_winner`.
8. Multiply compatible matrices without NumPy: `q08_matrix_multiply`.
9. Test maze reachability with breadth-first search: `q09_maze_has_path`.
10. Run NumPy-style sum, element-wise addition and matrix multiplication: `q10_numpy_operations`.

Exercise 10 works with NumPy arrays but does not import NumPy, so the package stays optional. Its test uses a small object that implements the same operations. With NumPy, the three calculations are the one-line expressions `matrix.sum()`, `first + second`, and `left @ right`; the pure-Python versions expose the loops and validation that those operations hide.
