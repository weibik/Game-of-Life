import numpy as np
import pygame
pygame.init()

WIDTH = 800
HEIGHT = 800

COLS = int(HEIGHT / 10)
ROWS = int(WIDTH / 10)

RECT_WIDTH = WIDTH / COLS
RECT_HEIGHT = HEIGHT / ROWS

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def draw_board(screen, board):
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 1:
                color = BLACK
            else:
                color = WHITE
            rect = pygame.Rect(col * RECT_WIDTH, row * RECT_HEIGHT, RECT_WIDTH, RECT_HEIGHT)
            pygame.draw.rect(screen, color, rect)


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


def run():
    running = True
    clock = pygame.time.Clock()

    board = np.zeros([ROWS, COLS], dtype="int64")
    midlle_row = ROWS // 2
    midlle_col = COLS // 2
    board[midlle_row][midlle_col] = 1
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        draw_board(screen, board)
        pygame.display.flip()


if __name__ == "__main__":
    run()
    pygame.quit()
