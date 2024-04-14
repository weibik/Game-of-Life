import numpy as np
from game_of_life.game_logic import get_num_of_neighbours, set_cell_value
from game_of_life.config import WHITE, BLACK, GRID_COLOR
import pygame


def update_board(board, rows, cols):
    """ Update each cell in the board depending on the neighbours. """
    new_board = np.copy(board)
    for i in range(rows):
        for j in range(cols):
            num_of_neighbours = get_num_of_neighbours(board, i, j, rows, cols)
            new_board[i][j] = set_cell_value(board[i][j], num_of_neighbours)
    board = np.copy(new_board)
    return board


def draw_board(screen, board, rows, cols, rect_width, rect_height, black_mode=True):
    if black_mode:
        main_color, second_color = WHITE, BLACK
    else:
        main_color, second_color = BLACK, WHITE
    for row in range(rows):
        for col in range(cols):
            color = main_color if board[row][col] == 0 else second_color
            pygame.draw.rect(
                screen,
                color,
                (col * rect_width, row * rect_height, rect_width, rect_height),
            )
            pygame.draw.rect(
                screen,
                GRID_COLOR,
                (col * rect_width, row * rect_height, rect_width, rect_height),
                1,
            )


def draw_button(screen, rect, color, text, text_color):
    pygame.draw.rect(screen, color, rect)
    font = pygame.font.SysFont(None, 30)
    button_text = font.render(text, True, text_color)
    text_rect = button_text.get_rect(center=rect.center)
    screen.blit(button_text, text_rect)
