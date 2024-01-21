import numpy as np


def initialize_board(rows, cols):
    return np.zeros([rows, cols], dtype="int64")


def get_num_of_neighbours(board: np.array, x: int, y: int, rows, cols) -> int:
    num_of_neighbours = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            new_row, new_col = x + i, y + j
            if 0 <= new_row < rows and 0 <= new_col < cols:
                num_of_neighbours += board[new_row][new_col]

    return num_of_neighbours


def set_cell_value(state: int, num_of_neighbours: int) -> int:
    if state == 1:
        if num_of_neighbours > 3 or num_of_neighbours < 2:
            return 0  # Cell dies due to overpopulation or underpopulation
        else:
            return 1  # Cell survives
    elif state == 0:
        if num_of_neighbours == 3:
            return 1  # Cell becomes alive due to reproduction
        else:
            return 0  # Cell remains dead
    else:
        return 0
