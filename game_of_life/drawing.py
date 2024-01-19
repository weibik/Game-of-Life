import numpy as np
from game_logic import get_num_of_neighbours, set_cell_value
from config import WHITE, BLACK, RECT_HEIGHT, RECT_WIDTH, COLS, ROWS, GRID_COLOR
import pygame


def update_board(board, r, c):
    new_board = np.copy(board)
    for i in range(r):
        for j in range(c):
            num_of_neighbours = get_num_of_neighbours(board, i, j)
            new_board[i][j] = set_cell_value(board[i][j], num_of_neighbours)
    board = np.copy(new_board)
    return board


def draw_board(screen, board):
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if board[row][col] == 0 else BLACK
            pygame.draw.rect(
                screen,
                color,
                (col * RECT_WIDTH, row * RECT_HEIGHT, RECT_WIDTH, RECT_HEIGHT),
            )
            pygame.draw.rect(
                screen,
                GRID_COLOR,
                (col * RECT_WIDTH, row * RECT_HEIGHT, RECT_WIDTH, RECT_HEIGHT),
                1,
            )


def draw_button(screen, rect, color, text, text_color):
    pygame.draw.rect(screen, color, rect)
    font = pygame.font.SysFont(None, 30)
    button_text = font.render(text, True, text_color)
    text_rect = button_text.get_rect(center=rect.center)
    screen.blit(button_text, text_rect)
