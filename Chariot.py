from Piece import Piece


class Chariot(Piece):
    """Creates General game piece"""

    def __init__(self, color):
        """general will inherit from Piece parent class"""
        super().__init__(color)
        self._name = 'Chariot'

    def __repr__(self):
        """override object display on the game board for testing purposes"""
        return self.get_color()[0] + "." + self._name[0:2]

    def get_name(self):
        """getter for self._name"""
        return self._name

    def is_valid_move(self, board, curr, dest):
        """determines the valid moves for the Chariot"""
        # moves and captures in a straight line horizontally or vertically
        # can move diagonally along the diagonally lines of the palace

        x1, y1 = curr[0], curr[1]
        x2, y2 = dest[0], dest[1]

        # attempt to move diagonally while outside the palace
        if not board.is_in_palace(curr) and abs(x2 - x1) > 0 and abs(y2 - y1) > 0:
            return False

        # attempt to move diagonally from palace to outside of palace
        if board.is_in_palace(curr) and not board.is_in_palace(dest):
            return False

        # attempt to move horizontally but blocked by a unit
        if abs(x2 - x1) > 0 and abs(y2 - y1) == 0:
            i = 0
            is_blocked = False
            if x2 - x1 > 0:  # move right

                while not is_blocked and i < x2:
                    if board.get_board()[y2][x1 + i] != '__':
                        break
                    i += 1
            else:  # move left
                while not is_blocked and i > x2:
                    if board.get_board()[y2][x1 + i] != '__':
                        break
                    i -= 1
            if not is_blocked:
                # check for capture event at the dest
                if board.get_board()[y2][x2] != '__':
                    if board.get_board()[y2][x2].get_color() == self.get_color():
                        return False

        # attempt to vertically but blocked by a unit
        elif abs(x2 - x1) == 0 and abs(y2 - y1) > 0:
            i = 0
            is_blocked = False

            if y2 - y1 > 0:  # move down
                while not is_blocked and i < y2:
                    if board.get_board()[y1 + 1][x2] != '__':
                        break
                    i += 1
            else:  # move up
                while not is_blocked and i > y2:
                    if board.get_board()[y1 - 1][x2] != '__':
                        break
                    i -= 1
            if not is_blocked:
                # check for capture event at the dest
                if board.get_board()[y2][x2] != '__':
                    if board.get_board()[y2][x2].get_color() == self.get_color():
                        return False

        return True
