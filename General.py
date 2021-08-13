from Piece import Piece

class General(Piece):
    """Creates General game piece"""

    def __init__(self, color):
        """general will inherit from Piece parent class"""
        super().__init__(color)
        self._name = 'General'

    def __repr__(self):
        """override object display on the game board for testing purposes"""
        return self._name[0:2]

    def get_name(self):
        """getter for self._name"""
        return self._name

    def is_valid_move(self, board, curr, dest):
        """determines the valid moves for the general"""
        # general cannot leave palace
        # move 1 unit in any direction
        # cannot move into occupied square by friendly unit

        x1, y1 = curr[0], curr[1]
        x2, y2 = dest[0], dest[1]

        # attempt to move out of palace
        if not board.is_in_palace(curr) and not board.is_in_palace(dest):
            return False

        # attempt to move more than 1 unit
        if abs(x2 - x1) > 1 or abs(y2 - y1) > 1:
            return False

        # attempt to move to an occupied square by friendly unit
        if self.get_color() == 'red':
            if board.get_board()[x2][y2] != '' and board.get_board()[x2][y2].get_color() == 'red':
                return False
        elif self.get_color() == 'blue':
            if board.get_board()[x2][y2] != '' and board.get_board()[x2][y2].get_color() == 'blue':
                return False
        return True


