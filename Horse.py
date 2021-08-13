from Piece import Piece


class Horse(Piece):
    """Creates General game piece"""

    def __init__(self, color):
        """general will inherit from Piece parent class"""
        super().__init__(color)
        self._name = 'Horse'

    def __repr__(self):
        """override object display on the game board for testing purposes"""
        return self._name[0:2]

    def get_name(self):
        """getter for self._name"""
        return self._name

    def is_valid_move(self, board:object, curr, dest):
        """determines the valid moves for the Horse"""
        # moves one orthogonally 1 and 1 diagonal
        # cannot jump over pieces
        # 4 movement scenarios
        x1, y1 = curr[0], curr[1]
        x2, y2 = dest[0], dest[1]

        # initial check for valid movement
        if abs(x2 - x1) == 1 and abs(y2 - y1) == 2:
            # check for invalid up movements
            if (y2 - y1) == -2:
                if board.get_board()[y1 - 1][x1] != '':     # path is blocked
                    if board.get_board()[y1 - 1][x1].get_color() == self.get_color():
                        return False
                if (x2 - x1) > 0 and board.get_board()[y2][x2] != '':   # up-left movement or up-right move
                    if board.get_board()[y2][x2].get_color() == self.get_color():
                        return False
                elif (x2 - x1) < 0 and board.get_board()[y2][x2] != '':
                    if board.get_board()[y2][x2].get_color() == self.get_color():
                        return False

            # check for invalid down movements
            elif (y2 - 1) == 2:
                if board.get_board()[y1 + 1][x1] != '':     # path is blocked
                    if board.get_board()[y1 + 1][x1].get_color() == self.get_color():
                        return False
                if (x2 - x1) > 0 and board.get_board()[y2][x2] != '':   # down-left movement or down-right move
                    if board.get_board()[y2][x2].get_color() == self.get_color():
                        return False
                elif (x2 - x1) < 0 and board.get_board()[y2][x2] != '':
                    if board.get_board()[y2][x2].get_color() == self.get_color():
                        return False

        elif abs(x2 - x1) == 2 and abs(y2 - y1) == 1:
            # check for invalid right movements
            if (x2 - x1) == 2:
                if board.get_board()[y1][x1 + 1] != '':     # path is blocked
                    if board.get_board()[y1][x1 + 1].get_color() == self.get_color():
                        return False
                if (y2 - y1) > 0 and board.get_board()[y2][x2] != '':   # right-up or right-down
                    if board.get_board()[y2][x2].get_color() == self.get_color():
                        return False
                elif (y2 - y1) < 0 and board.get_board()[y2][x2] != '':
                    if board.get_board()[y2][x2].get_color() == self.get_color():
                        return False

            # check for invalid left movements
            elif (x2 - x1) == -2:
                if board.get_board()[y1][x1 - 1] != '':     # path is blocked
                    if board.get_board()[y1][x1 - 1].get_color() == self.get_color():
                        return False
                if (y2 - y1) > 0 and board.get_board()[y2][x2] != '':   # left-up or left-down
                    if board.get_board()[y2][x2].get_color() == self.get_color():
                        return False
                elif (y2 - y1) < 0 and board.get_board()[y2][x2] != '':
                    if board.get_board()[y2][x2].get_color() == self.get_color():
                        return False
        else:
            return False    # movement is too many units

        return True

