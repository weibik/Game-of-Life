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
BUTTON_COLOR = (0, 128, 255)
BUTTON_TEXT_COLOR = WHITE


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

    start_stop_button_rect = pygame.Rect(WIDTH - 200, 10, 80, 30)
    start_stop_button_color = BUTTON_COLOR
    start_stop_button_text = "Start"
    start_stop_button_text_color = BUTTON_TEXT_COLOR
    start_stop_button_clicked = False

    clear_button_rect = pygame.Rect(WIDTH - 100, 10, 80, 30)
    clear_button_color = BUTTON_COLOR
    clear_button_text = "Clear"
    clear_button_text_color = BUTTON_TEXT_COLOR

    drawing_mode = False

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                cell_x = x // (WIDTH // COLS)
                cell_y = y // (HEIGHT // ROWS)

                if start_stop_button_rect.collidepoint(x, y):
                    start_stop_button_clicked = not start_stop_button_clicked
                    if start_stop_button_clicked:
                        start_stop_button_color = (255, 0, 0)
                        start_stop_button_text = "Stop"
                    else:
                        start_stop_button_color = BUTTON_COLOR
                        start_stop_button_text = "Start"
                elif clear_button_rect.collidepoint(x, y):
                    board = np.zeros([ROWS, COLS], dtype="int64")
                else:
                    drawing_mode = True
                    board[cell_y][cell_x] = 1 - board[cell_y][cell_x]
            elif event.type == pygame.MOUSEBUTTONUP:
                drawing_mode = False

        screen.fill(WHITE)
        draw_board(screen, board)

        if start_stop_button_clicked and not drawing_mode:
            board = update_board(board, ROWS, COLS)
            pygame.time.delay(100)

        draw_button(
            screen,
            start_stop_button_rect,
            start_stop_button_color,
            start_stop_button_text,
            start_stop_button_text_color,
        )
        draw_button(
            screen,
            clear_button_rect,
            clear_button_color,
            clear_button_text,
            clear_button_text_color,
        )

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    run()
