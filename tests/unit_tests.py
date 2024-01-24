import unittest
import numpy as np
import pygame
from game_of_life.drawing import update_board, draw_button
from game_of_life.game_logic import initialize_board, get_num_of_neighbours, set_cell_value


class TestGameLogic(unittest.TestCase):
    def test_initialize_board(self):
        rows, cols = 5, 5
        board = initialize_board(rows, cols)
        self.assertEqual(np.shape(board), (rows, cols))
        self.assertTrue(np.all(board == 0))

    def test_get_num_of_neighbours(self):
        board = np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        x, y = 1, 1
        result = get_num_of_neighbours(board, x, y, 3, 3)
        self.assertEqual(result, 4)

    def test_set_cell_value(self):
        state = 1
        num_of_neighbours = 2
        result = set_cell_value(state, num_of_neighbours)
        self.assertEqual(result, 1)

        state = 1
        num_of_neighbours = 4
        result = set_cell_value(state, num_of_neighbours)
        self.assertEqual(result, 0)

        state = 0
        num_of_neighbours = 3
        result = set_cell_value(state, num_of_neighbours)
        self.assertEqual(result, 1)


class TestDrawing(unittest.TestCase):
    def test_draw_button(self):
        pygame.init()

        screen_mock = pygame.Surface((800, 600))
        rect = pygame.Rect(50, 50, 100, 30)
        color = (0, 128, 255)
        text = "Test Button"
        text_color = (255, 255, 255)

        draw_button(screen_mock, rect, color, text, text_color)

        self.assertEqual(screen_mock.get_at((55, 55)), color)

        pygame.quit()


class TestUpdateBoard(unittest.TestCase):
    def test_update_board(self):
        board = np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        updated_board = update_board(board, 3, 3)
        expected_board = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
        self.assertTrue(np.array_equal(updated_board, expected_board))
