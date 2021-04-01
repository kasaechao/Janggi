import pygame, os, sys


class Board:
    """Janggi game board"""

    def __init__(self):
        self._board_img = pygame.image.load(os.path.join('images/JanggiWood.png'))
        self._board = [['  ' for col in range(9)] for row in range(10)]  # row x col calls
        self._board_size = (450, 500)

    def get_board_size(self):
        return self._board_size

    def get_board_img(self):
        return self._board_img

    def coord_to_pix(self, coord):
        x_coord = coord[1]
        y_coord = coord[0]
        origin = 0, 0
        # offset will depend on board size
        # current board size of 450x500 provides easy math
        offset = 50
        if x_coord != 0:
            x_coord = (x_coord * offset)
        else:
            x_coord = origin[0]
        if y_coord != 0:
            y_coord = (y_coord * offset)
        else:
            y_coord = origin[1]
        return x_coord, y_coord

    def pix_to_coord(self, coord):
        x_coord = coord[1]
        y_coord = coord[0]
        origin = 0, 0
        offset = 50
        if x_coord != 0:
            x_coord = (x_coord // offset)
        else:
            x_coord = origin[0]
        if y_coord != 0:
            y_coord = (y_coord // offset)
        else:
            y_coord = origin[1]
        return x_coord, y_coord

    def display_board(self):
        for row in self._board:
            print(row)

    def get_board(self):
        return self._board

    def set_board(self, coord, piece):
        self._board[coord[0]][coord[1]] = piece
        return self._board

    def is_in_board(self, coord):
        col = coord[1]
        row = coord[0]
        right_bound = 8
        left_bound = 0
        top_bound = 0
        bot_bound = 9
        if (row < left_bound or row > right_bound) or (col < top_bound or col > bot_bound):
            return False
        return True

    def is_in_palace_blue(self, coord):
        col = coord[1]
        row = coord[0]
        right_bound = 5
        left_bound = 2
        top_bound_blue = 7
        if (col < left_bound or col > right_bound) or row < top_bound_blue:
            print('cant leave palace')
            return False
        return True

    def is_in_palace_red(self, coord):
        col = coord[1]
        row = coord[0]
        right_bound = 5
        left_bound = 2
        top_bound_red = 2
        if (col < left_bound or col > right_bound) or row > top_bound_red:
            print('cant leave palace')
            return False
        return True

    def is_in_palace_corners(self, coord):
        bot_right_blue = (9, 5)
        bot_left_blue = (9, 3)
        top_left_blue = (7, 3)
        top_right_blue = (7, 5)
        bot_right_red = (2, 5)
        bot_left_red = (2, 3)
        top_left_red = (0, 3)
        top_right_red = (0, 5)
        mid_blue = (8, 4)
        mid_red = (1, 4)

        if coord == bot_left_blue or coord == bot_right_blue or coord == top_left_blue or coord == top_right_blue or coord == mid_blue:
            return True
        if coord == bot_left_red or coord == bot_right_red or coord == top_left_red or coord == top_right_red or coord == mid_red:
            return True
        return False


