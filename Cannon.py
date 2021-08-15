from Piece import Piece


class Cannon(Piece):
    """Creates General game piece"""

    def __init__(self, color):
        """general will inherit from Piece parent class"""
        super().__init__(color)
        self._name = 'Cannon'

    def __repr__(self):
        """override object display on the game board for testing purposes"""
        return self.get_color()[0] + "." + self._name[0:2]

    def get_name(self):
        """getter for self._name"""
        return self._name

    def is_valid_move(self, board, curr, dest):
        """determines the valid moves for the Cannon"""
        # moves orthogonally, must jump over exactly one other piece
        # can move and capture diagonally while in the palace
        # cannot capture another cannon
        x1, y1 = curr[0], curr[1]
        x2, y2 = dest[0], dest[1]

        # attempt to move diagonally while outside the palace
        if not board.is_in_palace(curr) and abs(x2 - x1) > 0 and abs(y2 - y1) > 0:
            return False

        # attempt to move diagonally from palace to outside of palace
        if board.is_in_palace(curr) and not board.is_in_palace(dest):
            return False

        # attempt to move diagonally in the palace without a jump piece
        if board.is_in_palace(curr) and board.is_in_palace(dest) and abs(x2 - x1) > 0 and abs(y2 - y1) > 0:
            if curr == (3, 0) or curr == (5, 0) or curr == (3, 2) or curr == (5, 2):  # red palace event:
                if board.get_board()[1][4] == '__':
                    return False
                if board.get_board()[y2][x2].get_color() == self.get_color(): # check for invalid capture
                    return False
            elif curr == (3, 7) or curr == (5, 6) or curr == (3, 9) or curr == (5, 9):  # blue palace event:
                if board.get_board()[8][4] == '__':
                    return False
                if board.get_board()[y2][x2].get_color() == self.get_color(): # check for invalid capture
                    return False

        # attempt to move horizontally but blocked by a unit
        if abs(x2 - x1) > 0 and abs(y2 - y1) == 0:
            i = 1
            is_blocked = False
            unit_count = 0
            if x2 - x1 > 0:  # move right
                while not unit_count > 2 and (x1 + i) < x2:
                    if board.get_board()[y2][x1 + i] != '__':
                        if board.get_board()[y2][x1 + i].get_name() == 'Cannon':
                            is_blocked = True
                            break
                        unit_count += 1
                    i += 1
                if unit_count < 1 or unit_count > 2:
                    is_blocked = True
            else:  # move left
                i = -1
                while not is_blocked and (x1 + i) > x2:
                    if board.get_board()[y2][x1 + i] != '__':
                        if board.get_board()[y2][x1 + i].get_name() == 'Cannon':
                            is_blocked = True
                            break
                        unit_count += 1
                    i -= 1
                if unit_count < 1 or unit_count > 2:
                    is_blocked = True

            if is_blocked:
                return False

            if not is_blocked:
                # check for capture event at the dest
                if board.get_board()[y2][x2] != '__':
                    if board.get_board()[y2][x2].get_color() == self.get_color():
                        return False
                    if board.get_board()[y2][x2].get_name() == 'Cannon':
                        return False


        # attempt to vertically but blocked by a unit
        elif abs(x2 - x1) == 0 and abs(y2 - y1) > 0:
            i = 1
            is_blocked = False
            unit_count = 0

            if y2 - y1 > 0:  # move down
                while not is_blocked and (y1 + i) < y2:
                    if board.get_board()[y1 + i][x2] != '__':
                        if board.get_board()[y1 + i][x2].get_name() == 'Cannon':
                            is_blocked = True
                            break
                        unit_count += 1
                    i += 1
                if unit_count < 1 or unit_count > 2:
                    is_blocked = True

            else:  # move up
                i = -1
                while not is_blocked and (y1 + i) > y2:
                    if board.get_board()[y1 + i][x2] != '__':
                        if board.get_board()[y1 + i][x2].get_name() == 'Cannon':
                            is_blocked = True
                            break
                        unit_count += 1
                    i -= 1
                if unit_count < 1 or unit_count > 2:
                    is_blocked = True
            if is_blocked:
                return False

            if not is_blocked:
                # check for capture event at the dest
                if board.get_board()[y2][x2] != '__':
                    if board.get_board()[y2][x2].get_color() == self.get_color():
                        return False
                    if board.get_board()[y2][x2].get_name() == 'Cannon':
                        return False

        return True
