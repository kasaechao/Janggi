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

    def is_valid_move(self, board):
        """determines if the requested move is a valid move"""
        pass


