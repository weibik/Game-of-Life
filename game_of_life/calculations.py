import numpy as np

WIDTH = 800
HEIGHT = 800

COLS = int(HEIGHT / 10)
ROWS = int(WIDTH / 10)


def get_num_of_neighbours(board: np.array, row: int, col: int) -> int:
    num_of_neighbours = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            new_row, new_col = row + i, col + j
            if 0 <= new_row < ROWS and 0 <= new_col < COLS:
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