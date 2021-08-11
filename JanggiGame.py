from Player import Player
from Board import Board


class JanggiGame:
    """
    main class to play Janggi
    """

    def __init__(self):
        """initial state of the game when a new game is created."""
        self._game_state = "UNFINISHED"
        self._red_player = Player('red')
        self._blue_player = Player('blue')
        self._in_check = None
        self._board = Board()

        # Setup the board
        red_pieces = self._red_player.get_pieces()
        blue_pieces = self._blue_player.get_pieces()
        for piece in red_pieces:
            coord = self.convert_coord(red_pieces[piece]['initial_location'])
            self._board.set_board(coord, red_pieces[piece]['name'])
        for piece in blue_pieces:
            coord = self.convert_coord(blue_pieces[piece]['initial_location'])
            self._board.set_board(coord, blue_pieces[piece]['name'])

    # ***************** UTILITY FUNCTION TO CONVERT COORDINATE TO LIST INDICES ************************
    @staticmethod
    def convert_coord(coord: str) -> tuple:
        """convert the requested move to valid board indices"""
        key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        col = int(coord[1:]) - 1
        for index in range(len(key)):
            if coord[0] == key[index]:
                row = index
                return col, row
        return None, None

    # ***************** GET METHODS FOR THE PRIMARY DATA MEMBERS IN THE INIT FUNCTION *****************
    def get_game_state(self):
        """get current game state"""
        return self._game_state

    def is_in_check(self):
        """get player in check"""
        return self._in_check

    def get_board(self):
        """get the current board"""
        return self._board

    def get_red_player(self):
        """get player private data member"""
        return self._red_player

    def get_blue_player(self):
        """get player private data member"""
        return self._blue_player

    def make_move(self, curr, dest):
        """moves a valid piece on the board"""
        pass


game = JanggiGame()
game.get_board().print_board()
