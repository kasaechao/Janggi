class Board:
    """Creates a new playing board with initial pieces and their locations"""

    def __init__(self):
        self._board = [["__" for col in range(9)] for row in range(10)]

    def print_board(self):
        """print the board and its pieces for testing and playing"""
        print("  ", '  a ', '   b ', '   c ', '   d ', '   e ', '   f ', '   g ', '   h ', '   i ')
        [print(row + 1, "", self._board[row]) for row in range(len(self._board) - 1)]
        [print(row + 1, self._board[row]) for row in range(len(self._board) - 1, len(self._board))]

    def get_board(self):
        """get method for self._board"""
        return self._board

    def set_board(self, coord: tuple, piece):
        """modify the board, coord = (row, col)"""
        col = coord[0]
        row = coord[1]
        self._board[row][col] = piece

    @staticmethod
    def is_in_palace(coord) -> bool:
        """check if current location is int he palace"""

        red_palace_locations = [(3, 0), (4, 0), (5, 0),
                                (3, 1), (4, 1), (5, 1),
                                (3, 2), (4, 2), (5, 2)]
        blue_palace_locations = [(3, 7), (4, 7), (5, 7),
                                 (3, 8), (4, 8), (5, 8),
                                 (3, 9), (4, 9), (5, 9)]
        if coord in red_palace_locations:
            return True
        if coord in blue_palace_locations:
            return True

        return False
