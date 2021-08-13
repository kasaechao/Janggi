from Piece import Piece


class Soldier(Piece):
    """Creates General game piece"""

    def __init__(self, color):
        """general will inherit from Piece parent class"""
        super().__init__(color)
        self._name = 'Soldier'

    def __repr__(self):
        """override object display on the game board for testing purposes"""
        return self._name[0:2]

    def get_name(self):
        """getter for self._name"""
        return self._name

    def is_valid_move(self, board: object, curr: tuple, dest: tuple) -> bool:
        """determines the valid moves for the Soldier"""

        x1, y1 = curr[0], curr[1]
        x2, y2 = dest[0], dest[1]
        is_palace_move = board.is_in_palace(curr) or board.is_in_palace(dest)

        # attempt to move out of board
        if (x2 < 0 or x2 > 9) or (y2 < 0 or y2 > 9):
            return False
        # only moves 1 unit
        # attempt to move 2 or more units
        if abs(x2 - x2) > 1 or abs(y2 - y1) > 1:
            return False
        # attempt to move diagonal while not in palace or trying to move out of palace diagonally
        if (abs(x2 - x1) > 0 and abs(y2 - y1) > 0) and not is_palace_move:
            return False
        elif (abs(x2 - x2) > 0 and abs(y2 - y1) > 0) and is_palace_move:
            # if blocked trying to move diagonally
            if board.get_board()[y2][x2] != '':
                return False

        if self._color == 'red':
            # only moves forward or sideways
            # attempt to move backwards
            if (y2 - y1) < 0:
                return False
            # if blocked by own piece
            if board.get_board()[y2][x2] != '' and board.get_board()[y2][x2].get_color() == 'red':
                return False

        elif self._color == 'blue':
            # only moves forward or sideways
            # attempt to move backwards
            if (y2 - y1) > 0:
                return False
            # if blocked by own piece
            if board.get_board()[y2][x2] != '' and board.get_board()[y2][x2].get_color() == 'blue':
                return False

        # can move diagonally forward if in the palace
        # only move side to sideways when the end of the board is reached
        # can only capture forwards or sideways
        # check if movement is only one space
        # check if movement is diagonal
        # check if theres a piece to capture if moving diagonal
        # check if at the end of the board, then only moves sideways

        return True
