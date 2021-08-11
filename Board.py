class Board:
    """Creates a new playing board with initial pieces and their locations"""

    def __init__(self):
        self._board = [["" for col in range(9)] for row in range(10)]

    def print_board(self):
        """print the board and its pieces"""
        print("  ", ' a ', ' b ', ' c ', ' d ', ' e ', ' f ', ' g ', ' h ', ' i ')
        [print(row, self._board[row]) for row in range(len(self._board))]

    def get_board(self):
        """get method for self._board"""
        return self._board

    def set_board(self, coord: tuple, piece):
        """modify the board, coord = (x,y) = (row, col)"""
        row = coord[0]
        col = coord[1]
        self._board[row][col] = piece




