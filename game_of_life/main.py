from config import WIDTH, HEIGHT, WHITE, BUTTON_COLOR, BUTTON_TEXT_COLOR, ROWS, COLS
from drawing import update_board, draw_board, draw_button
import numpy as np
import pygame

pygame.init()


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
