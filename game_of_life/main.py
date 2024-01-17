from calculations import get_num_of_neighbours, set_cell_value

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
GRID_COLOR = (80, 80, 80)


def draw_board(screen, board):
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if board[row][col] == 0 else BLACK
            pygame.draw.rect(screen, color, (col * RECT_WIDTH, row * RECT_HEIGHT, RECT_WIDTH, RECT_HEIGHT))
            pygame.draw.rect(screen, GRID_COLOR, (col * RECT_WIDTH, row * RECT_HEIGHT, RECT_WIDTH, RECT_HEIGHT), 1)


def update_board(board, r, c):
    new_board = np.copy(board)
    for i in range(r):
        for j in range(c):
            num_of_neighbours = get_num_of_neighbours(board, i, j)
            new_board[i][j] = set_cell_value(board[i][j], num_of_neighbours)
    board = np.copy(new_board)
    return board


def run():
    running = True
    clock = pygame.time.Clock()

    board = np.zeros([ROWS, COLS], dtype="int64")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                cell_x = x // (WIDTH // COLS)
                cell_y = y // (HEIGHT // ROWS)

                board[cell_y][cell_x] = 1 - board[cell_y][cell_x]

        screen.fill(WHITE)
        draw_board(screen, board)

        board = update_board(board, ROWS, COLS)

        pygame.display.flip()
        pygame.time.delay(1000)


if __name__ == "__main__":
    run()
    pygame.quit()
