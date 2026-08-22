"""Tests for Chapter 22."""

import unittest

from chapters.chapter_22_multidimensional_arrays import solutions


class FakeMatrix:
    def __init__(self, rows):
        self.rows = [list(row) for row in rows]

    def sum(self):
        return sum(sum(row) for row in self.rows)

    def __add__(self, other):
        return FakeMatrix(solutions.q05_elementwise_sum(self.rows, other.rows))

    def __matmul__(self, other):
        return FakeMatrix(solutions.q08_matrix_multiply(self.rows, other.rows))

    def __eq__(self, other):
        return isinstance(other, FakeMatrix) and self.rows == other.rows


class MultidimensionalArrayTests(unittest.TestCase):
    def test_easy_exercises(self):
        self.assertEqual(
            solutions.q01_corner_grid(),
            [[1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1]],
        )
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(
            solutions.q02_column_and_transpose(matrix),
            ([2, 5, 8], [[1, 4, 7], [2, 5, 8], [3, 6, 9]]),
        )
        grid, first_shared, second_shared = solutions.q03_shared_row_trap()
        self.assertEqual(grid, [[99, 0, 0], [99, 0, 0], [99, 0, 0]])
        self.assertTrue(first_shared and second_shared)

    def test_medium_exercises(self):
        self.assertEqual(solutions.q04_matrix_sum([[1, 2], [3, 4]]), 10)
        self.assertEqual(
            solutions.q05_elementwise_sum([[1, 2], [3, 4]], [[5, 6], [7, 8]]),
            [[6, 8], [10, 12]],
        )
        with self.assertRaises(ValueError):
            solutions.q05_elementwise_sum([[1, 2]], [[1], [2]])
        self.assertEqual(
            solutions.q06_rotate_clockwise([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
        )
        self.assertEqual(
            solutions.q07_tic_tac_toe_winner([["X", "O", " "], ["O", "X", " "], [" ", "O", "X"]]),
            "X",
        )
        self.assertIsNone(
            solutions.q07_tic_tac_toe_winner([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]])
        )

    def test_hard_exercises(self):
        self.assertEqual(
            solutions.q08_matrix_multiply([[1, 2], [3, 4], [5, 6]], [[7, 8, 9], [10, 11, 12]]),
            [[27, 30, 33], [61, 68, 75], [95, 106, 117]],
        )
        maze = [list("  # "), list("# # "), list("#   "), list("##  ")]
        self.assertTrue(solutions.q09_maze_has_path(maze, (0, 0), (3, 3)))
        blocked = [list(" # "), list("###"), list(" # ")]
        self.assertFalse(solutions.q09_maze_has_path(blocked, (0, 0), (0, 2)))
        matrix = FakeMatrix([[1, 2], [3, 4]])
        total, added, multiplied = solutions.q10_numpy_operations(
            matrix,
            FakeMatrix([[1, 2], [3, 4]]),
            FakeMatrix([[5, 6], [7, 8]]),
            FakeMatrix([[1, 2], [3, 4]]),
            FakeMatrix([[2], [1]]),
        )
        self.assertEqual(total, 10)
        self.assertEqual(added, FakeMatrix([[6, 8], [10, 12]]))
        self.assertEqual(multiplied, FakeMatrix([[4], [10]]))


if __name__ == "__main__":
    unittest.main()
