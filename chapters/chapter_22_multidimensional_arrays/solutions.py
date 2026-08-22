"""Solutions for the Chapter 22 exercises."""

from collections import deque


def _shape(matrix):
    if not matrix or not matrix[0]:
        raise ValueError("matrix must not be empty")
    columns = len(matrix[0])
    if any(len(row) != columns for row in matrix):
        raise ValueError("matrix rows must have equal lengths")
    return len(matrix), columns


def q01_corner_grid():
    """Return a 4 by 4 zero grid whose corners contain one."""
    grid = [[0] * 4 for _ in range(4)]
    for row, column in ((0, 0), (0, 3), (3, 0), (3, 3)):
        grid[row][column] = 1
    return grid


def q02_column_and_transpose(matrix, column=1):
    """Return one column and a list-of-lists transpose."""
    _, columns = _shape(matrix)
    if not 0 <= column < columns:
        raise IndexError("column is outside the matrix")
    selected = [row[column] for row in matrix]
    transposed = [list(values) for values in zip(*matrix)]
    return selected, transposed


def q03_shared_row_trap():
    """Return a mutated repeated-row grid and identity checks."""
    grid = [[0] * 3] * 3
    grid[0][0] = 99
    return grid, grid[0] is grid[1], grid[1] is grid[2]


def q04_matrix_sum(matrix):
    """Return the sum of all values in a rectangular matrix."""
    _shape(matrix)
    return sum(sum(row) for row in matrix)


def q05_elementwise_sum(first, second):
    """Return the element-wise sum of same-shaped matrices."""
    first_shape = _shape(first)
    if _shape(second) != first_shape:
        raise ValueError("matrices must have the same shape")
    return [
        [left + right for left, right in zip(first_row, second_row)]
        for first_row, second_row in zip(first, second)
    ]


def q06_rotate_clockwise(matrix):
    """Return a square matrix rotated 90 degrees clockwise."""
    rows, columns = _shape(matrix)
    if rows != columns:
        raise ValueError("matrix must be square")
    return [list(row)[::-1] for row in zip(*matrix)]


def q07_tic_tac_toe_winner(board):
    """Return ``'X'``, ``'O'``, or ``None`` for a 3 by 3 board."""
    if _shape(board) != (3, 3):
        raise ValueError("board must be 3 by 3")
    lines = list(board)
    lines.extend([list(column) for column in zip(*board)])
    lines.append([board[index][index] for index in range(3)])
    lines.append([board[index][2 - index] for index in range(3)])
    for line in lines:
        if line[0] in ("X", "O") and line.count(line[0]) == 3:
            return line[0]
    return None


def q08_matrix_multiply(first, second):
    """Return the matrix product of two compatible matrices."""
    first_rows, first_columns = _shape(first)
    second_rows, second_columns = _shape(second)
    if first_columns != second_rows:
        raise ValueError("first columns must equal second rows")
    result = [[0] * second_columns for _ in range(first_rows)]
    for row in range(first_rows):
        for column in range(second_columns):
            for shared in range(first_columns):
                result[row][column] += first[row][shared] * second[shared][column]
    return result


def q09_maze_has_path(maze, start, end):
    """Return whether open cells connect *start* to *end* using four-way moves."""
    rows, columns = _shape(maze)
    for point in (start, end):
        if len(point) != 2 or not (0 <= point[0] < rows and 0 <= point[1] < columns):
            raise ValueError("start and end must be cells inside the maze")
    if maze[start[0]][start[1]] != " " or maze[end[0]][end[1]] != " ":
        return False
    queue = deque([start])
    visited = {start}
    while queue:
        row, column = queue.popleft()
        if (row, column) == end:
            return True
        for row_step, column_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            neighbor = row + row_step, column + column_step
            neighbor_row, neighbor_column = neighbor
            if (
                0 <= neighbor_row < rows
                and 0 <= neighbor_column < columns
                and neighbor not in visited
                and maze[neighbor_row][neighbor_column] == " "
            ):
                visited.add(neighbor)
                queue.append(neighbor)
    return False


def q10_numpy_operations(matrix, first, second, left, right):
    """Return results of NumPy-compatible sum, addition, and ``@`` operations."""
    return matrix.sum(), first + second, left @ right


if __name__ == "__main__":
    print(q01_corner_grid())
    print(q06_rotate_clockwise([[1, 2], [3, 4]]))
