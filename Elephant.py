from Piece import Piece


class Elephant(Piece):
    """Creates General game piece"""

    def __init__(self, color):
        """general will inherit from Piece parent class"""
        super().__init__(color)
        self._name = 'Elepant'

    def __repr__(self):
        """override object display on the game board for testing purposes"""
        return self.get_color()[0] + "." + self._name[0:2]

    def get_name(self):
        """getter for self._name"""
        return self._name

    def is_valid_move(self, board, curr, dest):
        """determines the valid moves for the Elephant"""
        x1, y1 = curr[0], curr[1]
        x2, y2 = dest[0], dest[1]

        # initial check for valid movement
        # 1 orthogonal, 2 diagonal
        if abs(x2 - x1) == 2 and abs(y2 - y1) == 3:

            # check for invalid up movements
            if (y2 - y1) == -3:
                if board.get_board()[y1 - 1][x1] != '__':  # path is blocked orthogonally
                    return False

                if (x2 - x1) > 0 and board.get_board()[y2][x2] != '__':  # up-left move
                    if board.get_board[y1 - 2][x1 - 1] != '__':
                        return False
                    if board.get_board()[y2][x2].get_color() == self.get_color():
                        return False

                elif (x2 - x1) < 0 and board.get_board()[y2][x2] != '__':  # up-right move
                    if board.get_board[y1 - 2][x1 + 1] != '__':
                        return False
                    if board.get_board()[y2][x2].get_color() == self.get_color():
                        return False

            # check for invalid down movements
            elif (y2 - y1) == 3:
                if board.get_board()[y1 + 1][x1] != '__':  # path is blocked
                    return False

                if (x2 - x1) > 0 and board.get_board()[y2][x2] != '__':  # down-left move
                    if board.get_board[y1 + 2][x1 - 1] != '__':
                        return False
                    if board.get_board()[y2][x2].get_color() == self.get_color():
                        return False

                elif (x2 - x1) < 0 and board.get_board()[y2][x2] != '__':  # down-right move
                    if board.get_board[y1 + 2][x1 + 1] != '__':
                        return False
                    if board.get_board()[y2][x2].get_color() == self.get_color():
                        return False

        elif abs(x2 - x1) == 3 and abs(y2 - y1) == 2:
            # check for invalid right movements
            if (x2 - x1) == 2:
                if board.get_board()[y1][x1 + 1] != '__':  # path is blocked
                    return False
                if (y2 - y1) > 0 and board.get_board()[y2][x2] != '__':  # right-up or
                    if board.get_board[y1 - 2][x1 + 3] != '__':
                        return False
                    if board.get_board()[y2][x2].get_color() == self.get_color():
                        return False
                elif (y2 - y1) < 0 and board.get_board()[y2][x2] != '':  # right-down
                    if board.get_board[y1 + 2][x1 + 3] != '__':
                        return False
                    if board.get_board()[y2][x2].get_color() == self.get_color():
                        return False

            # check for invalid left movements
            elif (x2 - x1) == -2:
                if board.get_board()[y1][x1 - 1] != '__':  # path is blocked
                    return False
                if (y2 - y1) > 0 and board.get_board()[y2][x2] != '__':  # left-up
                    if board.get_board[y1 - 2][x1 - 3] != '__':
                        return False
                    if board.get_board()[y2][x2].get_color() == self.get_color():
                        return False
                elif (y2 - y1) < 0 and board.get_board()[y2][x2] != '__':  # left-down
                    if board.get_board[y1 + 2][x1 - 3] != '__':
                        return False
                    if board.get_board()[y2][x2].get_color() == self.get_color():
                        return False
        else:
            return False  # movement is too many units

        return True
